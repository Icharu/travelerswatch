# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-25

Motivated by a [best-vs-worst benchmark](docs/benchmarks/2026-11-25-best-vs-worst.md) on a live
project: a plausible but wrong bearing passed every v1.0.0 intake check, and the watchman then
steered the work the wrong way. See [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md).

### Added
- **Evidence scan** at intake (`references/evidence.md`): a one-line Scope, then README, docs,
  ADRs, evaluations, and git history are read before the Standard; sections start as drafts from
  evidence; every PM-vs-evidence contradiction must be resolved or explicitly accepted.
- **Objective anchor** rule: one Standard criterion must measure the Final objective; opt-out is
  explicit and recorded.
- **Two-direction checkpoint** (work vs bearing, bearing vs reality) and the verdict
  **Bearing in question**.
- **Status** section in the logbook: bearing `confirmed` / `under review`, checkpoint cadence, last
  checkpoint. *Under review* pauses drift flags until `/fixwatch` closes it.
- **`/configwatch`** skill to set the checkpoint cadence (default `every 3 commits or 2 sessions`).
- Watchman: shakedown nudge for `/checkwatch` at most once per session (local `.watch/.state`);
  injects **Scope** and a **limits & accepted risks** digest; strips `*( … )*` intake annotations.
- `fixwatch`: *evidence contradiction* trigger; closing a review with or without changes.
- Synthetic eval fixtures and 13 new eval cases (checkwatch 9, fixwatch 6, configwatch 4 in total);
  transcripts of headless runs.
- `tests/bench_hook.py` to time the hook per prompt; benchmark write-up with v1.0.0 vs v1.1.0 timings.
- ADR 0003.

### Changed
- Intake order: Scope → evidence → Standard → sections → relations/evidence conflicts/anchor.
- Fit check judges the Standard against the Scope and the evidence, not the lens name alone.
- Logbook template v1.1 (adds Status, Scope, *Evidence scanned*; items written without provenance notes).
- Hook parses the logbook in a single `awk` pass and uses bash built-ins (bash ≥ 3.2); ≈ 10–11 ms
  per prompt with cadence and git counting, vs ≈ 8 ms in v1.0.0.

### Compatibility
- v1.0 logbooks keep working unchanged (no Status → no nudges). `/checkwatch` or `/configwatch`
  offers to add the Status section.

## [1.0.0] - 2026-11-25

### Added
- `checkwatch` skill: intake (Standard with three modes and a six-point boundary check; Context,
  Constraints, Problem, Tools with a misfiling pass; relations and tensions) and checkpoint
  (On path / Drifting / Off path report with evidence).
- `fixwatch` skill: proposes a course change as a diff, shows the ripple, waits for PM
  confirmation, and appends to the Path log.
- Watchman `UserPromptSubmit` hook (`hooks/watchman.sh`): compact bearing on every prompt, capped at
  4,000 characters, injection-guarded, and silent without a logbook. Disable with `TRAVELERSWATCH_DISABLE=1`.
- Logbook template `.watch/WATCH.md`.
- Lenses: Project Management (default), Research, Software, Data Science.
- Eval suites for both skills (skill-creator `evals.json` format).
- Documentation: tale, concepts, methods (annotated literature), ADRs 0001–0002, worked PM example.
- READMEs in English, Português (Brasil), Español, 繁體中文, 简体中文, 日本語, العربية.
- SECURITY.md with private vulnerability reporting and a best-effort response table; CONTRIBUTING.md;
  CITATION.cff; .zenodo.json.

[Unreleased]: https://github.com/Icharu/travelerswatch/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/Icharu/travelerswatch/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Icharu/travelerswatch/releases/tag/v1.0.0
