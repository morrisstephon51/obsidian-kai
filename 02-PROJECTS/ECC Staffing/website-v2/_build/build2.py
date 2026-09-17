#!/usr/bin/env python3
"""Phase 2: author the 5 new pages + utility pages + sitemap/robots."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import assemble, write_page, OUT, build_head, build_header, build_footer, TAIL, FORM_PRIMARY, FORM_CC

COMPASS = ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
           'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-compass size-3.5 text-brass" aria-hidden="true">'
           '<circle cx="12" cy="12" r="10"></circle><path d="m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z"></path></svg>')

COMPASS_NAVY = COMPASS.replace('text-brass', 'text-navy').replace('size-3.5', 'size-5')

def hero(eyebrow, h1, sub):
    return (f'<section class="bg-navy text-navy-foreground"><div class="mx-auto max-w-6xl px-5 py-16 md:py-20">'
            f'<p class="flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-muted-foreground">{COMPASS}'
            f'<span class="text-navy-foreground/70">{eyebrow}</span></p>'
            f'<h1 class="mt-5 max-w-2xl text-4xl font-semibold text-navy-foreground md:text-5xl">{h1}</h1>'
            f'<p class="mt-5 max-w-xl text-sm leading-relaxed text-navy-foreground/75">{sub}</p></div></section>')

def eyebrow_light(label):
    return (f'<p class="flex items-center gap-2 text-xs font-semibold uppercase tracking-[0.22em] text-muted-foreground">{COMPASS}{label}</p>')

def divider():
    return ('<div class="mx-auto flex max-w-6xl items-center gap-4 px-5 py-10"><span class="h-px flex-1 bg-border"></span>'
            f'{COMPASS_NAVY}<span class="h-px flex-1 bg-border"></span></div>')

def closing_cta(heading, sub, btn_label, btn_href):
    return (f'''<section class="bg-charcoal"><div class="mx-auto flex max-w-6xl flex-col items-start gap-6 px-5 py-14 md:flex-row md:items-center md:justify-between"><div class="flex items-start gap-4"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mt-1 size-6 text-brass" aria-hidden="true"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><path d="M16 3.128a4 4 0 0 1 0 7.744"></path><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><circle cx="9" cy="7" r="4"></circle></svg><div><h2 class="text-2xl font-semibold text-charcoal-foreground">{heading}</h2><p class="mt-2 text-sm text-charcoal-foreground/75">{sub}</p></div></div><a href="{btn_href}" class="rounded-md bg-brass px-6 py-3 text-sm font-semibold text-navy hover:opacity-90">{btn_label}</a></div></section>''')

def card(title, body):
    return f'<article class="rounded-lg border border-border bg-card p-7"><h2 class="text-lg font-semibold">{title}</h2><p class="mt-2 text-sm leading-relaxed text-muted-foreground">{body}</p></article>'

def stat(value, label):
    return f'<div class="rounded-lg border border-border bg-card p-6"><dt class="font-display text-2xl font-semibold text-navy">{value}</dt><dd class="mt-1.5 text-xs leading-relaxed text-muted-foreground">{label}</dd></div>'

# ---------------------------------------------------------------
# 1. SERVICES
# ---------------------------------------------------------------
services_main = hero(
    'For Clients',
    'Every engagement model, explained plainly',
    'From a two-week coverage gap to a confidential executive search, here is how each of our four service lines works and how to tell which one fits.',
)
services_sections = ''
svc_blocks = [
    ('Contract Staffing', 'For surges, leaves, and project ramps',
     'We staff a role on our payroll for a defined stretch of time &mdash; a maternity leave, a seasonal peak, a project with a start and end date. You get coverage without adding headcount; the worker gets a real paycheck and a recruiter checking in.',
     ['Fastest path to a filled seat &mdash; most slates land inside 48 hours', 'No conversion fee if the assignment simply ends on schedule', 'We handle payroll, taxes, and workers&#x27; comp for the duration']),
    ('Contract-to-Hire', 'Evaluate fit on the job before you commit',
     'The person works the role for an agreed trial period, still on our payroll, while your team sees the actual day-to-day fit. If it works, you convert them to your headcount. If it does not, there is no severance conversation to have.',
     ['Try before you buy &mdash; on real work, not a panel interview', 'Clear, pre-agreed conversion terms with no surprise fees', 'Most common path for roles where culture fit matters as much as skill']),
    ('Direct Placement', 'Confidential, fully-vetted searches for key roles',
     'For roles that go straight onto your headcount &mdash; leadership hires, specialized or credentialed positions, or searches you would rather not run publicly. We manage the full cycle: sourcing, screening, reference checks, and offer support.',
     ['Every direct placement carries our replacement guarantee', 'Confidential search option when a role cannot be posted openly', 'One dedicated recruiter owns the search start to finish']),
    ('Workforce Consulting', 'Compensation benchmarking and retention strategy',
     'When the question is not "who do I hire" but "how do I stop losing people," we bring the market data: live compensation benchmarks for your role and region, and a look at where your onboarding or scheduling is quietly costing you retention.',
     ['Benchmarking pulled from active searches, not a stale survey', 'Retention read-out tied to our 92% placement-retention standard', 'Delivered as a working session, not a slide deck you shelve']),
]
for title, tag, body, bullets in svc_blocks:
    bullets_html = ''.join(f'<li class="rounded-lg border-l-2 border-brass bg-secondary px-5 py-3 text-sm text-charcoal">{b}</li>' for b in bullets)
    services_sections += f'''<section class="mx-auto max-w-6xl px-5 py-12"><p class="text-xs font-semibold uppercase tracking-[0.14em] text-brass">{tag}</p><h2 class="mt-2 text-2xl font-semibold md:text-3xl">{title}</h2><p class="mt-4 max-w-3xl text-sm leading-relaxed text-muted-foreground">{body}</p><ul class="mt-6 grid gap-3 md:grid-cols-3">{bullets_html}</ul></section>'''

services_main += services_sections + divider() + closing_cta(
    "Not sure which fits?", "Tell us the role and the timeline &mdash; we will recommend the right engagement model on the call.",
    "Request Talent", "/clients#contact",
)
write_page('services/index.html', assemble(
    'Staffing Solutions Explained | Elite Career Compass',
    'Contract staffing, contract-to-hire, direct placement, and workforce consulting: how each ECC engagement model works and who it is for.',
    '/services', 'clients', services_main,
))

# ---------------------------------------------------------------
# 2. INDUSTRIES
# ---------------------------------------------------------------
industries_main = hero(
    'For Clients',
    'We speak your industry&#x27;s language',
    'Vertical experience changes what "qualified" means. Here is what our screening looks for in each of the six industries we staff.',
)
ind_blocks = [
    ('Healthcare', 'Credentialing, licensure verification, and shift reliability come first &mdash; we screen for active licenses, required certifications, and a track record of showing up for the shift, not just a resume that reads well.'),
    ('Finance & Accounting', 'Close-the-books urgency and accuracy under deadline. We screen for the specific system experience (ERP, reconciliation tools) and the audit trail habits that keep month-end from becoming a fire drill.'),
    ('Technology', 'Stack-specific screening, not keyword matching &mdash; a technical conversation before a candidate ever reaches your interview loop, so the people you see can actually do the work described in the req.'),
    ('Light Industrial', 'Shift reliability, safety record, and physical-requirement fit. We staff for attendance and pace as much as for skill, because a no-show on a production line costs more than a slow ramp.'),
    ('Administrative', 'Software fluency, judgment, and discretion &mdash; the traits that separate someone who keeps an office running from someone who just answers the phone.'),
    ('Seasonal & Events', 'Fast ramps, hard deadlines, and short assignments. We keep a warm bench for peak seasons so a surge does not mean starting your search from zero.'),
]
ind_html = ''
for title, body in ind_blocks:
    ind_html += card(title, body)
industries_main += f'<section class="mx-auto max-w-6xl px-5 py-16">{eyebrow_light("Industries served")}<div class="mt-7 grid gap-5 md:grid-cols-2 lg:grid-cols-3">{ind_html}</div></section>'
industries_main += divider() + closing_cta(
    "Hiring in one of these fields?", "Tell us the role &mdash; we will match it to a recruiter who already knows the vertical.",
    "Request Talent", "/clients#contact",
)
write_page('industries/index.html', assemble(
    'Industries We Staff | Elite Career Compass',
    'Healthcare, Finance & Accounting, Technology, Light Industrial, Administrative, and Seasonal & Events &mdash; how ECC screens for each.',
    '/industries', 'clients', industries_main,
))

# ---------------------------------------------------------------
# 3. RESULTS
# ---------------------------------------------------------------
results_main = hero(
    'Proof',
    'Where clarity shows up in the numbers',
    'We would rather show you the standard we hold ourselves to than tell you we are great. Here is what we track, and what it means for your search.',
)
stats_html = ''.join([
    stat('48 hrs', 'Average time to first qualified slate'),
    stat('92%', 'Placement retention past one year'),
    stat('5', 'Core industries served'),
    stat('1:1', 'Dedicated recruiter per search'),
])
results_main += f'''<section class="mx-auto max-w-6xl px-5 py-16">{eyebrow_light("By the numbers")}<h2 class="mt-4 text-3xl font-semibold md:text-4xl">The standard every search is held to</h2><dl class="mt-8 grid grid-cols-2 gap-4 md:grid-cols-4">{stats_html}</dl></section>'''
results_main += divider()
method_cards = ''.join([
    card('What counts as a "qualified" slate', 'A candidate who has cleared reference checks, a skills conversation, and a motivation check &mdash; not just someone who matches keywords on a resume.'),
    card('How we define retention', 'Still in the role, by client report, twelve months after placement. Contract assignments that end on their pre-agreed date count as a completed placement, not a loss.'),
    card('The replacement guarantee', 'If a direct placement does not work out inside the guarantee window, we run the search again at no additional placement fee.'),
])
results_main += f'<section class="surface-soft"><div class="mx-auto max-w-6xl px-5 py-16">{eyebrow_light("How we measure it")}<div class="mt-7 grid gap-5 md:grid-cols-3">{method_cards}</div></div></section>'
results_main += f'''<section class="mx-auto max-w-3xl px-5 py-16 text-center">{eyebrow_light("Client references")}<h2 class="mt-4 text-2xl font-semibold md:text-3xl">Ask us for a direct reference</h2><p class="mt-4 text-sm leading-relaxed text-muted-foreground">We are still building out written case studies and are not going to publish quotes that are not real. What we will do on a call: connect you directly with a current client in your industry so you can ask them yourself.</p></section>'''
results_main += divider() + closing_cta(
    "Want to see the standard in your own search?", "Start with a conversation about the role &mdash; no obligation.",
    "Request Talent", "/clients#contact",
)
write_page('results/index.html', assemble(
    'Client Results | Elite Career Compass',
    'The numbers behind every ECC search: time to slate, placement retention, and how we measure success.',
    '/results', 'about', results_main,
))

# ---------------------------------------------------------------
# 4. CONTACT
# ---------------------------------------------------------------
contact_form = f'''<form class="mt-8 grid gap-4" action="https://formsubmit.co/{FORM_PRIMARY}" method="POST">
<input type="hidden" name="_subject" value="[Contact] New message from eccstaffing.com"/>
<input type="hidden" name="_next" value="https://eccstaffing.com/thanks/contact/"/>
<input type="hidden" name="_template" value="table"/>
<input type="hidden" name="_captcha" value="false"/>
<input type="hidden" name="_honey" style="display:none"/>
<input type="hidden" class="js-form-url" name="_url" value="https://eccstaffing.com/contact"/>
<input type="hidden" name="_cc" value="{FORM_CC}"/>
<div class="grid gap-4 sm:grid-cols-2"><label class="grid gap-2"><span class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Full name</span><input type="text" required placeholder="Jordan Avery" class="rounded-md border border-input bg-card px-4 py-3 text-sm outline-none focus:border-navy" name="name"/></label><label class="grid gap-2"><span class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Email</span><input type="email" required placeholder="you@company.com" class="rounded-md border border-input bg-card px-4 py-3 text-sm outline-none focus:border-navy" name="email"/></label></div>
<label class="grid gap-2"><span class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Subject</span><input type="text" required placeholder="What is this about?" class="rounded-md border border-input bg-card px-4 py-3 text-sm outline-none focus:border-navy" name="subject"/></label>
<label class="grid gap-2"><span class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Message</span><textarea name="message" required rows="5" placeholder="How can we help?" class="rounded-md border border-input bg-card px-4 py-3 text-sm outline-none focus:border-navy"></textarea></label>
<button type="submit" class="justify-self-start rounded-md bg-navy px-6 py-3 text-sm font-semibold text-navy-foreground transition-opacity hover:opacity-90">Send message</button>
</form>'''

contact_main = hero('Get in touch', 'Reach the ECC team directly', 'Hiring or applying? Use the links below for the fastest response. Everything else, send us a message.')
contact_main += f'''<section class="mx-auto max-w-6xl px-5 py-12"><div class="grid gap-4 md:grid-cols-2"><div class="rounded-lg border border-border bg-card p-7"><h2 class="text-lg font-semibold">Hiring? Request talent</h2><p class="mt-2 text-sm leading-relaxed text-muted-foreground">Tell us who you need &mdash; most clients get a first qualified slate inside 48 hours.</p><a href="/clients#contact" class="mt-4 inline-flex items-center gap-2 rounded-md bg-navy px-5 py-2.5 text-sm font-semibold text-navy-foreground hover:opacity-90">Request Talent</a></div><div class="rounded-lg border border-border bg-card p-7"><h2 class="text-lg font-semibold">Looking for a role? Apply</h2><p class="mt-2 text-sm leading-relaxed text-muted-foreground">Submit your application through our secure portal &mdash; it is always free to candidates.</p><a href="https://my.workforce.com/ats/apply/general/ad59138b-714d-4bc0-b78b-18a167f6eb27" class="mt-4 inline-flex items-center gap-2 rounded-md border border-navy px-5 py-2.5 text-sm font-semibold text-navy hover:bg-navy hover:text-navy-foreground">Apply Now</a></div></div></section>'''
contact_main += f'<section class="surface-soft"><div class="mx-auto max-w-3xl px-5 py-16">{eyebrow_light("Everything else")}<h2 class="mt-4 text-3xl font-semibold">Send us a message</h2>{contact_form}</div></section>'
contact_main += f'''<section class="mx-auto max-w-6xl px-5 py-16"><dl class="grid gap-4 sm:grid-cols-3"><div class="rounded-lg border border-border bg-card p-6"><dt class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Email</dt><dd class="mt-2 text-sm text-charcoal"><a href="mailto:info@eccstaffing.com" class="hover:text-navy">info@eccstaffing.com</a></dd></div><div class="rounded-lg border border-border bg-card p-6"><dt class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Phone</dt><dd class="mt-2 text-sm text-charcoal"><a href="tel:+17374233422" class="hover:text-navy">(737) 423-3422</a></dd></div><div class="rounded-lg border border-border bg-card p-6"><dt class="text-xs font-semibold uppercase tracking-[0.14em] text-muted-foreground">Service area</dt><dd class="mt-2 text-sm text-charcoal">Serving clients nationwide</dd></div></dl></section>'''
write_page('contact/index.html', assemble(
    'Contact Elite Career Compass',
    'Reach the ECC team: request talent, apply for a role, or send a general message to info@eccstaffing.com.',
    '/contact', '', contact_main,
))

# ---------------------------------------------------------------
# 5. FAQ
# ---------------------------------------------------------------
def qa(q, a):
    return f'''<details class="group rounded-lg border border-border bg-card p-6"><summary class="cursor-pointer list-none text-sm font-semibold text-charcoal marker:content-none">{q}</summary><p class="mt-3 text-sm leading-relaxed text-muted-foreground">{a}</p></details>'''

client_faqs = [
    ("Aren&#x27;t staffing agencies expensive?", "Our fee replaces the cost of your team&#x27;s time screening resumes that go nowhere. Pricing is transparent and quoted before a search starts &mdash; no surprise conversion fees."),
    ("Will you just send me warm bodies?", "No. Every slate is built from real screening &mdash; skills, references, and motivation &mdash; so your interview time goes to people who can actually do the work."),
    ("Do you understand my industry?", "We staff five core verticals and screen for what actually matters in each &mdash; see the specifics on our <a href=\"/industries\" class=\"underline hover:text-navy\">Industries page</a>."),
    ("Will I get locked into a long contract?", "No. Contract staffing ends on the date you agree to. Contract-to-hire converts on pre-agreed terms. Direct placement is a one-time search fee with a replacement guarantee."),
    ("How fast can you actually deliver candidates?", "48 hours to a first qualified slate is our average, not our best case. Complex or highly specialized searches take longer &mdash; we will tell you upfront if yours will."),
]
applicant_faqs = [
    ("Does it cost anything to work with ECC?", "No. Our service is always free to candidates &mdash; employers pay us, never you."),
    ("Is this just temp work?", "Some roles are contract, some are contract-to-hire, and some are direct placement from day one. We will tell you which a role is before you apply, not after."),
    ("Will I actually hear back?", "Every applicant gets a response &mdash; no silent rejections. If you apply and it has been more than a few business days, that is not how we are supposed to operate; email <a href=\"mailto:info@eccstaffing.com\" class=\"underline hover:text-navy\">info@eccstaffing.com</a>."),
    ("Is ECC a legitimate agency?", "We are a licensed staffing and recruiting firm. You can verify us, read about our founder and values on the <a href=\"/about\" class=\"underline hover:text-navy\">About page</a>, or ask to speak with a current client for a reference."),
    ("What happens after I apply?", "Apply, then a 20-minute screening call to map skills, schedule, and goals, then we match you to employers that actually fit &mdash; with context, not a resume dump."),
]
faq_main = hero('FAQ', 'Answers before you reach out', 'The questions we hear most, from both sides of the table.')
c_html = ''.join(qa(q, a) for q, a in client_faqs)
a_html = ''.join(qa(q, a) for q, a in applicant_faqs)
faq_main += f'<section class="mx-auto max-w-4xl px-5 py-16">{eyebrow_light("For clients")}<h2 class="mt-4 text-2xl font-semibold md:text-3xl">Hiring with ECC</h2><div class="mt-7 grid gap-4">{c_html}</div></section>'
faq_main += f'<section class="surface-soft"><div class="mx-auto max-w-4xl px-5 py-16">{eyebrow_light("For applicants")}<h2 class="mt-4 text-2xl font-semibold md:text-3xl">Applying through ECC</h2><div class="mt-7 grid gap-4">{a_html}</div></div></section>'
faq_main += divider()
faq_main += f'''<section class="mx-auto max-w-3xl px-5 pb-16 text-center"><p class="text-sm text-muted-foreground">Still have a question? <a href="/contact" class="underline hover:text-navy">Contact us</a> and we will get back to you.</p></section>'''
write_page('faq/index.html', assemble(
    'Frequently Asked Questions | Elite Career Compass',
    'Common questions from clients hiring through ECC and candidates applying &mdash; pricing, timelines, legitimacy, and what happens next.',
    '/faq', '', faq_main,
))

print('Phase 2 (5 new pages) complete.')
