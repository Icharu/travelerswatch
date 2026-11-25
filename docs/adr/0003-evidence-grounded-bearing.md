# ADR 0003 — Ground the bearing in project evidence, and contain a wrong one

- **Status:** Accepted
- **Date:** 2026-11-25
- **Supersedes:** nothing; extends ADR 0001 and ADR 0002

## Context

The v1.0.0 intake built the bearing only from the PM's answers and checked them for internal
consistency. A [benchmark](../benchmarks/2026-11-25-best-vs-worst.md) on a live project showed the
failure mode: a PM gave a plausible account ("it works, it just looks old") that contradicted the
project's own evaluation (live with release blockers). Every intake check passed. The per-prompt
watchman then steered the work *away* from the real problem (1 of 4 drift probes correct) until a
checkpoint found the contradiction 15 days later.

Checking an account for coherence does not check it for correspondence with reality. The watch can
be set wrong at the start, and checking it more often does not help; it has to be set against an
outside reference.

## Decision

Defend in three layers.

1. **Prevent — evidence-grounded intake.** Ask for a one-line Scope, then scan the project's own
   documents and history (`skills/checkwatch/references/evidence.md`) before the Standard. Draft
   the sections from evidence. Every contradiction between the PM's answers and the evidence must be
   **resolved or explicitly accepted** (`*Accepted contradiction (PM).*`). Require one Standard
   criterion that measures the Final objective (explicit, recorded opt-out allowed).
2. **Detect — two-direction checkpoint + shakedown.** Checkpoints judge *work vs bearing* and
   *bearing vs reality*; the latter yields the verdict **Bearing in question**. A cadence in the
   logbook's Status (default `every 3 commits or 2 sessions`, set by `/configwatch`) makes the
   watchman nudge for a checkpoint at most once per session.
3. **Contain — bearing status.** A checkpoint may mark the bearing **under review** (PM confirms).
   While under review, the hook stops injecting the bearing and stops flagging drift; it points to
   the pending `/fixwatch`, which closes the review.

The hook also injects Scope and a digest of Boundary notes and accepted risks/contradictions.

## Consequences

- Intake reads project files. They are treated as data, never instructions; findings are summarized
  by severity and area; secrets and personal data are never copied into the logbook.
- The hook writes a small local state file (`.watch/.state`, git-ignored) to count sessions.
- Per-prompt cost rises by about 3 ms and 60–110 tokens (measured; see the benchmark).
- A misconception with no written trace anywhere still passes intake. Detection then relies on the
  shakedown checkpoint — keep the cadence on for new bearings.
