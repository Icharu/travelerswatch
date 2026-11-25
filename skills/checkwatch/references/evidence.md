# Evidence scan — setting the watch against the sun

Intake answers can be **consistent with each other and still wrong about the project**. Every check
that only compares the PM's answers to each other will pass such a bearing. The evidence scan gives
the intake an independent reference — what the project's own documents and history say — so that
contradictions surface before the bearing is confirmed.

## What to read (in this order, stop when you have enough)

| Priority | Source | Look for |
|---|---|---|
| 1 | `README*`, project root docs | What the project is, status badges, "known issues", deployment state |
| 2 | Evaluations, reviews, audits, post-mortems (`docs/evaluation*`, `docs/review*`, `*report*`) | Verdicts (GO/NO-GO), open findings and their severity, recommended next phases |
| 3 | Decision records (`docs/adr/`, `docs/decisions/`) | Fixed choices: stack, hosting, data rules — these are often hidden constraints |
| 4 | Plans and specs (`docs/spec*`, `ROADMAP*`, `TODO*`, `CHANGELOG*`) | Stated objectives, what is next, what was dropped |
| 5 | `git log --oneline -30` and `git log --since=<30 days>` | What the work has *actually* been about recently |
| 6 | Open issues/PRs if the forge CLI is available | Blockers, priorities others have raised |
| 7 | Non-software projects: the folder's documents (briefs, minutes, budgets, protocols) | Same questions: state, decisions, limits, objective |

Read headings, summaries, verdicts, and tables — not every line. A dozen files is usually plenty.

## The evidence card (show this to the PM)

```markdown
**Evidence card** — sources: README, docs/evaluation/…, docs/adr/0001–0006, git log (30)

| Topic | Evidence says | Source |
|---|---|---|
| Current state | Live in production with 3 open high-severity findings | docs/evaluation/… §Verdict |
| Fixed choices | Stack and hosting decided; institutional server | docs/adr/0002, 0006 |
| Recent work | 7 of last 11 commits close security findings | git log |
| Referenced works | Evaluation (date), prior review (date) | docs/ |
```

Describe sensitive findings by **severity and area**, not by exploit detail, and never copy secrets
or personal data into the card or the logbook.

## Comparing answers with evidence

For each section the PM answers, ask: *does any line of the evidence card contradict this?*

| Pattern | Example | What to do |
|---|---|---|
| **State mismatch** | PM: "it works, just looks old" · evaluation: NO-GO with open blockers | Show both; ask which is current. |
| **Hidden constraint** | PM lists a hosting tool · ADR fixes institutional hosting | Constraint missing; tool may break it. |
| **Priority mismatch** | PM: redesign · recent commits and evaluation: security remediation | Ask whether the bearing should steer toward the documented priority. |
| **Phantom reference** | PM cites "last year's report" · not in the repo | Ask for it or record it as not available. |

Each contradiction is **resolved** (a section changes) or **accepted** by the PM explicitly, written
in Relations as `<PM statement> ↔ <evidence> (<source>). *Accepted contradiction (PM).*` The watchman
hook injects accepted contradictions on every prompt, so they stay visible.

## When there is no evidence

Some projects have nothing written down yet. That is fine — say so, record
`Evidence scanned: none found`, and remind the PM that the bearing rests on their word alone. The
shakedown checkpoint (default: after 3 commits or 2 sessions) is the next chance to catch a wrong
bearing; keep it on.

## Limits

The scan finds what is written down. A misconception that exists only in someone's head, with no
document or history to contradict it, will still pass intake. That is why the design has three
layers: **prevent** (this scan), **detect** (the two-direction checkpoint and its shakedown cadence),
and **contain** (the *under review* status that pauses drift flags until `/fixwatch`).
