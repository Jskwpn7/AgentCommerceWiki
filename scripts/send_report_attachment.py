#!/usr/bin/env python3
"""Send a report file as a REAL email attachment via Gmail SMTP.

Why this exists: himalaya v2 on this host does NOT compile `<#part filename=..>`
MML from stdin — it has no `template` subcommand and no built-in MML compiler,
so piping MML into `himalaya message send` ships the markup as literal text
with no attachment. This helper builds a proper multipart/mixed message with
email.mime and sends it over SMTP_SSL, producing a genuine base64 attachment.

Usage:
    python3 send_report_attachment.py <report_path> [--to TO] [--subject SUBJECT]

Defaults: --to area-buddy-manhood@duck.com
          --subject derived from the report filename (date-aware)

Gmail credentials are read from the himalaya config at
~/.config/himalaya/config.toml ([accounts.gmail] + smtp sasl plain block).
Exit code 0 on success, non-zero on failure. Prints one status line.
"""
import argparse
import os
import re
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formatdate, make_msgid, parseaddr
from pathlib import Path


def load_gmail_creds(config_path: str):
    """Parse the default gmail account's SMTP login from himalaya config.toml.

    Returns (email, smtp_host, smtp_port, username, password).
    """
    text = Path(config_path).read_text()
    email = None
    username = None
    password = None
    server = None
    # account email
    m = re.search(r'^\s*email\s*=\s*"([^"]+)"', text, re.M)
    if m:
        email = m.group(1)
    # smtp server (smtps://host:port)
    m = re.search(r'^\s*server\s*=\s*"(smtps?)://([^:/]+):?(\d+)?"', text, re.M)
    if m:
        proto, host, port = m.group(1), m.group(2), m.group(3)
        server = (host, int(port) if port else (465 if proto == "smtps" else 587), proto == "smtps")
    # sasl plain username/password (raw)
    m = re.search(r'^\s*username\s*=\s*"([^"]+)"', text, re.M)
    if m:
        username = m.group(1)
    m = re.search(r'^\s*password\.raw\s*=\s*"([^"]+)"', text, re.M)
    if m:
        password = m.group(1)
    return email, server, username, password


def default_subject(report_path: str) -> str:
    name = Path(report_path).stem
    # agentic-commerce-monitor-2026-08-17 -> 2026-08-17
    m = re.search(r'(\d{4}-\d{2}-\d{2})', name)
    date = m.group(1) if m else name
    return f"Agentic Commerce Wiki Monitor — {date}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("report_path")
    ap.add_argument("--to", default="area-buddy-manhood@duck.com")
    ap.add_argument("--subject", default=None)
    ap.add_argument("--config", default=os.path.expanduser("~/.config/himalaya/config.toml"))
    args = ap.parse_args()

    report = Path(args.report_path)
    if not report.exists():
        print(f"ERROR: report not found: {report}", file=sys.stderr)
        return 2
    data = report.read_bytes()
    if not data:
        print(f"ERROR: report is empty: {report}", file=sys.stderr)
        return 2

    email, server, username, password = load_gmail_creds(args.config)
    if not (email and server and username and password):
        print("ERROR: could not parse Gmail creds from himalaya config", file=sys.stderr)
        return 3

    host, port, use_tls = server
    subject = args.subject or default_subject(str(report))
    to_addr = parseaddr(args.to)[1] or args.to

    msg = MIMEMultipart("mixed")
    msg["From"] = email
    msg["To"] = args.to
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="gmail.com")

    msg.attach(MIMEText(
        f"Agentic Commerce Wiki Monitor report attached: {report.name}\n"
        "(Full report, Markdown.)",
        "plain", "utf-8"))

    att = MIMEApplication(data, _subtype="markdown")
    att.add_header("Content-Disposition", "attachment", filename=report.name)
    msg.attach(att)

    if use_tls:
        with smtplib.SMTP_SSL(host, port, timeout=60) as s:
            s.login(username, password)
            s.sendmail(username, [to_addr], msg.as_string())
    else:
        with smtplib.SMTP(host, port, timeout=60) as s:
            s.starttls()
            s.login(username, password)
            s.sendmail(username, [to_addr], msg.as_string())

    print(f"OK: sent {report.name} ({len(data)} bytes) to {to_addr} via {host}:{port}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
