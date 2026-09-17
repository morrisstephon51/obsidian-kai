#!/usr/bin/env python3
"""Phase 3: utility pages (privacy/terms/accessibility/404/thank-you), sitemap.xml, robots.txt."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build2 import hero, eyebrow_light, divider, closing_cta, OUT
from build import assemble, write_page, build_head, build_header, build_footer, TAIL

def simple_page(eyebrow, h1, body_html):
    main = hero(eyebrow, h1, '')
    main += f'<section class="mx-auto max-w-3xl px-5 py-16 text-sm leading-relaxed text-muted-foreground">{body_html}</section>'
    return main

# ---------------- Privacy ----------------
privacy_body = '''<p class="mb-4">Elite Career Compass LLC (&ldquo;ECC,&rdquo; &ldquo;we&rdquo;) collects the information you submit through this site &mdash; such as your name, contact details, and resume &mdash; solely to provide staffing and recruiting services: responding to your inquiry, matching candidates with roles, and communicating with you about them.</p>
<p class="mb-4">We do not sell your personal information. We share it only as needed to provide our services (for example, presenting a candidate&rsquo;s profile to a hiring client with the candidate&rsquo;s knowledge) or as required by law.</p>
<p class="mb-4">Form submissions from this site are delivered to <a href="mailto:info@eccstaffing.com" class="underline hover:text-navy">info@eccstaffing.com</a>. To ask what information we hold about you, or to request correction or deletion, email us at that address.</p>
<p class="rounded-lg border-l-2 border-brass bg-secondary px-5 py-4 text-charcoal">This page is a starting draft for launch. Have it reviewed by counsel before relying on it.</p>'''
write_page('privacy/index.html', assemble('Privacy Policy | Elite Career Compass', 'How Elite Career Compass collects and uses information submitted through this site.', '/privacy', '', simple_page('Legal', 'Privacy Policy', privacy_body)))

# ---------------- Terms ----------------
terms_body = '''<p class="mb-4">By using eccstaffing.com you agree to use the site lawfully and to submit only information that is accurate and yours to share.</p>
<p class="mb-4">Content on this site is provided for general information about our services and is not an offer of employment or a guarantee of placement.</p>
<p class="mb-4">All site content and branding are the property of Elite Career Compass LLC and may not be reused without permission.</p>
<p class="mb-4">Questions about these terms: <a href="mailto:info@eccstaffing.com" class="underline hover:text-navy">info@eccstaffing.com</a>.</p>
<p class="rounded-lg border-l-2 border-brass bg-secondary px-5 py-4 text-charcoal">This page is a starting draft for launch. Have it reviewed by counsel before relying on it.</p>'''
write_page('terms/index.html', assemble('Terms of Use | Elite Career Compass', 'Terms governing use of the eccstaffing.com website.', '/terms', '', simple_page('Legal', 'Terms of Use', terms_body)))

# ---------------- Accessibility ----------------
access_body = '''<p class="mb-4">We want everyone to be able to use this site, including people using screen readers, keyboard navigation, or magnification. The site is built with semantic headings, labeled forms, visible focus states, and color contrast aimed at WCAG 2.1 AA.</p>
<p class="mb-4">If anything on this site is hard for you to use, tell us and we&rsquo;ll fix it: <a href="mailto:info@eccstaffing.com" class="underline hover:text-navy">info@eccstaffing.com</a> or <a href="tel:+17374233422" class="underline hover:text-navy">(737) 423-3422</a>.</p>
<p>If a form is a barrier, you can complete any request &mdash; hiring, applying, or general &mdash; entirely by phone or email.</p>'''
write_page('accessibility/index.html', assemble('Accessibility | Elite Career Compass', 'ECC’s commitment to an accessible website, and how to reach us if something is a barrier.', '/accessibility', '', simple_page('Accessibility', 'Accessibility', access_body)))

# ---------------- 404 ----------------
main_404 = hero('Off the map', 'That page doesn&#x27;t exist', 'Your bearing is easy to recover from here.')
main_404 += f'''<section class="mx-auto max-w-6xl px-5 py-16"><div class="flex flex-wrap gap-3"><a href="/clients#contact" class="rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground hover:opacity-90">Request Talent</a><a href="https://my.workforce.com/ats/apply/general/ad59138b-714d-4bc0-b78b-18a167f6eb27" class="rounded-md border border-navy px-6 py-3 text-sm font-semibold text-navy hover:bg-navy hover:text-navy-foreground">Apply Now</a><a href="/" class="rounded-md border border-border px-6 py-3 text-sm font-semibold text-charcoal hover:border-navy hover:text-navy">Back to home</a></div></section>'''
page_404 = build_head('Page Not Found | Elite Career Compass', 'The page you were looking for does not exist.', '/404') + build_header('') + f'<main>{main_404}</main>' + build_footer() + TAIL
with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(page_404)
print('wrote 404.html', len(page_404))

# ---------------- Thank-you pages ----------------
thanks_talent = hero('Message sent', 'Your request is in', 'A dedicated recruiter will respond within one business day, and your first qualified slate averages 48 hours. Need us sooner? Call (737) 423-3422.')
thanks_talent += f'''<section class="mx-auto max-w-6xl px-5 py-16"><div class="flex flex-wrap gap-3"><a href="/services" class="rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground hover:opacity-90">Explore engagement models</a><a href="/results" class="rounded-md border border-border px-6 py-3 text-sm font-semibold text-charcoal hover:border-navy hover:text-navy">See our results</a></div></section>'''
write_page('thanks/talent/index.html', assemble('Request Received | Elite Career Compass', 'Your talent request has been received.', '/thanks/talent', '', thanks_talent))

thanks_contact = hero('Message sent', 'Message received', 'We respond within one business day. If your question is about hiring or finding work, these will get you moving now.')
thanks_contact += f'''<section class="mx-auto max-w-6xl px-5 py-16"><div class="flex flex-wrap gap-3"><a href="/clients#contact" class="rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground hover:opacity-90">Request Talent</a><a href="https://my.workforce.com/ats/apply/general/ad59138b-714d-4bc0-b78b-18a167f6eb27" class="rounded-md border border-navy px-6 py-3 text-sm font-semibold text-navy hover:bg-navy hover:text-navy-foreground">Apply Now</a></div></section>'''
write_page('thanks/contact/index.html', assemble('Message Received | Elite Career Compass', 'Your message has been received.', '/thanks/contact', '', thanks_contact))

# ---------------- sitemap.xml ----------------
PAGES = [
    '/', '/clients', '/applicants', '/insights', '/about',
    '/services', '/industries', '/results', '/contact', '/faq',
    '/insights/2026-candidate-market-speed-clarity',
    '/insights/90-day-window-turnover',
    '/insights/benchmarking-pay-remote-definitions',
    '/insights/contract-to-hire-vs-direct-search',
    '/insights/night-shift-staffing-without-burnout',
    '/insights/structured-interviews-without-bureaucracy',
    '/insights/what-hiring-managers-read-on-your-resume',
]
urls = ''.join(f'<url><loc>https://eccstaffing.com{p}</loc></url>' for p in PAGES)
sitemap = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap)
print('wrote sitemap.xml with', len(PAGES), 'urls')

# ---------------- robots.txt ----------------
robots = "User-agent: *\nAllow: /\n\nSitemap: https://eccstaffing.com/sitemap.xml\n"
with open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots)
print('wrote robots.txt')

print('Phase 3 complete. Total real content pages:', len(PAGES))
