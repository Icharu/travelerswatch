# ADR 0002 — Keep the logbook in the project repository, committed

- **Status:** Accepted
- **Date:** 2026-11-25

## Context

The bearing must survive what breaks the traveler's watch: conversation summarization, new sessions,
switching agents, and team members joining mid-project. Options were a file in the repo (committed
or git-ignored), a user-chosen path (e.g. a notes vault), or memory inside the agent.

## Decision

Store the bearing at `.watch/WATCH.md` in the project root and recommend committing it.

- The PM and team review the path and every course change through normal version control.
- `/fixwatch` appends to an in-file Path log; git history is the second, tamper-evident record.
- The skills suggest a commit after every bearing change (`watch: <short title>`).

## Consequences

- The bearing is visible to anyone with read access to the repo. Do not put secrets or personal data
  in it.
- A malicious edit to the file would reach the model through the hook; mitigated by treating it as
  data and by code review of changes to `.watch/` (see [SECURITY.md](../../SECURITY.md)).
- Teams that cannot commit it may git-ignore `.watch/`; everything still works locally.
