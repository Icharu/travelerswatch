---
name: configwatch
description: Shows and changes the Traveler's Watch settings for a project — the checkpoint cadence (every N commits or M sessions, or off) stored in the Status section of .watch/WATCH.md — without touching the bearing. Use when the user runs /configwatch, asks how often checkpoints should happen, wants the "checkpoint is due" nudge more or less often or turned off, or wants to see the watch's current status.
license: MIT
metadata:
  version: "1.1.0"
  family: travelers-watch
---

# /configwatch — set how often the watchman calls for a checkpoint

The watchman checks every prompt against the bearing, but only a **checkpoint** (`/checkwatch`) can
tell whether the bearing itself still matches reality. The cadence decides when the watchman asks
for one. A wrong bearing set at intake is caught at the first checkpoint — so the first one should
come early; later ones can be spaced out.

## Preconditions

- `.watch/WATCH.md` must exist. If not, offer `/checkwatch` to set the bearing first.
- If it has no `## Status` section (a v1.0 logbook), offer to add one, placed right after the
  intro quote:

  ```markdown
  ## Status
  - **Bearing:** confirmed
  - **Checkpoint cadence:** every 3 commits or 2 sessions
  - **Last checkpoint:** <today> @ <short HEAD SHA, or — without git>
  ```

## Steps

1. **Show the current settings** in one short block: bearing status, cadence, last checkpoint, and —
   if you can compute it — commits since the last checkpoint (`git rev-list --count <sha>..HEAD`).
2. **Ask for the new cadence.** Offer:
   - **Shakedown (default)** — `every 3 commits or 2 sessions`. Best right after intake or a big
     `/fixwatch`.
   - **Steady** — `every 10 commits or 5 sessions`. For a bearing that has passed at least one checkpoint.
   - **Custom** — any `every N commits or M sessions`; either part may be left out
     (`every 5 commits`, `every 3 sessions`).
   - **Off** — `off`. The watchman still flags drift on every prompt; only the checkpoint nudge stops.
     Warn once: a bearing that is wrong about the project will then only be caught when someone runs
     `/checkwatch` by hand.
3. **Write exactly one line** in `## Status`: `- **Checkpoint cadence:** <value>`. Use the exact
   wording `every N commits or M sessions` / `off` — the watchman hook parses it. Do not change any
   other line.
4. **Append a Path log entry** (settings changes are recorded too, but they are not course changes):

   ```markdown
   ### <YYYY-MM-DD> — Watch settings changed
   - **Trigger:** settings
   - **Proposed by:** PM
   - **Change:** Checkpoint cadence <old> → <new>
   - **Reason:** <why, in the PM's words>
   - **Impact:** none on the bearing
   - **PM confirmation:** <name or initials, date>
   ```

5. Suggest committing: `watch: cadence <new>`.

## How the cadence is counted

- **Commits:** commits on the current branch since the SHA in *Last checkpoint*.
- **Sessions:** distinct Claude Code sessions with at least one prompt since the last checkpoint,
  not counting the session where the checkpoint happened. Counted locally in `.watch/.state`
  (git-ignored).
- The nudge fires **at most once per session**; a new `/checkwatch` resets both counts.

## Rules

- Never change the bearing (Scope, Standard, Context, Constraints, Problem, Tools) here — that is
  `fixwatch`. Never change `Bearing:` status here either: *under review* is set by a checkpoint and
  closed by `/fixwatch`.
- Never rewrite earlier Path log entries.
