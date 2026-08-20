#!/usr/bin/env python3
"""Wiki health check for the UK Consumer Harms Research wiki.

Read-only linter over the Obsidian vault (``content/``). Purpose: catch the
regressions that recur during ingestion and keep the curated knowledge graph
internally consistent — without drowning in noise.

Checks
  ERRORS   dangling-wikilink      [[slug]] in a *wiki page* that resolves nowhere
           frontmatter            unclosed '---', or a wiki page missing title/type
  WARNINGS missing-raw-frontmatter raw page missing title/type/source_url/ingested
           low-outbound-links     wiki page with fewer than 2 unique [[links]]
           non-canonical-type     type: not in the known set
           off-taxonomy-tag       tag not in SCHEMA.md (opt-in: --check-tags)
  INFO     index-count-drift      on-disk counts vs index.md claims

Scope (what matters to the knowledge graph)
  * "Wiki pages" = files in concepts/ entities/ summaries/ notes/  -> full lint.
  * "Raw pages"  = files under raw/...                              -> frontmatter only
    (raw sources carry forward-looking links by nature; not linted for danglings).
  * Root meta    = index.md, log.md, SCHEMA.md, tech-monitor-*.md, etc.
    (doc examples / placeholders) -> not linted for danglings.

Usage
    python3 scripts/wiki_health_check.py [--root PATH] [--check-tags]
                                         [--full] [--json]

  --full    print every finding (default: high-signal summary + top offenders)
  --json    emit a machine-readable report
  --check-tags  also flag tags outside the SCHEMA.md taxonomy (pre-existing noise)

Exit codes: 0 clean, 1 errors, 2 warnings only, 3 usage error.

Design notes
  * Read-only; no git (the wiki is NOT a git repo); no writes.
  * Self-locating: defaults the wiki root to the parent of this script's dir.
  * Vault root is ``<root>/content`` (Quartz contentDir + Obsidian root).
  * Link resolution mirrors how *this vault* actually links: external URLs are
    fine; attachments (.pdf/.png/...) resolve by file anywhere in the vault;
    note links resolve by path, by stem, or by page title (case-insensitive).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

LINK_DIRS = ["concepts", "entities", "summaries", "notes"]
RAW_DIR = "raw"
ROOT_PAGES = {"index.md", "log.md", "SCHEMA.md", "INGESTION_PLAN.md"}
SKIP_DIRS = {"_archive", "_templates", ".obsidian", ".git", ".quartz"}
WIKI_TYPES = {"concept", "summary", "entity", "comparison", "query", "note"}
MIN_OUTBOUND_LINKS = 2
TOP_OFFENDERS = 15

WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
TAG_TOKEN_RE = re.compile(r"\b[a-z][a-z0-9]*(?:-[a-z0-9]+)*\b")
EXTERNAL_RE = re.compile(r"^(?:https?:)?//|^[a-z][a-z0-9+.-]*:", re.IGNORECASE)

# recognized non-note file extensions (anything else with a dot is a note name,
# e.g. an arXiv id like 2607.13718 is NOT an attachment extension).
BINARY_EXTS = {
    "pdf", "png", "jpg", "jpeg", "gif", "svg", "webp", "bmp",
    "mp3", "wav", "ogg", "mp4", "mov", "m4a",
    "csv", "tsv", "xlsx", "xls", "docx", "doc", "pptx",
}


def _is_md(p: Path) -> bool:
    return p.suffix == ".md" and p.is_file()


def _frontmatter_title(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    m = re.search(r"^title:\s*(.+)$", text[4:], re.MULTILINE)
    if not m:
        return ""
    val = m.group(1).strip()
    if len(val) >= 2 and val[:1] in "\"'" and val[-1:] == val[:1]:
        val = val[1:-1]
    return val.strip()


class VaultIndex:
    """Everything needed to resolve a [[wikilink]], built once."""

    def __init__(self, vault: Path, strict_paths: bool = False):
        self.vault = vault
        self.strict_paths = strict_paths
        self.slug_map: dict[str, list[str]] = {}    # lower stem -> [rel,...]
        self.path_map: dict[str, str] = {}          # lower dir/stem -> rel
        self.title_map: dict[str, list[str]] = {}   # lower title -> [rel,...]
        self.attach_paths: set[str] = set()         # lower rel path (all files)
        self.attach_names: set[str] = set()         # lower basename (all files)
        self._build()

    def _build(self):
        for f in self.vault.rglob("*"):
            if not f.is_file():
                continue
            rel = f.relative_to(self.vault)
            if any(p in SKIP_DIRS for p in rel.parts):
                continue
            self.attach_paths.add(str(rel).lower())
            self.attach_names.add(f.name.lower())

        md_files: list[Path] = []
        for d in LINK_DIRS:
            dd = self.vault / d
            if dd.is_dir():
                md_files += [f for f in sorted(dd.iterdir()) if _is_md(f)]
        rd = self.vault / RAW_DIR
        if rd.is_dir():
            md_files += [f for f in sorted(rd.rglob("*.md"))]
        md_files += [f for f in sorted(self.vault.iterdir()) if f.is_file() and _is_md(f)]

        for f in md_files:
            relstr = str(f.relative_to(self.vault))
            self.path_map[str(f.relative_to(self.vault).with_suffix("")).lower()] = relstr
            self.slug_map.setdefault(f.stem.lower(), []).append(relstr)
            try:
                title = _frontmatter_title(f.read_text(encoding="utf-8", errors="replace"))
            except Exception:
                title = ""
            if title:
                self.title_map.setdefault(title.lower(), []).append(relstr)

    def resolve(self, target: str) -> tuple[str, str]:
        """Return (kind, detail). kind in {'page','attachment','external','dangling'}."""
        t = target.strip()
        if not t:
            return ("external", "empty")
        if EXTERNAL_RE.match(t):
            return ("external", t)
        # a note link may carry a trailing .md — strip it before lookup
        t2 = t[:-3] if t.lower().endswith(".md") else t
        low = t2.lower()
        base = low.rsplit("/", 1)[-1]
        ext = base.rsplit(".", 1)[-1] if "." in base else ""
        # attachment? only for recognized non-note extensions
        if ext in BINARY_EXTS:
            if low in self.attach_paths or base in self.attach_names:
                return ("attachment", t)
            return ("dangling", f"attachment '{t}' not found in vault")
        # path form (contains '/')
        if "/" in low:
            if low in self.path_map:
                return ("page", self.path_map[low])
            if not self.strict_paths and base in self.slug_map:
                return ("page", self.slug_map[base][0])   # dir differs; page exists
            return ("dangling", f"path '{t}' has no matching page")
        # bare note link: by stem, then by title (case-insensitive)
        if low in self.slug_map:
            return ("page", self.slug_map[low][0])
        if low in self.title_map:
            return ("page", self.title_map[low][0])
        return ("dangling", f"'{t}' matches no page slug, path, or title")


def iter_content_files(vault: Path):
    for d in LINK_DIRS:
        dd = vault / d
        if dd.is_dir():
            for f in sorted(dd.iterdir()):
                if _is_md(f):
                    yield f.relative_to(vault), f
    rd = vault / RAW_DIR
    if rd.is_dir():
        for f in sorted(rd.rglob("*.md")):
            yield f.relative_to(vault), f
    for f in sorted(vault.iterdir()):
        if f.is_file() and _is_md(f):
            yield f.relative_to(vault), f


def split_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text, "missing opening '---' frontmatter"
    m = re.search(r"^---\s*\n", text[4:], re.MULTILINE)
    if not m:
        return None, text, "missing closing '---' frontmatter"
    return text[4 : 4 + m.start()], text[4 + m.end() :], None


def parse_frontmatter(fm: str) -> dict:
    data: dict = {}
    current_list_key = None
    for raw in fm.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not (line.startswith(" ") or line.startswith("\t")):
            if ":" not in line:
                continue
            key, _, val = line.partition(":")
            val = val.strip()
            data[key.strip()] = val if val else []
            current_list_key = key.strip() if val == "" else None
            continue
        s = line.strip()
        if s.startswith("- ") and current_list_key is not None:
            if not isinstance(data.get(current_list_key), list):
                data[current_list_key] = []
            data[current_list_key].append(s[2:].strip())
    return data


def collect_tags(fm: dict) -> list[str]:
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        return re.findall(r"[A-Za-z0-9][A-Za-z0-9_./-]*", tags)
    if isinstance(tags, list):
        return [str(t).strip().strip("\"'") for t in tags if str(t).strip()]
    return []


def parse_taxonomy(vault: Path) -> set[str]:
    sc = vault / "SCHEMA.md"
    if not sc.is_file():
        return set()
    text = sc.read_text(encoding="utf-8")
    m = re.search(r"## Tag Taxonomy\s*\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
    if not m:
        return set()
    return {t.lower() for t in TAG_TOKEN_RE.findall(m.group(1))}


def count_raw(vault: Path, sub: str) -> int:
    subp = vault / "raw" / sub
    return sum(1 for f in subp.glob("*.md") if f.is_file()) if subp.is_dir() else 0


def check(vault: Path, opts: argparse.Namespace) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    info: list[str] = []

    idx = VaultIndex(vault, strict_paths=opts.strict_paths)
    taxonomy = parse_taxonomy(vault) if opts.check_tags else None

    dir_counts = Counter()
    type_counter = Counter()
    files_checked = 0

    for rel, abs_p in iter_content_files(vault):
        relstr = str(rel)
        parts = rel.parts
        top = parts[0] if len(parts) > 1 else "(root)"
        dir_counts[top] += 1
        files_checked += 1

        is_root_meta = len(parts) == 1 and rel.name in ROOT_PAGES
        is_raw = len(parts) > 1 and top == RAW_DIR
        is_wiki_page = (not is_root_meta) and (not is_raw) and (rel.parent.name in LINK_DIRS)

        text = abs_p.read_text(encoding="utf-8", errors="replace")

        # --- frontmatter ---
        fm, body, fm_err = split_frontmatter(text)
        if fm_err and not is_root_meta:
            (errors if is_wiki_page else warnings).append(
                {"type": "frontmatter", "file": relstr, "detail": fm_err})
            fm = None
        data = parse_frontmatter(fm) if fm is not None else {}
        ptype = str(data.get("type", "")).strip().lower()
        type_counter[ptype or "(none)"] += 1

        if is_wiki_page:
            if not str(data.get("title", "")).strip():
                errors.append({"type": "frontmatter", "file": relstr, "detail": "missing 'title'"})
            if not ptype:
                errors.append({"type": "frontmatter", "file": relstr, "detail": "missing 'type'"})
            elif ptype not in WIKI_TYPES:
                warnings.append({"type": "non-canonical-type", "file": relstr,
                                 "detail": f"type '{ptype}' not in {sorted(WIKI_TYPES)}"})
        elif is_raw:
            if not str(data.get("title", "")).strip():
                warnings.append({"type": "missing-raw-frontmatter", "file": relstr, "detail": "missing 'title'"})
            if not ptype:
                warnings.append({"type": "missing-raw-frontmatter", "file": relstr, "detail": "missing 'type'"})

        # --- dangling wikilinks: curated wiki pages only ---
        if is_wiki_page:
            for raw in WIKILINK_RE.findall(text):
                target = raw.split("|", 1)[0].split("#", 1)[0].strip()
                kind, detail = idx.resolve(target)
                if kind == "dangling":
                    errors.append({"type": "dangling-wikilink", "file": relstr,
                                   "detail": f"[[{raw}]] -> {detail}"})

        # --- outbound link deficit: wiki pages only ---
        if is_wiki_page:
            uniq = {l.split("|", 1)[0].strip() for l in WIKILINK_RE.findall(body)}
            uniq.discard("")
            if len(uniq) < MIN_OUTBOUND_LINKS:
                warnings.append({"type": "low-outbound-links", "file": relstr,
                                 "detail": f"only {len(uniq)} unique [[link]]s (want >= {MIN_OUTBOUND_LINKS})"})

        # --- off-taxonomy tags (opt-in): wiki pages only ---
        if taxonomy is not None and is_wiki_page:
            for tag in collect_tags(data):
                if tag and tag.lower() not in taxonomy:
                    warnings.append({"type": "off-taxonomy-tag", "file": relstr,
                                     "detail": f"tag '{tag}' not in SCHEMA.md taxonomy"})

    # --- index.md count drift (INFO) ---
    index_p = vault / "index.md"
    if index_p.is_file():
        itext = index_p.read_text(encoding="utf-8")
        claims: dict[str, int] = {}
        for m in re.finditer(r"^\|\s*([A-Za-z ]+?)\s*\|\s*(\d+)\s*\|\s*$", itext, re.MULTILINE):
            claims[m.group(1)] = int(m.group(2))
        tm = re.search(r"Total pages:\s*(\d+)", itext)
        if tm:
            claims["__total__"] = int(tm.group(1))
        label_map = {"Concepts": "concepts", "Entities": "entities", "Summaries": "summaries",
                     "Raw Papers": ("raw", "papers"), "Raw Articles": ("raw", "articles"),
                     "Raw Research": ("raw", "research"), "Raw Standards": ("raw", "standards")}
        for label, claimed in claims.items():
            if label == "__total__":
                continue
            v = label_map.get(label)
            if not v:
                continue
            actual = count_raw(vault, v[1]) if isinstance(v, tuple) else dir_counts.get(v, 0)
            if actual != claimed:
                info.append(f"index.md: {label} claims {claimed}, disk has {actual}")
        if "__total__" in claims:
            raw_total = (count_raw(vault, "papers") + count_raw(vault, "articles")
                         + count_raw(vault, "research") + count_raw(vault, "standards"))
            disk_total = (dir_counts.get("concepts", 0) + dir_counts.get("entities", 0)
                          + dir_counts.get("summaries", 0) + dir_counts.get("notes", 0) + raw_total)
            if disk_total != claims["__total__"]:
                info.append(f"index.md: Total claims {claims['__total__']}, disk has {disk_total}")

    return {
        "vault": str(vault), "files_checked": files_checked,
        "dir_counts": dict(sorted(dir_counts.items())), "type_counts": dict(sorted(type_counter.items())),
        "errors": errors, "warnings": warnings, "info": info,
        "checks": {"tags": bool(opts.check_tags), "strict_paths": bool(opts.strict_paths)},
    }


def _top_offenders(items: list[dict], n: int):
    c = Counter(it["file"] for it in items)
    return c.most_common(n)


def _render_section(title, items, icon, full: bool, by_type: bool = True):
    L = [f"{title} — {len(items)}"]
    if not items:
        L.append("  (none)")
        return L
    if full:
        by: dict[str, list[dict]] = {}
        for it in items:
            by.setdefault(it["type"], []).append(it)
        for t in sorted(by):
            L.append(f"  [{t}] ({len(by[t])})")
            for it in by[t]:
                L.append(f"    {icon} {it['file']}: {it['detail']}")
    else:
        # high-signal: counts by type, then top offending files
        tc = Counter(it["type"] for it in items)
        L.append("  by type: " + ", ".join(f"{t}={n}" for t, n in tc.most_common()))
        L.append(f"  top {min(TOP_OFFENDERS, len(_top_offenders(items, TOP_OFFENDERS)))} files:")
        for f, n in _top_offenders(items, TOP_OFFENDERS):
            sample = next(it["detail"] for it in items if it["file"] == f)
            L.append(f"    {icon} {f}: {n}  (e.g. {sample})")
        total_files = len(_top_offenders(items, 10**9))
        shown = min(TOP_OFFENDERS, total_files)
        if total_files > shown:
            L.append(f"    … +{total_files - shown} more files. Re-run with --full to list every finding.")
    L.append("")
    return L


def render_human(r: dict, full: bool) -> str:
    L = []
    bar = "=" * 64
    L.append(bar)
    L.append("WIKI HEALTH CHECK — UK Consumer Harms Research")
    L.append(bar)
    L.append(f"vault root : {r['vault']}")
    L.append(f"pages linted: {r['files_checked']}")
    L.append("dir counts : " + ", ".join(f"{k}={v}" for k, v in r["dir_counts"].items()))
    L.append("types      : " + ", ".join(f"{k}={v}" for k, v in r["type_counts"].items() if v))
    if r["checks"]["tags"]:
        L.append("tag check  : ENABLED (SCHEMA.md taxonomy)")
    L.append("")
    L += _render_section("ERRORS", r["errors"], "x", full)
    L += _render_section("WARNINGS", r["warnings"], "!", full)
    if r["info"]:
        L.append(f"INFO — {len(r['info'])}")
        for s in r["info"]:
            L.append(f"    i  {s}")
        L.append("")
    verdict = ("HEALTHY" if not r["errors"] and not r["warnings"]
               else "NEEDS ATTENTION (errors)" if r["errors"]
               else "OK (warnings only)")
    L.append(bar)
    L.append(f"VERDICT: {verdict}  [errors={len(r['errors'])} warnings={len(r['warnings'])} info={len(r['info'])}]")
    L.append(bar)
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Read-only health check for the wiki vault.")
    default_root = Path(__file__).resolve().parents[1]
    ap.add_argument("--root", default=str(default_root), help=f"wiki root dir (default: {default_root})")
    ap.add_argument("--check-tags", action="store_true",
                    help="also flag tags outside the SCHEMA.md taxonomy (pre-existing noise)")
    ap.add_argument("--strict-paths", action="store_true",
                    help="require path-form links to match the exact dir (no basename fallback)")
    ap.add_argument("--full", action="store_true", help="list every finding (default: summary + top offenders)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args(argv)

    vault = Path(args.root).resolve() / "content"
    if not vault.is_dir():
        print(f"error: vault root not found: {vault}", file=sys.stderr)
        return 3

    r = check(vault, args)
    print(json.dumps(r, indent=2) if args.json else render_human(r, args.full))
    return 1 if r["errors"] else 2 if r["warnings"] else 0


if __name__ == "__main__":
    sys.exit(main())
