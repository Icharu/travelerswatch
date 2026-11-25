# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[Unreleased]: https://github.com/Icharu/travelerswatch/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Icharu/travelerswatch/releases/tag/v1.0.0
