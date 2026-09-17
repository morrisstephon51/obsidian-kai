#!/usr/bin/env python3
"""Build website-v2 from live eccstaffing.com captures + new pages."""
import re, os, html, shutil

SCRATCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sources')
OUT = os.path.expanduser('~/kai/02-PROJECTS/ECC Staffing/website-v2')

# Form delivery target. info@eccstaffing.com's FormSubmit activation is still
# unconfirmed as of 2026-09-16 (see project memory) -- primary is temporarily
# Stefan's own already-active inbox so tonight's client demo is guaranteed to
# work; info@eccstaffing.com is CC'd so it starts receiving automatically the
# moment its own activation is clicked. Swap FORM_PRIMARY back once confirmed.
FORM_PRIMARY = 'morrisstephon51@gmail.com'
FORM_CC = 'info@eccstaffing.com'

def read(name):
    return open(f'{SCRATCH}/{name}', encoding='utf-8', errors='replace').read()

def extract_head_meta(html_src):
    title = re.search(r'<title>(.*?)</title>', html_src).group(1)
    desc = re.search(r'<meta name="description" content="([^"]*)"', html_src)
    desc = desc.group(1) if desc else ''
    return title, desc

def extract_main(html_src):
    m = re.search(r'<main[^>]*>(.*)</main>', html_src, re.S)
    return m.group(1)

FONT_LINKS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com"/>'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous"/>'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700&amp;family=Manrope:wght@400;500;600;700&amp;display=swap"/>'
)

NAV_ITEMS = [
    ('home', '/', 'Home'),
    ('clients', '/clients', 'Clients'),
    ('applicants', '/applicants', 'Applicants'),
    ('insights', '/insights', 'Insights'),
    ('about', '/about', 'About ECC'),
]

def build_head(title, desc, canonical):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<meta name="description" content="{desc}"/>
<meta name="author" content="Elite Career Compass LLC"/>
<link rel="canonical" href="https://eccstaffing.com{canonical}"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="{title}"/>
<meta property="og:description" content="{desc}"/>
<meta property="og:url" content="https://eccstaffing.com{canonical}"/>
<meta name="twitter:card" content="summary"/>
<link rel="icon" type="image/png" href="/assets/img/favicon.png"/>
<link rel="stylesheet" href="/assets/css/site.css"/>
{FONT_LINKS}
</head>
<body><div class="min-h-screen bg-background">'''

def build_header(active):
    logo_cls = 'flex items-center gap-2.5'
    logo_extra = ''
    if active == 'home':
        logo_cls += ' active'
        logo_extra = ' data-status="active" aria-current="page"'
    links = []
    for key, href, label in NAV_ITEMS:
        base = 'text-sm font-medium text-charcoal transition-colors hover:text-navy'
        if key == active:
            cls = base + ' text-navy after:block after:h-px after:bg-brass'
            extra = ' data-status="active" aria-current="page"'
        else:
            cls = base
            extra = ''
        links.append(f'<a href="{href}" class="{cls}"{extra}>{label}</a>')
    nav = ''.join(links)
    return (
        '<header class="sticky top-0 z-50 border-b border-border/60 bg-background/90 backdrop-blur">'
        '<div class="mx-auto flex max-w-6xl items-center justify-between gap-4 px-5 py-4">'
        f'<a class="{logo_cls}" href="/"{logo_extra}>'
        '<img src="/assets/img/logo.png" alt="Elite Career Compass LLC logo" width="944" height="1160" class="h-11 w-auto"/>'
        '<span class="leading-tight"><span class="block font-display text-sm font-semibold tracking-tight text-navy">Elite Career Compass</span>'
        '<span class="block text-[11px] uppercase tracking-[0.18em] text-muted-foreground">Staffing &amp; Recruiting</span></span></a>'
        f'<nav id="primary-nav" class="hidden items-center gap-7 md:flex">{nav}'
        '<a href="/clients#contact" class="rounded-md bg-navy px-4 py-2 text-sm font-semibold text-navy-foreground transition-opacity hover:opacity-90">Request Talent</a></nav>'
        '<button type="button" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="mobile-nav" class="md:hidden rounded-md border border-border p-2 text-navy">'
        '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-5" aria-hidden="true"><path d="M4 5h16"></path><path d="M4 12h16"></path><path d="M4 19h16"></path></svg>'
        '</button></div>'
        '<nav id="mobile-nav" hidden class="border-t border-border/60 bg-background px-5 py-4 md:hidden">'
        '<div class="flex flex-col gap-4">' + ''.join(
            f'<a href="{href}" class="text-sm font-medium text-charcoal hover:text-navy">{label}</a>' for _, href, label in NAV_ITEMS
        ) + '<a href="/clients#contact" class="rounded-md bg-navy px-4 py-2 text-center text-sm font-semibold text-navy-foreground">Request Talent</a>'
        '</div></nav>'
        '</header>'
    )

FOOTER_EXTRA_LINKS = [
    ('/services', 'Our Services'),
    ('/industries', 'Industries We Staff'),
    ('/results', 'Client Results'),
    ('/contact', 'Contact Us'),
    ('/faq', 'FAQ'),
]

def build_footer():
    extra = ''.join(f'<li><a href="{h}" class="hover:text-brass">{t}</a></li>' for h, t in FOOTER_EXTRA_LINKS)
    return f'''<footer class="bg-navy text-navy-foreground"><div class="mx-auto grid max-w-6xl gap-10 px-5 py-14 md:grid-cols-3"><div><div class="flex items-center gap-3"><span class="inline-flex items-center justify-center rounded-md bg-navy-foreground p-2"><img src="/assets/img/logo.png" alt="Elite Career Compass LLC logo" width="944" height="1160" loading="lazy" class="h-12 w-auto"/></span><span class="font-display text-base font-semibold text-navy-foreground">Elite Career Compass LLC</span></div><p class="mt-4 max-w-xs text-sm text-navy-foreground/70">Guiding talent. Empowering employers. A people-first staffing and recruiting partner built on direction, knowledge, and trust.</p></div><div><h4 class="text-sm font-semibold uppercase tracking-[0.16em] text-navy-foreground">Navigate</h4><ul class="mt-4 space-y-2.5 text-sm text-navy-foreground/75"><li><a href="/clients" class="hover:text-brass">For Clients</a></li><li><a href="/applicants" class="hover:text-brass">For Applicants</a></li><li><a href="/insights" class="hover:text-brass">Insights</a></li><li><a href="/about" class="hover:text-brass">About us</a></li>{extra}</ul></div><div><h4 class="text-sm font-semibold uppercase tracking-[0.16em] text-navy-foreground">Contact</h4><ul class="mt-4 space-y-2.5 text-sm text-navy-foreground/75"><li class="flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-brass" aria-hidden="true"><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"></path><rect x="2" y="4" width="20" height="16" rx="2"></rect></svg> <a href="mailto:info@eccstaffing.com" class="hover:text-brass">info@eccstaffing.com</a></li><li class="flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-brass" aria-hidden="true"><path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path></svg> <a href="tel:+17374233422" class="hover:text-brass">(737) 423-3422</a></li><li class="flex items-center gap-2"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4 text-brass" aria-hidden="true"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle></svg> Serving clients nationwide</li></ul></div></div><div class="border-t border-navy-foreground/10 px-5 py-5 text-center text-xs text-navy-foreground/60">&copy; 2026 Elite Career Compass LLC. All rights reserved. &middot; <a href="/privacy" class="hover:text-brass">Privacy</a> &middot; <a href="/terms" class="hover:text-brass">Terms</a> &middot; <a href="/accessibility" class="hover:text-brass">Accessibility</a></div></footer>'''

TAIL = '<script src="/assets/js/site.js"></script></div></body></html>'

def assemble(title, desc, canonical, active, main_html):
    return build_head(title, desc, canonical) + build_header(active) + f'<main>{main_html}</main>' + build_footer() + TAIL

def fix_email(s):
    return s.replace('info@eccstsffing.com', 'info@eccstaffing.com')

def fix_asset_paths(s):
    s = re.sub(r'/assets/ecc-logo-[A-Za-z0-9]+\.png', '/assets/img/logo.png', s)
    s = re.sub(r'/assets/hero-team-[A-Za-z0-9]+\.jpg', '/assets/img/hero-team.jpg', s)
    return s

def write_page(rel_path, content):
    path = os.path.join(OUT, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('wrote', rel_path, len(content), 'bytes')

# ---------- 1. Kept hub pages ----------
KEPT_HUBS = [
    ('live-home.html', 'index.html', 'home', '/'),
    ('live-clients.html', 'clients/index.html', 'clients', '/clients'),
    ('live-applicants.html', 'applicants/index.html', 'applicants', '/applicants'),
    ('live-insights.html', 'insights/index.html', 'insights', '/insights'),
    ('live-about.html', 'about/index.html', 'about', '/about'),
]

for src, dest, active, canonical in KEPT_HUBS:
    raw = read(src)
    title, desc = extract_head_meta(raw)
    main = extract_main(raw)
    main = fix_email(main)
    main = fix_asset_paths(main)
    if active == 'clients':
        # Wire the existing Request Talent form to actually deliver mail.
        assert '<form class="mt-8 grid gap-4">' in main, 'clients form markup changed unexpectedly'
        # TEMPORARY (2026-09-16, ahead of tonight's client meeting): info@eccstaffing.com
        # has not yet clicked its FormSubmit activation link, so it cannot be confirmed
        # working before the meeting. Primary delivery is temporarily Stefan's own,
        # already-active inbox so the live demo is guaranteed to work; info@eccstaffing.com
        # is CC'd so it starts receiving automatically the moment that mailbox activates
        # too, with no further code change needed. Swap FORM_PRIMARY back to
        # info@eccstaffing.com (and drop _cc) once that mailbox is confirmed. See
        # project_ecc_staffing_v2_rebuild.md.
        hidden = (
            '<input type="hidden" name="_subject" value="[Talent Request] New request from eccstaffing.com"/>'
            '<input type="hidden" name="_next" value="https://eccstaffing.com/thanks/talent/"/>'
            '<input type="hidden" name="_template" value="table"/>'
            '<input type="hidden" name="_captcha" value="false"/>'
            '<input type="hidden" name="_honey" style="display:none"/>'
            '<input type="hidden" class="js-form-url" name="_url" value="https://eccstaffing.com/clients#contact"/>'
            f'<input type="hidden" name="_cc" value="{FORM_CC}"/>'
        )
        main = main.replace(
            '<form class="mt-8 grid gap-4">',
            f'<form class="mt-8 grid gap-4" action="https://formsubmit.co/{FORM_PRIMARY}" method="POST">{hidden}',
        )
        main = main.replace(
            '<button type="submit" class="justify-self-start rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground transition-opacity hover:opacity-90 disabled:opacity-60">Request talent</button>',
            '<button type="submit" class="justify-self-start rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground transition-opacity hover:opacity-90 disabled:opacity-60">Request talent</button>'
            '<p class="mt-3 text-xs text-muted-foreground">Prefer not to use the form? Call <a href="tel:+17374233422" class="underline hover:text-navy">(737) 423-3422</a> or email <a href="mailto:info@eccstaffing.com" class="underline hover:text-navy">info@eccstaffing.com</a> directly.</p>',
        )
    page = assemble(title, desc, canonical, active, main)
    write_page(dest, page)

# ---------- 2. Kept insight articles ----------
ARTICLE_SLUGS = [
    '2026-candidate-market-speed-clarity',
    '90-day-window-turnover',
    'benchmarking-pay-remote-definitions',
    'contract-to-hire-vs-direct-search',
    'night-shift-staffing-without-burnout',
    'structured-interviews-without-bureaucracy',
    'what-hiring-managers-read-on-your-resume',
]
for slug in ARTICLE_SLUGS:
    raw = open(f'{SCRATCH}/articles/{slug}.html', encoding='utf-8', errors='replace').read()
    title, desc = extract_head_meta(raw)
    main = extract_main(raw)
    main = fix_email(main)
    main = fix_asset_paths(main)
    page = assemble(title, desc, f'/insights/{slug}', 'insights', main)
    write_page(f'insights/{slug}/index.html', page)

print('Phase 1 (kept pages) complete.')
