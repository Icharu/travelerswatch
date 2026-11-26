# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.2] - 2026-11-26

### Added
- The tale (`docs/tale.md`) in Português (Brasil), Español, 繁體中文, 简体中文, 日本語 and العربية
  (`i18n/<lang>/tale.md`), with a language bar on every version; the translated READMEs now link to
  the tale in their own language.

### Fixed
- The version number is now the same everywhere (plugin manifests, skill metadata,
  `CITATION.cff`, `.zenodo.json`, README badges and citations), so the Zenodo record shows the
  right version. v1.2.1 still reported 1.2.0.

## [1.2.1] - 2026-11-26

Documentation-only release. DOI: 10.5281/zenodo.24548859.

### Added
- Release notes for v1.2.0 (`docs/releases/v1.2.0.md`).

### Changed
- v1.2.0 is cited with the all-versions DOI (10.5281/zenodo.24543183); the "pending" DOI rows were
  removed from the READMEs and `CITATION.cff`.

### Known issues
- The plugin manifests, skills, `CITATION.cff` and `.zenodo.json` in this release still report
  version 1.2.0, so the Zenodo record shows "1.2.0".
- The tale translations were not pushed before the release was published, so they are not part of
  v1.2.1. They are listed under Unreleased.

## [1.2.0] - 2026-11-26

### Added
- Zenodo DOIs in the READMEs and `CITATION.cff`: concept 10.5281/zenodo.24543183, v1.1.0 10.5281/zenodo.24543326, v1.0.0 10.5281/zenodo.24543184.
- **Post-project review** (`/checkwatch` Part C): rebuilds the timeline from the logbook and git
  history, compares original and final bearing, reports unlogged changes, judges the objective and
  accepted risks against evidence, and drafts evidence-tied lessons. The PM chooses *review and
  close* or *review only*; reviews are written to `.watch/reviews/`. See ADR 0005.
- **Checkpoint log** (logbook v1.2): one append-only line per checkpoint (date, SHA, verdict, reason).
- **Closed** bearing status: the watchman stays silent; `/fixwatch` can reopen it as a logged scope change.
- **Human-in-the-loop rule** in `checkwatch` and `fixwatch`: no fully automated sessions for the
  bearing; repetitive work inside the bearing is automated. See ADR 0004.
- `GOVERNANCE.md` (solo-maintained, solo-driven; origin; AI-assistance disclosure), `QUICKSTART.md`,
  `docs/iso-iec-42001.md` (not certified; clause-by-clause map of what TTW covers and does not).
- README: *What it is / what it is not*, *Why human-in-the-loop in project management?*,
  *Positioning*, *Your data*, *Prohibited uses*, *ISO/IEC 42001*, *Citing TTW*.
- CONTRIBUTING: *What led to this project* (research window and references).
- Methods §5 (Koshman & Zubkova 2026; Adamantiadou & Tsironis 2025); tale epilogue.
- Plugin icon (`.claude-plugin/icon.png`, 512×512), README banner (light and dark variants) in every README, and a social
  preview image (`.github/assets/`).
- Eval cases: checkwatch #10 (post-project review), #11 (Checkpoint log); fixwatch #7
  (refuses auto-approval). Hook tests 16–17.

### Changed
- Translations moved to `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING in pt-BR, es, zh-Hant,
  zh-Hans, ja, ar). Links to the old `README.<lang>.md` paths no longer work.

### Licensing
- **The whole repository is now licensed under CC BY-NC 4.0** (`LICENSE`), replacing MIT for code
  and CC BY 4.0 for documentation; `LICENSE-docs` removed. Commercial use needs the maintainer's
  permission. Copies of v1.0.0 (MIT) and v1.1.0 (MIT + CC BY 4.0) keep the licenses they were
  released under.

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

### Licensing
- Dual license from this release: code (`hooks/`, `tests/`, `.sh`, `.py`, `.json`, `.yml`, `.cff`)
  under MIT (`LICENSE`); documentation and skill text (all Markdown files) under CC BY 4.0
  (`LICENSE-docs`). Release 1.0.0 remains MIT in full.

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

[Unreleased]: https://github.com/Icharu/travelerswatch/compare/v1.2.2...HEAD
[1.2.2]: https://github.com/Icharu/travelerswatch/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/Icharu/travelerswatch/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/Icharu/travelerswatch/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/Icharu/travelerswatch/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Icharu/travelerswatch/releases/tag/v1.0.0
