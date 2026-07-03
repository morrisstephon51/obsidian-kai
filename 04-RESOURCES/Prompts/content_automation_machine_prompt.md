# CONTENT AUTOMATION MACHINE — CLAUDE CODE MASTER PROMPT
### Zero New Subscriptions Edition | Video-First | Everything In-App

---

## CONTEXT & CONSTRAINTS

Build a full-stack Content Automation Machine web application that functions
as a complete autonomous marketing department. The primary output is AI-generated
short videos and flyers created entirely within the app. The user already pays for:

- Canva (paid plan) — use Canva API for flyer creation and animated exports
- Google Workspace (paid) — use Google Drive API for asset storage and Docs
- Figma (paid) — use Figma API for design token extraction

DO NOT suggest or require any additional paid subscriptions or services.
All AI video generation must happen inside the app using the free stack defined below.

---

## TECH STACK — ZERO NEW SUBSCRIPTIONS

### Frontend
- Framework: Next.js 14 (App Router, TypeScript)
- Styling: Tailwind CSS + shadcn/ui
- Animation: Framer Motion (free)
- Video Preview: Custom React player using HTML5 video + canvas

### Backend
- Runtime: Next.js API Routes + Edge Functions
- Database: Supabase (free tier — PostgreSQL)
- Storage: Supabase Storage (free tier — thumbnails, temp audio files,
  brand assets ONLY — max ~50MB per item. Final rendered MP4 videos must
  go to Google Drive. Supabase free tier is 1GB total; a single 60s video
  can be 50–150MB and would exhaust it quickly.)
  Google Drive (already paid) handles all final video file storage.
- Auth: Supabase Auth (email + Google OAuth — uses existing Google account)
- Scheduling: cron-job.org (100% free external cron service) → pings
  a protected Next.js API route on schedule. Do NOT use Vercel Cron Jobs
  — they require the Vercel Pro plan ($20/month) which violates the
  zero-subscription constraint.

### AI Engine
- Text/Script Generation: Anthropic Claude API (claude-sonnet-4-6)
  with web search tool enabled for trend detection
- Extended thinking enabled for strategy and long-form content

### VIDEO GENERATION ENGINE — ALL FREE
This is the core of the app. Use this exact stack:

1. REMOTION (https://remotion.dev) — PRIMARY VIDEO RENDERER
   - 100% free and open source (MIT license)
   - Renders React components to MP4 video server-side
   - Install: @remotion/core, @remotion/renderer, @remotion/player
   - Claude generates scene JSON → Remotion renders it to video
   - Live preview in browser using @remotion/player before rendering
   - Final render via @remotion/renderer on the server
   - This handles: kinetic text videos, slideshow videos, animated
     infographic videos, b-roll + overlay videos

2. PEXELS API (https://pexels.com/api) — FREE STOCK VIDEO & PHOTOS
   - Completely free, no subscription
   - Used for b-roll footage in video scenes
   - Also used for background images in flyers

3. PIXABAY API (https://pixabay.com/api/docs) — FREE STOCK MEDIA
   - Completely free backup for Pexels
   - Additional stock photos and video clips

4. WEB SPEECH API — FREE AI VOICEOVER (Primary)
   - Built into every modern browser, zero cost
   - Used to generate voiceover audio for videos in-browser
   - Capture with MediaRecorder API → save as audio file
   - Multiple voice options available natively

5. ELEVENLABS FREE TIER — OPTIONAL UPGRADE VOICEOVER
   - Free tier: 10,000 characters/month
   - Only use if user opts in, clearly label as optional
   - Falls back to Web Speech API if quota exceeded

6. FFMPEG.WASM — FREE SERVER-SIDE VIDEO PROCESSING
   - Use @ffmpeg/ffmpeg (WebAssembly build) ONLY — do NOT use fluent-ffmpeg
   - fluent-ffmpeg requires a system FFmpeg binary which cannot be installed
     on Vercel serverless functions — it will silently fail at deploy time
   - @ffmpeg/ffmpeg runs entirely in Node.js/browser with no binary dependency
   - Combine audio + video + music tracks
   - Add transitions between scenes
   - Encode final MP4 at correct dimensions per platform
   - Install: @ffmpeg/ffmpeg @ffmpeg/util @ffmpeg/core

7. FREESOUND API (https://freesound.org/apiv2) — FREE BACKGROUND MUSIC
   - Free API for royalty-free sound effects and ambient music
   - Used for video background tracks

### DESIGN ENGINE — USING EXISTING PAID TOOLS

8. CANVA API (already paid) — FLYER & IMAGE POST CREATION
   - Use Canva Connect API to create designs programmatically
   - Canva MCP server URL: https://mcp.canva.com/mcp
   - Create: social media posts, event flyers, story graphics,
     church bulletin inserts, email headers
   - Export in all required dimensions automatically
   - User's brand kit already in Canva — reference it by ID

9. FIGMA API (already paid) — DESIGN TOKENS
   - Pull brand colors, typography, and component specs
   - Use as the single source of truth for all visual consistency
   - Auto-sync brand vault colors from Figma variables

10. GOOGLE DRIVE API (already paid) — ASSET STORAGE & EXPORT
    - Store all generated videos in user's Google Drive
    - Organize by brand, platform, and date
    - Share links directly from the app

### Deployment
- Vercel (free tier) — handles the Next.js app
- Supabase (free tier) — handles database and small file storage
- Google Drive — handles large video file storage

---

## PROJECT STRUCTURE

```
content-machine/
├── app/
│   ├── (auth)/
│   ├── dashboard/
│   ├── generate/
│   ├── calendar/
│   ├── library/
│   ├── trends/
│   ├── analytics/
│   └── settings/
├── components/
│   ├── video-studio/
│   ├── flyer-studio/
│   ├── brand-vault/
│   ├── content-calendar/
│   └── ui/
├── lib/
│   ├── ai/
│   │   ├── claude.ts
│   │   ├── prompts.ts
│   │   └── video-schema.ts
│   ├── video/
│   │   ├── remotion-renderer.ts
│   │   ├── scene-builder.ts
│   │   ├── ffmpeg-processor.ts
│   │   └── voiceover.ts
│   ├── media/
│   │   ├── pexels.ts
│   │   └── pixabay.ts
│   ├── integrations/
│   │   ├── canva.ts
│   │   ├── figma.ts
│   │   └── google-drive.ts
│   └── supabase/
│       ├── client.ts
│       └── server.ts
├── remotion/
│   ├── compositions/
│   │   ├── HookAd15s.tsx
│   │   ├── Commercial30s.tsx
│   │   ├── Explainer60s.tsx
│   │   ├── TikTokOrganic.tsx
│   │   ├── ReelsOrganic.tsx
│   │   └── StorySequence.tsx
│   ├── components/
│   │   ├── KineticText.tsx
│   │   ├── SceneTransition.tsx
│   │   ├── CaptionOverlay.tsx
│   │   ├── LogoBug.tsx
│   │   └── CTACard.tsx
│   └── Root.tsx
├── supabase/
│   └── migrations/
└── public/
    └── fonts/
```

---

## MODULE 1 — BRAND VAULT

Build a locked brand configuration panel that governs every output.
Fields to store in Supabase `brands` table:

```typescript
interface BrandVault {
  id: string
  user_id: string
  brand_name: string
  industry: string
  mission: string
  taglines: string[]
  voice_descriptors: string[]       // ["bold", "warm", "community-first"]
  tone: {
    formal_vs_casual: number        // 0-100 slider
    serious_vs_playful: number      // 0-100 slider
  }
  content_pillars: ContentPillar[]
  target_personas: Persona[]
  color_palette: {
    primary: string                 // hex
    secondary: string
    accent: string
    background_dark: string
    background_light: string
    text_on_dark: string
  }
  font_preferences: {
    headline: string
    body: string
  }
  canva_brand_kit_id: string        // pulled from Canva API
  figma_file_id: string             // for design token sync
  banned_words: string[]
  compliance_rules: string[]
  sample_approved_posts: string[]   // few-shot examples for AI
  logo_url: string                  // stored in Supabase Storage
  video_style: VideoStyleConfig
}

interface VideoStyleConfig {
  primary_style: "kinetic_text" | "broll_overlay" | "slideshow" | "mixed"
  color_grade: "vibrant" | "muted" | "high_contrast" | "warm" | "cool"
  transition_style: "cut" | "fade" | "slide" | "zoom"
  text_animation: "typewriter" | "pop" | "slide_up" | "fade_in" | "bounce"
  music_genre: "hip_hop" | "gospel" | "ambient" | "electronic" | "corporate"
  voiceover_enabled: boolean
  voiceover_engine: "web_speech" | "elevenlabs"
  voiceover_voice_id: string
  caption_style: "bold_bottom" | "center_pop" | "side_scroll" | "none"
}
```

The Brand Vault is injected as a system prompt prefix on EVERY Claude API call.
Include 2-3 sample approved posts as few-shot examples in every generation call.

---

## MODULE 2 — AI VIDEO STUDIO (PRIMARY FEATURE — Built in Phase 2)

This is the core of the entire application. The workflow is:

```
User Input → Claude generates Scene JSON → Remotion previews in browser
→ User approves or edits → Server renders final MP4 → Saves to Drive
```

### Step 1: Input Collection
User provides ONE of:
- Topic/idea (free text)
- URL to scrape for context (article, event page)
- Uploaded document or image
- Upcoming event details (name, date, location, purpose)
- A previously saved post from the library

### Step 2: Claude Scene Generation
Call Claude API with this system prompt pattern:

```
SYSTEM: You are a world-class video ad director and copywriter for 
{brand_name}. {full_brand_vault_json}

You write SHORT VIDEO AD SCRIPTS that stop thumbs mid-scroll.
Every scene you write gets rendered as a real video inside our app.

RULES:
- Hooks must land in the first 2 seconds
- Every scene needs exact visual direction (what's on screen)
- Every scene needs exact voiceover text (what's spoken)
- Every scene needs on-screen text overlay (what's typed/shown)
- Return ONLY valid JSON, no markdown, no preamble
```

Claude must return a `VideoSceneData` JSON object for each video format.

### Video Scene Data Schema

```typescript
interface VideoSceneData {
  video_id: string
  format: VideoFormat
  brand_id: string
  total_duration_ms: number
  aspect_ratio: "9:16" | "1:1" | "16:9"
  resolution: "1080x1920" | "1080x1080" | "1920x1080"
  
  // Search terms for Pexels/Pixabay b-roll
  broll_search_queries: string[]
  
  // Background music direction
  music: {
    genre: string
    mood: string
    tempo: "slow" | "medium" | "fast"
    freesound_search: string
  }
  
  scenes: Scene[]
  
  // Platform-specific copy adjustments
  platform_copy: {
    tiktok_caption: string
    instagram_caption: string
    facebook_caption: string
    youtube_description: string
    hashtags: string[]
  }
  
  // Review metadata
  confidence_score: number
  review_flag: boolean
  review_reason: string
}

interface Scene {
  scene_id: string
  duration_ms: number
  
  // What the Remotion component renders
  background: {
    type: "broll_video" | "solid_color" | "gradient" | "image"
    value: string                   // search query, hex, gradient string, or url
    overlay_opacity: number         // 0-1 dark overlay on top of broll
  }
  
  // Text to display on screen
  text_layers: TextLayer[]
  
  // Spoken voiceover for this scene
  voiceover_text: string
  voiceover_timing_ms: number      // when voiceover starts in scene
  
  // Entry animation for this scene
  transition_in: "cut" | "fade" | "slide_up" | "zoom_in" | "wipe"
  transition_out: "cut" | "fade" | "slide_down" | "zoom_out" | "wipe"
}

interface TextLayer {
  id: string
  text: string
  style: "headline" | "subheadline" | "body" | "cta" | "caption" | "stat"
  position: "top" | "center" | "bottom" | "top-left" | "bottom-right"
  animation: "typewriter" | "pop_in" | "slide_up" | "fade_in" | "bounce"
  animation_delay_ms: number
  duration_ms: number
  font_size: "sm" | "md" | "lg" | "xl" | "2xl"
  color: string                    // hex — pulled from brand vault
  background_pill: boolean         // show pill/chip background behind text
  background_color: string
  bold: boolean
  uppercase: boolean
}
```

### Video Formats to Generate (All in One Run)

Generate ALL of these simultaneously using Promise.all:

```typescript
type VideoFormat =
  | "hook_15s"          // 15s — Hook + Claim + CTA
  | "commercial_30s"    // 30s — Hook + Problem + Solution + CTA
  | "explainer_60s"     // 60s — Full story arc
  | "tiktok_organic"    // 15-30s — Pattern interrupt, native feel
  | "reels_organic"     // 15-30s — Storytelling hook
  | "youtube_short"     // 45-60s — Value + subscribe CTA
  | "story_sequence"    // 3-slide Instagram/FB story set
```

Each format is a separate Claude API call running in parallel.
Show a real-time generation progress panel as each format completes.

### Step 3: Remotion Video Compositions

Build these Remotion compositions in /remotion/compositions/:

#### HookAd15s.tsx
```
Props: VideoSceneData (hook_15s format)
Structure:
- Scene 1 (0-3s): BOLD hook text explodes onto screen over dark bg or broll
- Scene 2 (3-10s): Single stat or claim with supporting visual
- Scene 3 (10-15s): CTA card with brand logo + call to action text
Animations: All text uses spring() from @remotion/core for physics-based
entry animations. @remotion/motion-blur is for motion blur effect only —
do NOT use it as the animation source.
```

#### Commercial30s.tsx  
```
Props: VideoSceneData (commercial_30s format)
Structure:
- Scene 1 (0-5s): Hook — problem statement or surprising fact
- Scene 2 (5-13s): Problem visualization — broll + text overlay
- Scene 3 (13-23s): Solution reveal — brand answer, value prop
- Scene 4 (23-30s): CTA card — logo, tagline, action
```

#### Explainer60s.tsx
```
Props: VideoSceneData (explainer_60s format)
Structure:
- Scene 1 (0-5s): Hook question
- Scene 2 (5-25s): Context/story with broll and voiceover
- Scene 3 (25-45s): Value proof — stats, benefits, community
- Scene 4 (45-60s): CTA with next steps
```

#### TikTokOrganic.tsx
```
Props: VideoSceneData (tiktok_organic format)
Native TikTok feel:
- No polished intro — jump straight to pattern interrupt
- Captions appear as bold subtitles word-by-word (TikTok caption style)
- Fast cuts every 2-3 seconds
- Trending audio direction shown as text overlay
```

#### ReelsOrganic.tsx
```
Props: VideoSceneData (reels_organic format)
Instagram Reels native feel:
- Warm, story-driven hook in first 2 seconds
- Mix of broll + text overlays with smooth fade transitions
- Captions styled in Instagram's native bold-white format
- Ends with a "save this" or "share with someone who needs this" CTA
- Aspect ratio: 9:16 (1080x1920)
```

#### YoutubeShort.tsx
```
Props: VideoSceneData (youtube_short format)
YouTube Shorts native feel:
- Opens with a direct question or surprising statement
- Structured: Question (5s) → Value answer (35s) → Subscribe CTA (10s)
- Bold chapter-style text overlays marking transitions
- End card: subscribe button placeholder + next video suggestion text
- Aspect ratio: 9:16 (1080x1920)
```
```
Props: VideoSceneData (story_sequence format)
Renders 3 separate 1080x1920 story cards:
- Card 1: Hook/attention grabber
- Card 2: Main message/offer
- Card 3: CTA + swipe-up instruction
Each card exported as both static image AND 5-second animated video
```

### Step 4: Live Preview
Use @remotion/player to show a live preview of the video IN THE BROWSER
before any rendering happens. User can scrub, play, pause.

Show all 7 format previews in a scrollable horizontal carousel.
Each preview card shows: platform icon, duration, aspect ratio toggle.

### Step 5: Edit Controls
Before rendering, allow user to edit:
- Any text layer (inline edit by clicking on the preview)
- Background style (swap broll search query → auto-fetches new Pexels clips)
- Color overrides (eyedropper from brand palette)
- Scene duration sliders
- Music selection (search Freesound directly in the panel)
- Voiceover toggle + voice selection

### Step 6: Server-Side Render
When user approves, the render process has TWO phases:

PHASE A — Browser (client-side, runs first):
1. Generate voiceover audio using Web Speech API + MediaRecorder
   (SpeechSynthesisUtterance → MediaRecorder captures audio stream → Blob)
2. Upload the captured audio Blob to Supabase Storage as .webm
3. Receive the audio file URL back before proceeding to Phase B

PHASE B — Server (after audio URL is available):
POST to /api/render-video with VideoSceneData + voiceover_audio_url

Server process:
1. Fetch Pexels/Pixabay clips for all broll queries
2. Download audio from Supabase Storage URL (from Phase A)
3. Download Freesound music track
4. Use @remotion/renderer to renderMedia() to MP4
5. Use @ffmpeg/ffmpeg (WASM) to mix voiceover + music at correct levels
6. Upload final MP4 to user's Google Drive
7. Delete temp audio file from Supabase Storage
8. Save metadata to Supabase
9. Return download URL + Drive link

NOTE: If ElevenLabs is selected instead of Web Speech, generate the
audio server-side via ElevenLabs API directly — Phase A is skipped.

Show a real-time render progress bar (SSE stream from server).

---

## MODULE 3 — FLYER & IMAGE STUDIO (CANVA API)

After video generation, automatically trigger flyer creation using Canva API.

### Canva Integration Architecture

```typescript
// lib/integrations/canva.ts
// Use the Canva MCP server (already connected at https://mcp.canva.com/mcp)
// For server-side API calls, use Canva Connect REST API

interface FlyerBrief {
  flyer_type: "event" | "program_promo" | "resource_awareness" | "social_share"
  
  // Claude generates all copy
  copy: {
    headline: string              // 3-8 words, punchy
    subheadline: string           // 1 supporting sentence
    body_copy: string             // 2-4 lines max
    cta_text: string              // button label
    cta_url: string               // link or QR destination
    event_details?: string        // date/time/location if applicable
  }
  
  // Design direction for Canva template search
  design: {
    canva_template_keywords: string[]
    color_palette: BrandColors
    layout: "centered" | "split" | "overlay" | "minimal"
    image_direction: string       // Pexels search query for hero image
    include_qr: boolean
    qr_data: string
    logo_placement: "top-left" | "top-center" | "bottom-center"
  }
  
  // Output dimensions — generate ALL of these every time
  dimensions: FlyerDimension[]
}

interface FlyerDimension {
  name: string
  width: number
  height: number
}

// Always generate all 6 of these per flyer brief:
const FLYER_DIMENSIONS: FlyerDimension[] = [
  { name: "Instagram Post",    width: 1080, height: 1080  },
  { name: "Instagram Story",   width: 1080, height: 1920  },
  { name: "Facebook Cover",    width: 1920, height: 1005  },
  { name: "Print Letter",      width: 2550, height: 3300  }, // 8.5x11 at 300dpi
  { name: "Twitter Card",      width: 1200, height: 675   },
  { name: "LinkedIn Banner",   width: 1584, height: 396   },
]
```

### Canva API Flow
1. Claude generates FlyerBrief JSON from the same input as the video
2. Search Canva templates using brief keywords
3. Present 3 template options to user (thumbnail preview)
4. User selects template
5. Use Canva editing API to inject brand copy, colors, and logo
6. Export all required dimensions
7. Save to Google Drive + Supabase

### QR Code Generation
Use qrcode npm package (free) to generate QR codes inside the app.
No external QR service needed. QR codes link to:
- Specialist email addresses (pre-configured per brand)
- Event registration pages
- Resource links
- Social media profiles

---

## MODULE 4 — CONTENT CALENDAR

Full drag-and-drop calendar showing all generated content.

```typescript
interface CalendarSlot {
  id: string
  brand_id: string
  content_item_id: string
  platform: Platform
  content_type: "video" | "flyer" | "image" | "text"
  scheduled_at: Date
  posted_at?: Date
  status: "draft" | "pending_approval" | "approved" | "scheduled" 
        | "posted" | "failed"
  thumbnail_url: string
  drive_url: string
}

type Platform = 
  | "instagram_reels" | "instagram_post" | "instagram_story"
  | "tiktok" | "youtube_shorts" | "facebook" | "linkedin" | "twitter"
```

Features:
- Monthly view with color-coded platform icons
- Click any slot → full preview of the video or flyer
- Drag to reschedule
- Bulk generate: pick a date range + content pillars → AI fills the calendar
- One-click export to Google Calendar (uses existing Google account)
- Export calendar as PDF for stakeholder review

---

## MODULE 5 — APPROVAL WORKFLOW

Every generated piece goes to "Pending Approval" first.

```typescript
interface ApprovalAction {
  type: "approve" | "edit_and_approve" | "reject" | "revise_with_ai"
  reviewer_id: string
  timestamp: Date
  notes?: string                  // required if rejecting
  ai_revision_feedback?: string   // if sending back to AI for revision
}
```

When "Revise with AI" is selected:
- Original content + rejection note + brand vault → new Claude call
- Regenerates only the failed format, not the whole set
- Shows side-by-side diff of original vs revision
- Tracks revision history

---

## MODULE 6 — TREND INTELLIGENCE AGENT

Autonomous agent that runs every morning at 7 AM via Vercel Cron.

```typescript
// app/api/cron/trend-scan/route.ts
// Triggered by cron-job.org (free) hitting this endpoint daily at 7 AM
// Protect this endpoint with a secret header:
// Check: request.headers.get('x-cron-secret') === process.env.CRON_SECRET
// Configure cron-job.org to send that header with every ping

// Process:
// 1. Use Claude with web search tool to find trending topics
// 2. Filter against brand's content pillars
// 3. Score relevance (0-100) and trend decay (days remaining)
// 4. Save to trend_briefs table
// 5. Send email notification if high-relevance trend found

interface TrendBrief {
  id: string
  brand_id: string
  topic: string
  summary: string                 // 2-sentence explanation
  relevance_score: number         // 0-100, match to brand pillars
  decay_estimate_days: number     // how long before trend goes cold
  source_urls: string[]
  suggested_angle: string         // how THIS brand should approach it
  content_pillar_match: string    // which pillar this fits
  used: boolean
  created_at: Date
}
```

On the dashboard, display today's trend briefs as cards.
Each card has a "Generate Content From This Trend" button that
pre-fills the Video Studio input and runs Module 2 automatically.

---

## MODULE 7 — PERFORMANCE TRACKER

Manual input panel (no extra API connections needed):

```typescript
interface PerformanceEntry {
  id: string
  content_item_id: string
  platform: Platform
  metrics: {
    views: number
    likes: number
    comments: number
    shares: number
    saves: number
    reach: number
    profile_visits: number
    link_clicks: number
  }
  recorded_at: Date
  week_number: number
}
```

Weekly AI Analysis (runs every Sunday at 11 PM):
- Claude analyzes performance data for the week
- Returns structured "What's Working / What's Not" report
- Recommendations are written back to Brand Vault as updated guidance
- Shown on Analytics dashboard as a visual report

---

## MODULE 8 — CONTENT LIBRARY

Permanent archive of all generated content.

Features:
- Grid view with video thumbnails and flyer previews
- Filter by: brand, platform, content type, pillar, status, performance tier
- Full-text search across all captions, scripts, and copy
- "Remix This" button → sends content back to Video Studio as new input
- Evergreen tagging → content marked evergreen auto-queues for recycling
  every 30/60/90 days based on user preference
- Bulk download as ZIP → all videos + flyers for a given campaign
- Direct link to Google Drive folder per content batch

---

## DATABASE SCHEMA (Supabase Migrations)

```sql
-- brands table
create table brands (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users not null,
  brand_name text not null,
  industry text,
  mission text,
  taglines text[],
  voice_config jsonb,
  tone_settings jsonb,
  content_pillars jsonb,
  target_personas jsonb,
  color_palette jsonb,
  font_preferences jsonb,
  canva_brand_kit_id text,
  figma_file_id text,
  banned_words text[],
  compliance_rules text[],
  sample_approved_posts text[],
  logo_url text,
  video_style_config jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

-- content_items table
create table content_items (
  id uuid primary key default gen_random_uuid(),
  brand_id uuid references brands not null,
  input_topic text,
  input_type text,                -- "topic" | "url" | "document" | "event"
  generated_at timestamptz default now(),
  video_outputs jsonb,            -- array of VideoSceneData objects
  flyer_outputs jsonb,            -- array of FlyerBrief objects  
  text_outputs jsonb,             -- captions, hashtags, etc.
  render_status text default 'pending',
  drive_folder_url text,
  status text default 'pending_approval',
  approval_history jsonb,
  tags text[],
  is_evergreen boolean default false,
  evergreen_recycle_days integer
);

-- calendar_slots table
create table calendar_slots (
  id uuid primary key default gen_random_uuid(),
  brand_id uuid references brands not null,
  content_item_id uuid references content_items,
  platform text not null,
  content_type text,
  scheduled_at timestamptz,
  posted_at timestamptz,
  status text default 'draft',
  thumbnail_url text,
  drive_url text
);

-- performance_data table
create table performance_data (
  id uuid primary key default gen_random_uuid(),
  content_item_id uuid references content_items,
  platform text,
  views integer default 0,
  likes integer default 0,
  comments integer default 0,
  shares integer default 0,
  saves integer default 0,
  reach integer default 0,
  link_clicks integer default 0,
  recorded_at timestamptz default now(),
  week_number integer
);

-- trend_briefs table
create table trend_briefs (
  id uuid primary key default gen_random_uuid(),
  brand_id uuid references brands not null,
  topic text,
  summary text,
  relevance_score integer,
  decay_estimate_days integer,
  source_urls text[],
  suggested_angle text,
  content_pillar_match text,
  used boolean default false,
  created_at timestamptz default now()
);

-- Auto-update trigger for brands.updated_at
create or replace function update_updated_at_column()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger brands_updated_at
  before update on brands
  for each row execute function update_updated_at_column();

-- render_jobs table (track Remotion render status)
create table render_jobs (
  id uuid primary key default gen_random_uuid(),
  content_item_id uuid references content_items,
  format text,
  status text default 'queued',   -- queued | rendering | complete | failed
  progress integer default 0,
  output_url text,
  drive_url text,
  error_message text,
  started_at timestamptz,
  completed_at timestamptz
);
```

---

## UI/UX REQUIREMENTS

### Visual Design Direction
- Dark mode by default (light mode toggle in settings)
- Design language: Bold, professional, modern — NOT generic SaaS
- Primary accent: Pulled from active brand's primary color (dynamic)
- Typography: Strong display font for headlines, clean mono for data
- Use Framer Motion for all page transitions and component animations

### Navigation Structure
Sidebar navigation with icons + labels:
```
⚡ Dashboard        → Today's trends + quick actions + recent renders
🎬 Video Studio     → PRIMARY — input → generate → preview → render
🪪 Flyer Studio     → Canva-powered flyer creation
📅 Calendar         → Content calendar + scheduling
📚 Library          → All generated content
📈 Trends           → Daily trend briefs from agent
📊 Analytics        → Performance tracking + AI reports
🏢 Brand Vault      → Brand configuration
⚙️ Settings         → API keys, integrations, preferences
```

### Video Studio UI Flow
1. Full-width input area (text, URL paste, or drag-drop file)
2. "Generate All Formats" button → triggers parallel Claude calls
3. Live generation progress: show each format completing in real-time
4. Video carousel: horizontal scroll of all 7 format previews
   - Each preview card: platform icon + Remotion player + duration badge
   - Active card expands to full preview
5. Edit panel: slides in from right when any preview is selected
6. "Render Selected" or "Render All" button
7. Render progress: real-time progress bar per format
8. Done state: download buttons + Drive link + "Add to Calendar" button

### Real-Time Streaming
Use Server-Sent Events (SSE) for:
- Generation progress (which format Claude is working on)
- Render progress (% complete per video)
- Trend brief notifications (new trends found)

### Mobile Responsive
Full mobile support for:
- Reviewing and approving content on the go
- Viewing trend briefs
- Checking the content calendar
- (Generation and rendering are desktop-primary but still functional)

---

## ENVIRONMENT VARIABLES

```env
# Anthropic
ANTHROPIC_API_KEY=

# Supabase
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# Google (OAuth + Drive API — already paid)
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
GOOGLE_DRIVE_FOLDER_ID=

# Canva (already paid)
CANVA_CLIENT_ID=
CANVA_CLIENT_SECRET=

# Figma (already paid)
FIGMA_ACCESS_TOKEN=
FIGMA_FILE_ID=

# Free Media APIs (all free, just need account)
PEXELS_API_KEY=
PIXABAY_API_KEY=
FREESOUND_CLIENT_ID=
FREESOUND_CLIENT_SECRET=

# Optional — ElevenLabs free tier
ELEVENLABS_API_KEY=

# Cron security (used with cron-job.org — free)
CRON_SECRET=

# Vercel
VERCEL_URL=
```

---

## KEY PACKAGE DEPENDENCIES

NOTE: The dependencies block below uses // comments for documentation.
Remove all comment lines before using as actual package.json content.
JSON does not support comments — they will cause parse errors.

```json
{
  "dependencies": {
    "next": "14.x",
    "react": "18.x",
    "typescript": "5.x",
    "@anthropic-ai/sdk": "latest",
    "@supabase/supabase-js": "latest",
    "@supabase/ssr": "latest",
    "@remotion/core": "latest",
    "@remotion/player": "latest",
    "@remotion/renderer": "latest",
    "@remotion/motion-blur": "latest",
    "@remotion/transitions": "latest",
    "@ffmpeg/ffmpeg": "latest",
    "@ffmpeg/util": "latest",
    "@ffmpeg/core": "latest",
    "qrcode": "latest",
    "qrcode.react": "latest",
    "@fullcalendar/react": "latest",
    "@fullcalendar/daygrid": "latest",
    "@fullcalendar/interaction": "latest",
    "tailwindcss": "latest",
    "framer-motion": "latest",
    "lucide-react": "latest",
    "googleapis": "latest",
    "axios": "latest",
    "date-fns": "latest",
    "zod": "latest",
    "zustand": "latest"
  }
}
```

---

## AI AGENT BEHAVIOR RULES

Every Claude API call must follow these rules:

1. ALWAYS inject the full Brand Vault as the system prompt prefix
2. ALWAYS include 2-3 sample approved posts as few-shot examples
3. ALWAYS request JSON-only output for structured generation
4. USE extended thinking for complex generation by passing the correct
   API parameter structure:
   ```json
   "thinking": { "type": "enabled", "budget_tokens": 10000 }
   ```
   Enable for:
   - Weekly performance analysis reports
   - Full campaign strategy generation
   - YouTube long-form scripts
5. USE web search tool for:
   - Trend intelligence agent runs
   - Any generation tagged as "trending" or "timely"
   - Fact-checking health statistics (BigHeart Health brand)
6. NEVER generate content that:
   - Makes direct medical claims (BigHeart Health brand rule)
   - Promises financial outcomes (The Plug AI brand rule)
   - Contains any word in the brand's banned_words list
   - Lacks a clear CTA unless format is awareness-only
7. VIDEO SCRIPTS: always return scene-by-scene JSON, never prose
8. CONFIDENCE SCORING: every output gets a 1-10 confidence score
   and a review_flag boolean with reason

---

## BUILD ORDER — EXECUTE IN THIS SEQUENCE

Build and fully test each module before starting the next.
Do not scaffold everything and leave it hollow.

### Phase 1 — Foundation (Build First)
1. Supabase schema migrations
2. Next.js project scaffold with auth
3. Brand Vault module (UI + Supabase CRUD)
4. Claude API integration + prompt system
5. Seed script with two demo brands (BigHeart Health + The Plug AI)

### Phase 2 — Core Engine (Build Second)
6. Remotion compositions: all 6 video format components
7. Pexels + Pixabay media fetching
8. Video Studio input + Claude generation flow
9. @remotion/player live preview in browser
10. Server-side render endpoint + FFmpeg audio mix
11. Google Drive upload integration

### Phase 3 — Design Layer (Build Third)
12. Canva API flyer brief generation
13. Canva template search + selection UI
14. QR code generation (qrcode package)
15. Flyer export + Drive storage

### Phase 4 — Operations Layer (Build Fourth)
16. Content Calendar with FullCalendar
17. Approval workflow queue
18. Content Library with search + filters
19. Trend Intelligence Agent cron job
20. Performance tracker + weekly AI report

### Phase 5 — Polish
21. Mobile responsive layouts
22. SSE streaming for real-time progress
23. Dark/light mode toggle
24. Notification system
25. README.md + .env.example + architecture diagram

---

## DELIVERABLES

1. Full working Next.js application with all modules functional
2. All Supabase migration SQL files
3. All Remotion composition components (6 video formats)
4. .env.example with every variable documented and labeled as
   "REQUIRED" or "OPTIONAL — FREE TIER AVAILABLE"
5. README.md with:
   - Complete setup guide (step by step, no assumed knowledge)
   - How to connect Canva, Google Drive, and Figma (already paid)
   - How to get free API keys for Pexels, Pixabay, Freesound
   - Architecture diagram in Mermaid syntax
   - Brand Vault configuration guide
   - How to add a new Remotion video composition
6. Seed script: pre-populates two demo brands:
   - BigHeart Health (navy/gold, healthcare/faith community)
   - The Plug AI (purple/amber, AI education)
   Both brands seeded with sample approved posts so the app
   is not empty on first launch.

Begin with Phase 1. Confirm the project structure and database
schema before writing any component code. Ask one clarifying
question if anything in this spec is ambiguous.
```
