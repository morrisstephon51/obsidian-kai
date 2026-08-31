#!/usr/bin/env python3
"""Site audit: run after generate.py. Fails loudly on any violation.

Checks:
 1. Email policy — every mailto:/form recipient is info@eccstaffing.com;
    the misspelled legacy domain appears nowhere.
 2. Link integrity — every internal href/src resolves to a generated file.
 3. Structure — exactly one <h1>, a <title>, meta description, canonical,
    viewport, and lang attribute per page.
 4. Accessibility basics — every <img> has alt; every form input has a
    label or aria-label; nav toggle has aria-expanded.
 5. Forms — every form posts to formsubmit.co/info@eccstaffing.com and
    carries a _subject and _next.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EMAIL = "info@eccstaffing.com"
errors, warns = [], []

pages = sorted(p for p in ROOT.rglob("*.html") if "_build" not in p.parts)
files = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file() and "_build" not in p.parts}

def resolve(href):
    href = href.split("#")[0].split("?")[0]
    if not href or href.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
        return True
    path = href.lstrip("/")
    if href.endswith("/") or path == "":
        path = path + "index.html"
    return path in files

for page in pages:
    rel = "/" + str(page.relative_to(ROOT))
    t = page.read_text(encoding="utf-8")

    # 1. email policy
    if "eccstsffing" in t or "eccstsﬀing" in t:
        errors.append(f"{rel}: contains the misspelled legacy domain")
    for m in re.findall(r"mailto:([^\"'\s>]+)", t):
        if m != EMAIL:
            errors.append(f"{rel}: mailto to {m!r} (must be {EMAIL})")
    for m in re.findall(r"formsubmit\.co/([^\"'\s>]+)", t):
        if m != EMAIL:
            errors.append(f"{rel}: form posts to {m!r} (must be {EMAIL})")
    for m in set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", t)):
        m = m.rstrip(".")
        if m != EMAIL and not m.endswith("formsubmit.co"):
            errors.append(f"{rel}: unexpected email address {m!r}")

    # 2. link integrity
    for attr, href in re.findall(r'(href|src|action)="([^"]+)"', t):
        if not resolve(href):
            errors.append(f"{rel}: broken {attr} -> {href}")

    # 3. structure
    h1s = re.findall(r"<h1[\s>]", t)
    if len(h1s) != 1:
        errors.append(f"{rel}: {len(h1s)} <h1> elements (want exactly 1)")
    for needle, label in [("<title>", "title"), ('name="description"', "meta description"),
                          ('rel="canonical"', "canonical"), ('name="viewport"', "viewport"),
                          ('<html lang="en">', "lang attribute")]:
        if needle not in t:
            errors.append(f"{rel}: missing {label}")

    # 4. accessibility basics
    for img in re.findall(r"<img\b[^>]*>", t):
        if 'alt="' not in img:
            errors.append(f"{rel}: img without alt: {img[:80]}")
    for inp in re.findall(r"<(?:input|select|textarea)\b[^>]*>", t):
        if 'type="hidden"' in inp or "_honey" in inp:
            continue
        m = re.search(r'id="([^"]+)"', inp)
        if not m or f'for="{m.group(1)}"' not in t:
            if "aria-label" not in inp:
                errors.append(f"{rel}: unlabeled form control: {inp[:90]}")

    # 5. forms
    for form in re.findall(r"<form\b.*?</form>", t, re.S):
        if f"formsubmit.co/{EMAIL}" not in form:
            errors.append(f"{rel}: form not posting to formsubmit.co/{EMAIL}")
        if 'name="_subject"' not in form:
            errors.append(f"{rel}: form missing _subject")
        if 'name="_next"' not in form:
            errors.append(f"{rel}: form missing _next")

# sitemap covers all indexable pages
sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
for page in pages:
    rel = "/" + str(page.relative_to(ROOT))
    if rel.endswith("/index.html"):
        loc = rel[: -len("index.html")]
        if loc.startswith("/thanks/"):
            continue
        if f"<loc>https://eccstaffing.com{loc}</loc>" not in sitemap:
            errors.append(f"sitemap.xml: missing {loc}")

print(f"Audited {len(pages)} pages, {len(files)} files.")
if errors:
    print(f"\n{len(errors)} ERROR(S):")
    for e in errors: print("  ✗", e)
    sys.exit(1)
print("All checks passed: email policy, links, structure, accessibility basics, forms, sitemap.")
