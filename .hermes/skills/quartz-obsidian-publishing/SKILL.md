---
name: quartz-obsidian-publishing
description: "Publish an Obsidian vault as a Quartz v5 static site — branch merge, config fixes, theme install, Vercel deployment."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [Quartz, Obsidian, Vercel, Static Site, Publishing]
    related_skills: [wiki-ingest, obsidian, vercel-deployment]
---

# Quartz + Obsidian Wiki Publishing

Use when: publishing an Obsidian vault to Quartz v5 and deploying to Vercel (or similar). Covers branch merging, config fixes, theme/plugin resolution, build verification, and Vercel setup.

## Prerequisites

- Node.js >= 22, npm >= 10.9.2
- Git repository with Quartz v5 scaffolding (from `jackyzha0/quartz`)
- Obsidian vault with markdown content in `content/`

## Step 1: Merge Vault into Quartz Repo

```bash
# In the quartz repo directory (on main/default branch, e.g. v5)
cd /path/to/quartz-repo
git remote add vault /path/to/obsidian-vault
git fetch vault
git merge vault/master --allow-unrelated-histories
```

Move vault content into Quartz's `content/` directory:

```bash
# After merge, move vault markdown into content/
# Do NOT use symlinks — user preferred direct merge
cp -r /path/to/vault/content/*.md quartz/content/ 2>/dev/null || true
```

## Step 2: Configure Quartz

### Identify the active config file

```bash
# The active config may be quartz.config.yaml OR quartz.config.default.yaml
# Check which one exists and is referenced by the build
ls quartz.config.* 2>/dev/null
```

### Fix `ignorePatterns`

The Quartz default config often has wrong ignore patterns. The Obsidian `.obsidian/` directory and `_templates/` must be excluded:

```yaml
ignorePatterns:
  - private
  - _templates          # Not "templates" — Quartz uses underscore
  - _templates/**       # Recursive
  - .obsidian
  - .obsidian/**
```

Verify actual directory names: `ls -la | grep -E 'templates|obsidian'`

### Set the correct `baseUrl`

```yaml
configuration:
  baseUrl: your-domain.vercel.app   # Update AFTER Vercel deployment
```

Leave placeholder during initial setup (e.g. `mysite.github.io/quartz`).

## Step 3: Install Dependencies

### Theme installation may fail without `--force`

```bash
npm install @quartz-themes/default --force
```

This bypasses npm script execution blocks that can be triggered in certain environments (especially Linux with specific npm versions or when `allow-scripts` is not set).

### Vercel requires `.npmrc`

Create `.npmrc` at repo root for Vercel builds:

```ini
legacy-peer-deps=true
allow-scripts=true
```

Without this, Vercel's `npm install` fails with ERESOLVE conflicts between plugins (e.g. `@quartz-community/latex` vs `@myriaddreamin/rehype-typst` peer dep mismatches).

### Install remaining dependencies

```bash
npm install
```

## Step 4: Build & Verify

```bash
npx quartz build
```

Expected output:
```
Parsed N Markdown files in Xs
Filtered out M files in X
Emitted K files to `public` in Xm
Done processing N files in Xm
```

- Exit code 0 = success
- Typical build: ~300 files → ~2000+ output files, ~90-100MB
- LaTeX warnings are cosmetic (Unicode/encoding in articles) — non-blocking

### Prettier check (optional but recommended)

```bash
npx prettier --check quartz.config.yaml
```

## Step 5: Vercel Deployment

### Commit and push first

```bash
git add -A
git commit -m "wip: configure quartz for vault publishing"
git push origin <branch>
```

### Vercel dashboard setup

1. Go to **https://vercel.com/dashboard** → "Add New..." → Project
2. Import the Git repository
3. Project name: lowercase with hyphens
4. Settings:

| Setting | Value |
|---------|-------|
| Framework Preset | **Other** |
| Root Directory | **./** |
| Build Command | `npx quartz plugin install && npx quartz build` |
| Output Directory | **public** |

5. Click "Deploy"

### Post-deployment: update baseUrl

After Vercel assigns a URL, update `quartz.config.yaml`:

```yaml
configuration:
  baseUrl: your-site.vercel.app   # No https://, no trailing slash
```

Commit, push, and Vercel auto-rebuilds.

### Add `vercel.json` for clean URLs

Quartz generates `page.html` but Vercel expects clean URLs (no `.html` extension). Create `vercel.json` at repo root:

```json
{
  "cleanUrls": true
}
```

## Step 6: Automated Builds

Vercel automatically rebuilds on every push to the connected branch — no additional CI config needed.

## Common Pitfalls

### Build fails with ERESOLVE / peer dependency conflicts
**Fix:** Add `.npmrc` with `legacy-peer-deps=true` (Step 3 above)

### Build fails with `@quartz-themes/default` not found
**Fix:** `npm install @quartz-themes/default --force` — the `--force` bypasses environment npm script blocks

### Build fails with wrong ignorePatterns
**Fix:** Check actual directory names (`ls -la`) and ensure `_templates` (not `templates`) matches

### Config file confusion
The active config is often `quartz.config.yaml`, not `quartz.config.default.yaml` (which is a stale example). Verify by checking which file the build reads.

### URLs require `.html` extension on Vercel
**Fix:** `vercel.json` with `cleanUrls: true` — required before deploying

### Git auth issues
- `gh` CLI not installed: use HTTPS token embedded in remote URL
- SSH: generate key with `ssh-keygen -t ed25519`, add public key to GitHub settings
- Token: generate at https://github.com/settings/tokens, scope `repo`

## Verification Checklist

- [ ] `npx quartz build` exits 0 with expected file counts
- [ ] `public/` contains HTML files (~1000+)
- [ ] `npx prettier --check quartz.config.yaml` passes (optional)
- [ ] Vercel deployment shows green/success status
- [ ] Site loads at `*.vercel.app` URL
- [ ] `baseUrl` updated to production domain
- [ ] Clean URLs work (no `.html` in address bar)
