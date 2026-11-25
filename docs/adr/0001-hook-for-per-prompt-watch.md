# ADR 0001 — Use a UserPromptSubmit hook for the per-prompt watch

- **Status:** Accepted
- **Date:** 2026-11-25

## Context

The skill must check every prompt against the project's bearing. Skills are loaded on demand: the
model reads a skill's body only when a task matches its description. A skill alone therefore cannot
guarantee a check on every prompt.

Research on multi-turn LLM use shows performance drops when instructions are spread across turns
(Laban et al., 2025) and that drift can be lowered by lightweight goal reminders
(*Drift No More?*, arXiv 2510.07777). See [methods](../methods.md).

## Decision

Ship a Claude Code `UserPromptSubmit` hook (`hooks/watchman.sh`) that, when `.watch/WATCH.md`
exists, prints a compact bearing (Problem, Constraints, Tools, latest Path-log entry) and a one-line
watch instruction. Claude Code adds this output to the model's context.

- Policy on drift: **flag in one line, then continue** (chosen by the maintainer over "stop and ask").
- Output capped at 4,000 characters; Context and Standard are left out to keep it small.
- Logbook text is wrapped in a `<bearing>` block, labelled as data, and stripped of bearing tags.
- Bash + awk only; always exits 0; silent without a logbook; `TRAVELERSWATCH_DISABLE=1` turns it off.

## Consequences

- Every prompt costs up to ~1k tokens of extra context while a logbook exists.
- The hook is Claude Code–specific. Other agents use the two skills and run `/checkwatch` manually.
- The hook reads a file anyone with repo write access can change, so its output is treated as data,
  not instructions (see [SECURITY.md](../../SECURITY.md)).
