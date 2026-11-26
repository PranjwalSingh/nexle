# Current Work — Nexle

---

## CV Editor — Replacing LaTeX Compiler

Currently using `pdflatex` via `cv_compiler.py` which requires ~4GB RAM — too heavy for free deployment tiers.

**Goal:** replace with a lightweight visual editor embedded via iframe or a free open-source WYSIWYG solution.
Options being evaluated: `@docx-editor.dev/react`, OnlyOffice Community Edition, Google Docs embed.
PDF export stays, the LaTeX pipeline goes.

---

## Auth — Google & GitHub OAuth

Swapping manual email/password login for OAuth via Supabase.

- Enable Google + GitHub providers in Supabase dashboard
- Create OAuth apps on Google Cloud Console and GitHub, paste credentials into Supabase
- Frontend uses `supabase.auth.signInWithOAuth({ provider: 'google' })`

**Google scopes to request:**
- Gmail read/send — for polling application emails and sending cold emails on the user's behalf
- Google Calendar read/write — for scheduling interviews and follow-ups on the user's behalf
- Standard profile scopes (email, name, profile picture)

Tokens must be stored and refreshed — this is ongoing work.

---

## Frontend

Full redesign in progress. Currently just a simple landing page placeholder while backend stabilises.

--- 

## Auto-Apply Extension

Browser extension that fills job application forms automatically.

**MVP approach (record + replay):**
- Manually record form-filling sessions (similar to Playwright codegen), generating reusable Python test cases
- Replace hardcoded values in test cases with profile variables (`f"{full_name}"` etc.)
- On apply: inject JS to fetch live DOM, match against test case library algorithmically (no LLM), adapt and fill maximally
- Single-page forms only for MVP — if multi-page detected, exit and label job as `unapplied_attempted`
- Store match ratio between test and actual page; invoke LLM only if submission fails

**Later — smart agent + shared test cases:**
- For high-importance jobs (many users + high score), after the first agent run generates a test case, store it on the job record
- Subsequent users reuse that test case with their own values instead of re-running the full agent: saves LLM tokens significantly
- DOM diff check at runtime to verify the stored test case still applies
- Branch handling for conditional DOM changes (checkboxes, yes/no answers that show/hide fields) stored as separate paths

---

## Email Tracking — Post-Apply

After auto-applying, poll Gmail for emails from the same company domain.

- Map incoming emails to job IDs precisely by company domain + timing
- Classify: OA, interview, rejection, thank-you confirmation
- Flag if any follow-up action is needed
- Update `user_jobs.status` automatically based on email content
- Diversify application order across companies to reduce email ambiguity

---

## Job Forum — Per Posting

Community thread per job posting, initially targeted at UW students.

- Any user who has a job in their dashboard can open or join its thread
- Automated prompts when a user's status updates (OA received, interview, offer, rejection) — opt-in transparency
- Lets applicants see where others are in the process for the same job
- Threads scoped to the canonical `jobs` table row so all users referencing the same posting share one forum

---