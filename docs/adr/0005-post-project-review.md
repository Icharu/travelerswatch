# ADR 0005 — Checkpoint log and post-project review from the logbook

- **Status:** Accepted
- **Date:** 2026-11-25
- **Extends:** ADR 0002 (committed logbook), ADR 0003

## Context

Koshman & Zubkova (2026) reviewed 97 publications on AI in project management and found little
research on AI in later life-cycle phases such as the **post-project review**. We checked whether
TTW supports one. Being transparent about the answer:

| Question | Before this ADR (v1.1.0) |
|---|---|
| Is there a step that reviews a finished project or phase? | **No.** `/checkwatch` only had intake and checkpoint. |
| Does the logbook keep checkpoint verdicts? | **No.** Only the date and SHA of the *last* checkpoint; every earlier verdict was overwritten. |
| Does the logbook keep course changes? | Yes: the Path log is append-only, with trigger, reason, impact, and PM confirmation. |
| Can the original bearing be recovered? | Partly: from the *Bearing set* entry, and from git history if the logbook was committed. |
| Can a project be marked as finished? | **No.** The watchman kept injecting the bearing forever. |

So the Path log was a good start, but a review built from it alone would miss every checkpoint
verdict, and there was no way to close the watch.

## Decision

1. **Checkpoint log.** Logbook v1.2 adds an append-only `## Checkpoint log` section, placed before
   the Path log. Each checkpoint appends one line: date, SHA, verdict, reason. Older logbooks get the
   heading at their next checkpoint.
2. **Post-project review** (`/checkwatch` Part C). When the PM says the project or phase is ending,
   Claude rebuilds the timeline from the Checkpoint log, the Path log, and git history; compares the
   original and final bearing; reports any unlogged change; judges the Final objective and the
   accepted risks against evidence; and drafts lessons tied to entries or commits.
3. **The PM decides** between *review and close*, *review only* (e.g. end of a phase), edit, or
   cancel. Nothing is written before that.
4. **Closed status.** On close, Status becomes `Bearing: closed <date> — post-project review`, the
   review is written to `.watch/reviews/`, and the watchman goes silent. `/fixwatch` can reopen it
   as a logged scope change.

## Consequences

- The hook needs one new case (`closed` → silent); the Checkpoint log needs none, because the hook
  ignores sections it does not parse. Both are covered by tests 16–17.
- **Limits, stated plainly:** checkpoint verdicts from before v1.2 are not recoverable. A review
  is only as good as the logbook: changes made without `/fixwatch` show up only as unlogged
  differences in git, and not at all if the logbook was never committed. The review is a
  self-assessment drafted by the model and confirmed by the PM, not an independent audit.
