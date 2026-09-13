#!/usr/bin/env node
// Rebuilds _INDEX.md, the file agents read before opening vault notes.
// One line per note: `path — gist (modified)`, grouped by top-level folder.
// Generated folders (agent output/results) collapse to one summary line so the index stays cheap to read every loop.
//
//   node _ops/build-index.mjs            rebuild _INDEX.md
//   node _ops/build-index.mjs --check    exit 1 and list the drift if _INDEX.md is stale; writes nothing
//
// Gists already in _INDEX.md are kept. New notes take frontmatter `description:`, else their H1.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const args = process.argv.slice(2);
const opt = (name) => { const i = args.indexOf(name); return i === -1 ? null : args[i + 1]; };
const vault = path.resolve(opt('--vault') ?? path.join(path.dirname(fileURLToPath(import.meta.url)), '..'));
const indexPath = path.join(vault, '_INDEX.md');
const outPath = path.resolve(opt('--out') ?? indexPath);
const checkOnly = args.includes('--check');

const COLLAPSE_NAMES = new Set(['output', 'results', 'sessions']);
const COLLAPSE_OVER = 40;
const NOTE_LINE = /^- (.+?\.md)(?: — (.*))? \(\d{4}-\d{2}-\d{2}\)$/;
const DIR_LINE = /^- (.+\/) — \d+ generated files, /;

const day = (ms) => {
  const d = new Date(ms);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
};
const visible = (dir) => fs.readdirSync(dir, { withFileTypes: true }).filter((e) => !e.name.startsWith('.') && e.name !== 'node_modules');

const notes = [];
const collapsed = [];
const attachments = new Map();

function summarize(dir) {
  let count = 0;
  let newest = 0;
  (function tally(d) {
    for (const e of visible(d)) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) tally(p);
      else { count++; newest = Math.max(newest, fs.statSync(p).mtimeMs); }
    }
  })(dir);
  return { count, newest };
}

function walk(dir) {
  const rel = path.relative(vault, dir);
  const entries = visible(dir);
  const agentOutput = rel.startsWith(`07-AI${path.sep}agents${path.sep}`) && COLLAPSE_NAMES.has(path.basename(dir));
  if (rel && (agentOutput || entries.filter((e) => e.isFile()).length > COLLAPSE_OVER)) {
    collapsed.push({ rel: `${rel}/`, ...summarize(dir) });
    return;
  }
  for (const e of entries) {
    const p = path.join(dir, e.name);
    const r = path.relative(vault, p);
    if (e.isDirectory()) walk(p);
    else if (r === '_INDEX.md') continue;
    else if (e.name.endsWith('.md')) notes.push({ rel: r, mtime: fs.statSync(p).mtimeMs });
    else {
      const top = r.includes(path.sep) ? `${r.split(path.sep)[0]}/` : '(root)';
      const ext = path.extname(e.name).slice(1).toLowerCase() || 'no-ext';
      const a = attachments.get(top) ?? { count: 0, exts: new Set() };
      a.count++;
      a.exts.add(ext);
      attachments.set(top, a);
    }
  }
}
walk(vault);

const previous = fs.existsSync(indexPath) ? fs.readFileSync(indexPath, 'utf8') : '';

if (checkOnly) {
  const listedNotes = new Set();
  const listedDirs = new Set();
  for (const line of previous.split('\n')) {
    const n = line.match(NOTE_LINE);
    if (n) listedNotes.add(n[1]);
    else if (DIR_LINE.test(line)) listedDirs.add(line.match(DIR_LINE)[1]);
  }
  const missing = [...notes.map((n) => n.rel).filter((r) => !listedNotes.has(r)), ...collapsed.map((c) => c.rel).filter((r) => !listedDirs.has(r))];
  const gone = [...[...listedNotes].filter((r) => !notes.some((n) => n.rel === r)), ...[...listedDirs].filter((r) => !collapsed.some((c) => c.rel === r))];
  if (!missing.length && !gone.length) { console.log('_INDEX.md is current'); process.exit(0); }
  console.log(`_INDEX.md is stale: ${missing.length} not listed, ${gone.length} listed but gone`);
  for (const r of missing.slice(0, 20)) console.log(`  + ${r}`);
  for (const r of gone.slice(0, 20)) console.log(`  - ${r}`);
  console.log('Rebuild: node _ops/build-index.mjs');
  process.exit(1);
}

const oldGists = new Map();
for (const line of previous.split('\n')) {
  const m = line.match(NOTE_LINE);
  if (m?.[2]) oldGists.set(m[1], m[2]);
}

function gistFor(rel) {
  const text = fs.readFileSync(path.join(vault, rel), 'utf8').slice(0, 4000);
  // Keep existing gists, except an "(empty)" label on a note that has since been filled in.
  const old = oldGists.get(rel);
  const hasBody = text.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n?/, '').trim().length > 0;
  if (old && !(/^\(?empty\)?$/i.test(old) && hasBody)) return old;
  const front = text.match(/^---\r?\n([\s\S]*?)\r?\n---/)?.[1] ?? '';
  const description = front.match(/^description:\s*["']?(.+?)["']?\s*$/m)?.[1];
  if (description) return description;
  const h1 = text.match(/^# (.+)$/m)?.[1]?.trim();
  if (h1 && h1.toLowerCase() !== path.basename(rel, '.md').toLowerCase()) return h1;
  return null;
}

const topOf = (rel) => (rel.includes('/') ? `${rel.split('/')[0]}/` : '(root)');
const byTop = new Map();
const add = (top, sortKey, line) => {
  if (!byTop.has(top)) byTop.set(top, []);
  byTop.get(top).push([sortKey, line]);
};
for (const n of notes) {
  const gist = gistFor(n.rel);
  add(topOf(n.rel), n.rel, `- ${n.rel}${gist ? ` — ${gist}` : ''} (${day(n.mtime)})`);
}
for (const c of collapsed) {
  add(topOf(c.rel), c.rel, `- ${c.rel} — ${c.count} generated files, newest ${c.newest ? day(c.newest) : 'n/a'} (collapsed; list the folder to see them)`);
}

const sectionOrder = (a, b) => {
  const rank = (s) => (s === '(root)' ? 2 : /^\d/.test(s) ? 0 : 1);
  return rank(a) - rank(b) || a.localeCompare(b);
};

const today = day(Date.now());
const created = previous.match(/^created:\s*(\S+)/m)?.[1] ?? today;
const out = [
  '---',
  `created: ${created}`,
  `updated: ${today}`,
  'type: note',
  'status: active',
  'tags: []',
  '---',
  '',
  `# Vault index — built ${today}`,
  '<!-- FOR AI AGENTS: read this file first, then open only the note you need. Check freshness: node _ops/build-index.mjs --check. Rebuild: node _ops/build-index.mjs. Format: path — gist (modified). Generated folders are collapsed to one line. -->',
  '',
];
for (const top of [...byTop.keys()].sort(sectionOrder)) {
  out.push(`## ${top}`);
  for (const [, line] of byTop.get(top).sort((a, b) => a[0].localeCompare(b[0]))) out.push(line);
  out.push('');
}
if (attachments.size) {
  out.push('## Attachments / non-markdown');
  for (const top of [...attachments.keys()].sort(sectionOrder)) {
    const a = attachments.get(top);
    out.push(`- ${top} — ${a.count} files (${[...a.exts].sort().join(', ')})`);
  }
  out.push('');
}

const tmp = path.join(path.dirname(outPath), `.${path.basename(outPath)}.tmp`);
fs.writeFileSync(tmp, out.join('\n'));
fs.renameSync(tmp, outPath);
console.log(`Wrote ${outPath}: ${notes.length} notes, ${collapsed.length} collapsed folders, ${[...attachments.values()].reduce((s, a) => s + a.count, 0)} attachments`);
