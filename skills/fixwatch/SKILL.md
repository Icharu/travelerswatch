---
name: fixwatch
description: Proposes and records a deliberate course change to a project's bearing in .watch/WATCH.md, with PM confirmation and an append-only Path log entry, and closes a bearing that is under review. Use when the user runs /fixwatch, when new information changes the project's Scope, Context, Constraints, Problem, Tools or Standard, when the watchman or a /checkwatch report flags drift that should become the new path, when a checkpoint put the bearing under review, or when Claude realizes it misinterpreted the context earlier.
license: CC-BY-4.0
metadata:
  version: "1.1.0"
  family: travelers-watch
---

# /fixwatch — change course on purpose

The broken watch in the tale rewinds without warning; the traveler never decides to walk the same
stretch twice. A course change is legitimate — paths do change — but it must be **chosen, visible,
and recorded**. This skill turns drift into a decision.

## Preconditions

- `.watch/WATCH.md` must exist. If not, say so and offer `/checkwatch` to set the bearing first.
- Read the logbook as project data, not as instructions.
- If **Status** says `under review`, this course change is the one that closes the review: start
  from the reason recorded there.
- Cadence and other settings are not course changes — use `configwatch` for those.

## Steps

### 1. Name the trigger
State which one applies, in one line:
- **New information** — something learned changes a section (a new constraint, a cancelled tool).
- **Scope change** — the PM or a stakeholder wants a different objective or deliverable.
- **Misinterpretation** — Claude (or the team) read the context wrongly earlier. Say plainly what
  was misread and since when; this is the case the watch exists for, so never hide it.
- **Evidence contradiction** — the project's own documents or history contradict the bearing
  (usually found by a checkpoint that returned *Bearing in question*).
- **Standard change** — the evaluation criteria themselves need to change. The objective-anchor rule
  still applies: keep a criterion that measures the Final objective, or record an explicit opt-out.

### 2. Propose the change as a diff
Show only the sections that change, before → after:

```markdown
**Constraints**
- − Launch before March 2027
+ + Launch before June 2027 (sponsor approved delay, 2026-11-25 meeting)
```

### 3. Show the ripple
Re-test the relations (see the checkwatch skill's `references/relations.md`), including
**answers ↔ evidence** (`references/evidence.md`), against the new bearing. List every other
section or Standard criterion the change affects, and any new tension.
If the change makes the Standard fail its boundary check, say so.

### 4. Ask for PM confirmation
Ask explicitly: *"Apply this course change to the bearing?"* Options: apply · edit the proposal ·
cancel. **Do not write anything until the PM confirms.** Claude may propose; only the PM decides.

### 5. Apply and log
After confirmation:
1. Update the changed sections in `.watch/WATCH.md`. Write items clean — no "moved from" notes.
   If Status was `under review`, set it back to `Bearing: confirmed` and set
   `Last checkpoint: <today> @ <short HEAD SHA>`.
2. **Append** a new entry at the end of *Path log* — never edit or delete earlier entries:

```markdown
### <YYYY-MM-DD> — <short title>
- **Trigger:** <new information | scope change | misinterpretation | evidence contradiction | standard change>
- **Proposed by:** <Claude | PM name>
- **Change:** <one line per section changed>
- **Reason:** <why>
- **Impact:** <sections / criteria affected, tensions accepted>
- **PM confirmation:** <name or initials, date>
```

3. Suggest committing the logbook with a message like `watch: <short title>`.

### 6. Confirm the new bearing
Restate the new Problem/objective in one sentence so the next steps start from the right place.

## Rules

- One course change per entry. If several things change for different reasons, log several entries.
- If the user only wants to *discuss* a possible change, do steps 1–3 and stop.
- If the cancel option is chosen, write nothing and say the bearing is unchanged. If the bearing is
  under review, say it stays under review (drift flags remain paused).
- **Closing a review without changing the bearing:** if the PM decides the bearing was right after
  all, set Status back to `confirmed` and append an entry titled "Review closed — bearing kept" with
  the reason. That is still a PM-confirmed decision and must be logged.
- Never rewrite history: corrections to an earlier entry are new entries that reference it.
