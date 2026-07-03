# CONTENT AUTOMATION MACHINE — COMPLETION + DEPLOYMENT PROMPT
### Full User Journey Audit | Autonomous & Manual Modes | GoDaddy Live Deployment

---

## YOUR MISSION

You are completing and deploying a full-stack Content Automation Machine.
The app has been scaffolded across 5 phases. Your job now is to:

1. Audit every user journey from first visit to completed action
2. Fix every broken path, dead end, missing UI state, and error
3. Ensure content creation works both AUTONOMOUSLY and MANUALLY
4. Deploy the finished app live to a custom GoDaddy domain

Do not add new features. Fix, complete, and ship what exists.

---

## STEP 1 — FULL CODEBASE AUDIT

Before writing a single line of code, read every file in the project.
Run this exact audit checklist and report what you find:

### Audit Checklist

```
READ every file in:
- app/ (all routes and pages)
- components/ (all UI components)
- lib/ (all utility and integration files)
- remotion/ (all video compositions)
- supabase/migrations/ (all SQL files)

FOR EACH FILE, check:
□ Does it compile without TypeScript errors?
□ Does it import from files that actually exist?
□ Does every function have a complete implementation (no TODO, no placeholder)?
□ Does every API route return proper success AND error responses?
□ Does every form have loading, success, and error states?
□ Does every async operation have a try/catch?
□ Does every page handle the empty state (no data yet)?
□ Does every page handle the loading state?
□ Does every page handle the error state?

REPORT FORMAT:
- File name
- Status: COMPLETE / INCOMPLETE / BROKEN
- Issue description if not complete
- Fix required
```

Do not proceed past this audit until you have read every file.

---

## STEP 2 — USER JOURNEY MAP

After the audit, map and fix every user journey.
A journey is ONLY complete when the user can finish the full action
without hitting a dead end, blank screen, unhandled error, or confusion.

---

### JOURNEY 1: NEW USER ONBOARDING

```
Start: User visits the app for the first time (never signed in)

Step 1 → Landing page loads
  REQUIRED:
  - App name and tagline visible immediately
  - "Get Started" or "Sign In" button is the primary CTA
  - No broken images, no console errors, no blank white screen
  - Works on mobile

Step 2 → User clicks "Get Started"
  REQUIRED:
  - Auth page loads with Google Sign In option
  - Email/password option also available as fallback
  - No redirect loops
  - Loading spinner while auth processes

Step 3 → User signs in successfully
  REQUIRED:
  - Redirect to /onboarding (NOT directly to dashboard)
  - If no brand vault exists → show onboarding flow
  - If brand vault exists → skip to dashboard

Step 4 → Onboarding: Brand Setup
  REQUIRED:
  - Step-by-step wizard (not one giant form)
  - Step 1: Brand name + industry + mission (required)
  - Step 2: Voice + tone sliders + content pillars
  - Step 3: Color palette (hex inputs + preview swatches)
  - Step 4: Upload logo (drag and drop, shows preview)
  - Step 5: Add 2-3 sample posts as examples
  - Progress indicator showing which step they're on
  - "Skip for now" option on optional steps
  - "Save and Continue" saves progress between steps
  - Final step: "Go to Dashboard" button

Step 5 → Dashboard loads for first time
  REQUIRED:
  - Welcome message with user's brand name
  - Quick action cards: "Create Video", "Create Flyer", "View Trends"
  - Empty calendar with "Schedule your first post" prompt
  - Empty library with "Generate your first content" prompt
  - No raw JSON, no undefined errors, no blank panels

END STATE: User has a configured brand and understands the app.
```

---

### JOURNEY 2: AUTONOMOUS CONTENT GENERATION (One-Click Mode)

```
Start: User wants the app to create content with minimum input

Step 1 → User clicks "Auto-Generate" from dashboard
  REQUIRED:
  - Modal or panel opens
  - User selects: content pillar from dropdown
  - User selects: target platform(s) — checkboxes
  - User clicks "Generate Everything"

Step 2 → AI generates all formats simultaneously
  REQUIRED:
  - Live progress panel shows each format being generated
  - Format cards appear as each one completes (streaming)
  - Each card shows: platform icon, format name, status badge
  - If any format fails → show retry button for that format only
  - User does NOT have to wait for all formats before seeing results

Step 3 → User reviews generated content
  REQUIRED:
  - All generated video scripts shown as preview cards
  - Each card shows: hook text, scene count, duration, platform
  - "Preview" button → shows Remotion player preview in modal
  - "Edit" button → opens inline text editor for any scene
  - "Approve" button → moves to render queue
  - "Reject" button → asks for feedback, regenerates that format

Step 4 → Render queue
  REQUIRED:
  - Shows all approved formats queued for rendering
  - "Render All" button starts the render pipeline
  - Real-time progress bar per video (0% → 100%)
  - When complete: thumbnail preview + download button + Drive link
  - "Add to Calendar" button for each rendered video

Step 5 → Auto-scheduling (fully autonomous path)
  REQUIRED:
  - Toggle: "Auto-schedule to calendar"
  - If ON → AI picks optimal posting times per platform and schedules
  - Scheduled slots appear on content calendar immediately
  - User gets a summary: "5 videos scheduled across 3 platforms"

END STATE: User generated, rendered, and scheduled content
without manually writing anything.
```

---

### JOURNEY 3: MANUAL CONTENT CREATION (Full Control Mode)

```
Start: User has a specific idea and wants full creative control

Step 1 → User goes to /generate (Video Studio)
  REQUIRED:
  - Clean input area — large text box front and center
  - Input accepts: typed topic, pasted URL, or drag-drop file
  - Platform selector: choose which platforms to generate for
  - Format selector: choose which video formats to generate
  - Advanced options collapsible panel:
    - Tone override (more formal / more casual slider)
    - Duration override per format
    - Music genre selector
    - Voiceover on/off toggle

Step 2 → User submits their input
  REQUIRED:
  - Button changes to loading state immediately
  - "Generating..." message with animated indicator
  - SSE stream shows which format Claude is working on in real-time
  - If Claude API errors → clear error message with retry button
  - If generation succeeds → scroll to results automatically

Step 3 → User edits before rendering
  REQUIRED:
  - Every text layer is clickable and editable inline
  - Clicking a scene in the Remotion preview highlights it
  - Scene duration is adjustable via slider
  - B-roll background is swappable (type new search term → auto-fetches)
  - Music track is replaceable (search Freesound inline)
  - Color overrides available per text layer
  - Undo/redo for all edits

Step 4 → User renders final video
  REQUIRED:
  - "Render" button clearly visible
  - Confirmation dialog: shows format, platform, duration, file size estimate
  - Render progress: real-time percentage + current step description
    ("Fetching b-roll...", "Mixing audio...", "Encoding MP4...")
  - On complete: video plays inline, download button, Drive link
  - If render fails → exact error shown + "Try Again" button

Step 5 → User creates matching flyer
  REQUIRED:
  - After video renders, prompt appears: "Create a matching flyer?"
  - One click → Canva flyer brief auto-generated from same input
  - 3 Canva template options shown as thumbnails
  - User picks one → flyer opens in Canva editor (new tab)
  - Or: "Auto-create all sizes" → generates all 6 dimensions automatically

END STATE: User has a custom video + matching flyer
with full creative control at every step.
```

---

### JOURNEY 4: FLYER CREATION ONLY

```
Start: User needs a flyer for an event or campaign

Step 1 → User goes to /flyer (Flyer Studio)
  REQUIRED:
  - Input form: event name, date, location, description, CTA
  - Or: free-form text input ("Create a flyer for our health fair")
  - Toggle: "Include QR code" + QR destination field

Step 2 → AI generates flyer brief
  REQUIRED:
  - Shows generated copy: headline, subheadline, body, CTA
  - User can edit any copy field inline before designing
  - Color palette pulled from brand vault automatically
  - "Use different colors" option to override

Step 3 → Canva template selection
  REQUIRED:
  - 3 template thumbnails shown based on brief keywords
  - "Refresh templates" button for different options
  - User clicks preferred template

Step 4 → Flyer is created in Canva
  REQUIRED:
  - Canva API creates the design with brand copy injected
  - Loading state while Canva processes
  - On complete: preview thumbnail shown in app
  - "Open in Canva" button → opens the editable design
  - "Export All Sizes" → downloads all 6 dimensions as ZIP

Step 5 → QR code (if toggled on)
  REQUIRED:
  - QR code generated inside the app (qrcode package)
  - Preview of QR shown with destination URL labeled
  - "Download QR" button → PNG download
  - QR is also embedded in the Canva flyer automatically

END STATE: User has a branded flyer in all dimensions
plus an optional QR code, without leaving the app.
```

---

### JOURNEY 5: CONTENT CALENDAR MANAGEMENT

```
Start: User wants to plan and schedule content

Step 1 → User goes to /calendar
  REQUIRED:
  - Monthly calendar view loads with all scheduled content
  - Each scheduled item shows: platform icon, content thumbnail, time
  - Color coded by platform
  - Empty days show a "+" button to add content

Step 2 → User schedules existing content
  REQUIRED:
  - Drag any approved content from library onto a calendar day
  - Or: click "+" on a day → choose from library or generate new
  - Platform selector per slot
  - Time picker for exact post time
  - Duplicate slot option

Step 3 → Bulk AI scheduling
  REQUIRED:
  - "Auto-fill Calendar" button
  - User picks: date range, content pillars, platforms
  - AI generates + schedules a full month of content
  - Preview shown before confirming
  - "Looks good, schedule it" → fills the calendar

Step 4 → Export options
  REQUIRED:
  - "Export to Google Calendar" → creates events in user's Google Cal
  - "Download as PDF" → printable calendar for stakeholders
  - "Export as CSV" → for external scheduling tools

END STATE: User has a fully populated content calendar
with content assigned to every platform and time slot.
```

---

### JOURNEY 6: TREND-TO-CONTENT (Fully Autonomous)

```
Start: User opens app in the morning and sees trend briefs

Step 1 → Dashboard shows today's trend briefs
  REQUIRED:
  - Maximum 5 trend cards visible on dashboard
  - Each card shows: topic, relevance score, decay estimate,
    suggested angle for THIS brand specifically
  - Cards sorted by relevance score descending

Step 2 → User clicks "Generate from This Trend"
  REQUIRED:
  - One click pre-fills the Video Studio with the trend context
  - Brand vault + trend brief → sent to Claude together
  - Generates full content set automatically
  - User lands on the review screen with results

Step 3 → If no trends yet (first run or cron hasn't fired)
  REQUIRED:
  - Empty state with explanation: "Trend scan runs daily at 7 AM"
  - "Scan Now" button → manually triggers the trend scan
  - Loading state while scan runs
  - Results appear without page refresh

END STATE: User went from seeing a trending topic to
having generated content in under 60 seconds.
```

---

### JOURNEY 7: PERFORMANCE TRACKING + AI REPORT

```
Start: User wants to understand what content is working

Step 1 → User goes to /analytics
  REQUIRED:
  - Overview cards: total views, total likes, best performing platform,
    top performing content piece
  - Bar chart: performance by platform
  - List: top 5 content pieces by engagement

Step 2 → User logs performance manually
  REQUIRED:
  - Each content item in library has "Log Performance" button
  - Form: views, likes, comments, shares, saves, reach
  - Save → numbers appear on the analytics dashboard immediately

Step 3 → Weekly AI Report
  REQUIRED:
  - "Generate Weekly Report" button (or auto-generates every Sunday)
  - Loading state with "AI is analyzing your performance data..."
  - Report appears as formatted text with sections:
    - What Worked This Week
    - What Didn't Work
    - Top Performing Format
    - Recommended Adjustments
    - Suggested Content for Next Week
  - "Apply Recommendations to Brand Vault" button
    → updates sample posts and voice guidance automatically

END STATE: User knows exactly what to make more of
and the AI is getting smarter about their brand each week.
```

---

### JOURNEY 8: CONTENT LIBRARY MANAGEMENT

```
Start: User wants to find, reuse, or manage past content

Step 1 → User goes to /library
  REQUIRED:
  - Grid view of all generated content with thumbnails
  - Filter bar: platform, content type, pillar, status, date range
  - Search bar: searches across all captions and scripts
  - Sort: newest, oldest, highest performing

Step 2 → User clicks a content item
  REQUIRED:
  - Modal opens with full details:
    - Video preview or flyer preview
    - All platform captions
    - Performance metrics (if logged)
    - Status badge
    - Created date

Step 3 → User remixes content
  REQUIRED:
  - "Remix This" button → pre-fills Video Studio with original content
  - User can update topic, change platforms, adjust tone
  - Generates fresh content based on the original

Step 4 → Evergreen recycling
  REQUIRED:
  - "Mark as Evergreen" toggle on any content item
  - Dropdown: recycle every 30 / 60 / 90 days
  - Evergreen items auto-appear on the calendar on their recycle date
  - Badge shows on the item: "♻️ Evergreen - recycles in X days"

END STATE: No good content ever goes to waste.
```

---

## STEP 3 — AUTONOMOUS MODE VS MANUAL MODE

The app must support BOTH modes clearly.

### Add a Global Mode Toggle to the Settings page:

```typescript
type AppMode = "autonomous" | "manual" | "hybrid"

interface ModeSettings {
  mode: AppMode
  autonomous_settings: {
    auto_approve_content: boolean        // skip approval queue
    auto_schedule_after_render: boolean  // auto-add to calendar
    auto_render_after_approve: boolean   // render without clicking
    auto_generate_on_trend: boolean      // generate when new trend found
    daily_content_count: number          // how many pieces per day
    preferred_platforms: Platform[]      // which platforms to target
  }
}
```

### Mode Behaviors:

**AUTONOMOUS MODE (set and forget)**
- Trend agent fires at 7 AM → finds relevant trends
- Auto-generates content for each trend
- Auto-approves (skips queue) if confidence score > 8
- Auto-renders all approved content
- Auto-schedules to calendar at optimal times
- User wakes up to fully scheduled, rendered content
- Dashboard shows: "12 pieces created overnight. Review here →"

**MANUAL MODE (full control)**
- Nothing happens without the user clicking
- Every step requires explicit approval
- Default mode for new users

**HYBRID MODE (recommended default)**
- Trend scan runs automatically
- Content is generated automatically from trends
- BUT: requires human approval before rendering
- Approved content auto-renders and auto-schedules
- User reviews once, everything else is handled

---

## STEP 4 — FIX ALL ERROR STATES

For every API route in the app, ensure:

```typescript
// Every route must follow this pattern:
export async function POST(request: Request) {
  try {
    // validate input
    const body = await request.json()
    if (!body.required_field) {
      return Response.json(
        { error: "required_field is required" },
        { status: 400 }
      )
    }

    // do the work
    const result = await doTheWork(body)

    return Response.json({ success: true, data: result })

  } catch (error) {
    console.error('[route-name] error:', error)
    return Response.json(
      {
        error: "Something went wrong",
        detail: error instanceof Error ? error.message : "Unknown error"
      },
      { status: 500 }
    )
  }
}
```

Every UI component that calls an API must handle:
- Loading state (spinner or skeleton)
- Success state (shows result)
- Error state (shows message + retry button)
- Empty state (shows prompt to get started)

---

## STEP 5 — LANDING PAGE

Build a proper landing page at the root URL `/` for non-authenticated users.

```
Sections:
1. Hero: App name + tagline + "Get Started Free" CTA button
2. How it works: 3 steps (Input topic → AI generates video → Schedule it)
3. Features: Video Studio, Flyer Studio, Trend Agent, Calendar, Analytics
4. Brands it supports: BigHeart Health + The Plug AI as demo examples
5. CTA: "Start Creating Content →" button → /auth/signin

Design:
- Dark background
- Brand colors from the active brand (or default purple/gold)
- Clean, modern, professional
- NOT a generic SaaS template — make it distinctive
- Animated hero with a mockup of the Video Studio UI
```

---

## STEP 6 — MOBILE RESPONSIVENESS

Every page must work on a phone screen (375px wide minimum).

Priority pages for mobile:
- Dashboard (read trends, see scheduled content)
- Approval queue (approve/reject on the go)
- Content library (browse past content)
- Analytics (check performance)

Video Studio and Flyer Studio are desktop-primary but must not break on mobile.
Show a banner on mobile: "For the best creation experience, use a desktop browser."

---

## STEP 7 — FINAL QA CHECKLIST

Before deployment, verify every item below passes:

```
AUTHENTICATION
□ Google Sign In works and redirects correctly
□ Email sign up works
□ Sign out works and clears session
□ Protected routes redirect to /auth/signin if not logged in
□ Auth callback URL is configured in Supabase

BRAND VAULT
□ Create brand works and saves to Supabase
□ Edit brand works and updates correctly
□ Logo upload works (saves to Supabase Storage)
□ Brand colors update the app's accent color in real-time
□ Multiple brands can be created and switched between

VIDEO STUDIO
□ Text input → Claude API → scene JSON works end to end
□ SSE streaming shows live progress
□ Remotion player preview loads without SSR errors
□ All 7 format previews render without crashing
□ Edit controls update the preview in real-time
□ Render button → FFmpeg pipeline → MP4 file output
□ Google Drive upload works after render
□ Download button works

FLYER STUDIO
□ Input → Claude brief generation works
□ Canva template search returns results
□ Template selection → Canva design creation works
□ All 6 dimensions export correctly
□ QR code generates and downloads

CONTENT CALENDAR
□ All scheduled slots display on the correct dates
□ Drag and drop reschedule works
□ "Auto-fill calendar" AI scheduling works
□ Export to Google Calendar works
□ PDF export works

APPROVAL WORKFLOW
□ New content goes to pending queue
□ Approve moves to approved status
□ Reject with note works
□ "Revise with AI" regenerates correctly
□ Auto-approve mode (autonomous) works

TREND AGENT
□ Manual "Scan Now" works and returns briefs
□ Briefs display on dashboard correctly
□ "Generate from this trend" pre-fills Studio correctly
□ Cron endpoint is protected with CRON_SECRET

ANALYTICS
□ Performance data saves correctly
□ Charts render without library errors
□ Weekly AI report generates and displays
□ "Apply to Brand Vault" works

CONTENT LIBRARY
□ All content items display with thumbnails
□ Search works across captions and scripts
□ Filters work correctly
□ "Remix This" pre-fills Studio correctly
□ Evergreen toggle saves correctly

GENERAL
□ No unhandled console errors on any page
□ No blank white screens on any route
□ No TypeScript compilation errors
□ All environment variables are read correctly
□ app builds successfully with: npm run build
```

Run `npm run build` and fix every error before deploying.

---

## STEP 8 — DEPLOYMENT TO VERCEL + GODADDY DOMAIN

Follow these steps in exact order.

### 8A — Push to GitHub

```bash
# In the project terminal:
git init
git add .
git commit -m "feat: complete content automation machine v1"
git branch -M main

# Then go to github.com → New Repository
# Name it: content-machine
# Keep it Private
# Copy the remote URL it gives you, then run:

git remote add origin https://github.com/YOUR_USERNAME/content-machine.git
git push -u origin main
```

### 8B — Deploy to Vercel

1. Go to **vercel.com** → sign in with GitHub
2. Click **"Add New Project"**
3. Import the `content-machine` repository
4. Framework preset: **Next.js** (auto-detected)
5. Click **"Environment Variables"** and add ALL of these:

```
ANTHROPIC_API_KEY
NEXT_PUBLIC_SUPABASE_URL
NEXT_PUBLIC_SUPABASE_ANON_KEY
SUPABASE_SERVICE_ROLE_KEY
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
CRON_SECRET
PEXELS_API_KEY
PIXABAY_API_KEY
FREESOUND_CLIENT_ID
FREESOUND_CLIENT_SECRET
GOOGLE_DRIVE_FOLDER_ID
ELEVENLABS_API_KEY         (optional)
NEXT_PUBLIC_APP_URL        (set this to your GoDaddy domain URL)
```

6. Click **"Deploy"**
7. Wait 2–3 minutes for build to complete
8. Vercel gives you a `.vercel.app` URL — test it first

### 8C — Connect GoDaddy Domain

After Vercel deploys successfully:

1. In Vercel → go to your project → **Settings → Domains**
2. Click **"Add Domain"**
3. Type your GoDaddy domain (e.g. `contentmachine.com` or `theplugai.com`)
4. Vercel will show you TWO DNS records to add:
   ```
   Type: A     Name: @      Value: 76.76.21.21
   Type: CNAME Name: www    Value: cname.vercel-dns.com
   ```
5. Go to **godaddy.com → My Products → DNS** next to your domain
6. Delete any existing A record pointing to a GoDaddy parking page
7. Click **"Add New Record"** twice and add both records above
8. Save
9. Wait 10–30 minutes (DNS propagation)
10. Go back to Vercel → your domain should show a green checkmark

### 8D — Update Auth Callback URLs

After domain is connected, update these in two places:

**Supabase:**
- Go to supabase.com → your project → **Authentication → URL Configuration**
- Site URL: `https://yourdomain.com`
- Redirect URLs: add `https://yourdomain.com/auth/callback`

**Google Cloud Console:**
- Go to console.cloud.google.com → Credentials → your OAuth client
- Add to Authorized JavaScript origins: `https://yourdomain.com`
- Add to Authorized redirect URIs: `https://yourdomain.com/auth/callback`

### 8E — Set up cron-job.org (free)

1. Go to **cron-job.org** → create free account
2. Click **"Create Cronjob"**
3. URL: `https://yourdomain.com/api/cron/trend-scan`
4. Schedule: Daily at 7:00 AM
5. Under **"Headers"** → add:
   - Header name: `x-cron-secret`
   - Header value: your `CRON_SECRET` value
6. Save → your trend agent now runs every morning automatically

---

## STEP 9 — POST-LAUNCH SMOKE TEST

After going live, test these in order on the real domain:

```
1. Visit yourdomain.com → landing page loads
2. Click "Get Started" → auth page loads
3. Sign in with Google → redirects to onboarding or dashboard
4. Complete brand vault setup → saves correctly
5. Go to Video Studio → type a topic → generate content
6. Preview plays in browser
7. Approve and render → video downloads
8. Go to Flyer Studio → create a flyer → opens in Canva
9. Check Content Calendar → scheduled items show
10. Check /analytics → no errors
11. Click "Scan Now" on trends → returns briefs
```

If any step fails → report the exact error and route.
Fix it and redeploy with: `git push origin main`
Vercel auto-redeploys on every push.

---

## DELIVERABLES FOR THIS PROMPT

1. All journeys working end to end with zero dead ends
2. Autonomous mode functional (set and forget)
3. Manual mode functional (full control)
4. Hybrid mode set as default
5. Landing page built at root `/`
6. All QA checklist items passing
7. `npm run build` runs with zero errors
8. App deployed to Vercel
9. GoDaddy domain connected and live
10. cron-job.org trend scan configured
11. Final smoke test passing on live domain

Begin with the codebase audit in Step 1.
Read every file before touching anything.
Report your findings before writing any code.
```
