# Governance

This document says who makes The Traveler's Watch (TTW), how decisions are made, where the project
came from, and how AI was used to build it. It describes how things actually work today, not how
they might work later.

## At a glance

| | |
|---|---|
| **Maintainer and author** | Icaro de Jesus Silva ([Icharu](https://github.com/Icharu) on GitHub) |
| **Model** | **Solo-maintained** and **solo-driven** (definitions below) |
| **Started** | 2026-11-25, first public release v1.0.0 the same day |
| **License** | [CC BY-NC 4.0](LICENSE) from the first release after v1.1.0 (earlier releases keep their licenses) |
| **AI assistance** | Built with Claude Code (Claude Opus 5.5) as a coding and writing assistant; disclosed below |
| **Funding / SLA** | Maintained in spare time; there is no service-level agreement |

## Solo-maintained and solo-driven

Both terms apply, and they mean different things:

- **Solo-maintained**: one person reviews issues and pull requests, keeps the tests and evals
  passing, answers security reports ([SECURITY.md](SECURITY.md)), and cuts releases. There is no
  second maintainer and no team.
- **Solo-driven**: one person decides where the project goes: what TTW is and is not, which
  proposals are accepted, and when a release is made. Contributors propose; the maintainer decides.

This mirrors TTW's own rule: Claude may propose a course change, but only the project manager
confirms it. Here, anyone may propose; the maintainer confirms.

## Origin

- **The problem.** Long projects worked through with language models drift: early assumptions
  harden, context gets summarized away, and a model that took a wrong turn keeps returning to it.
  The research behind that observation is in [docs/methods.md](docs/methods.md).
- **The metaphor.** The project is built around an original retelling of a traveler with a
  broken watch and a watchman on the wall ([docs/tale.md](docs/tale.md)). The watchman's line,
  *"Watchman, what of the night?"*, is from Isaiah 21:11 (public domain).
- **The first releases.** v1.0.0 set the bearing from the PM's answers alone. A best-vs-worst
  benchmark on a live academic project (anonymized) showed that a plausible but wrong bearing
  passed every check, which led to v1.1.0 and its evidence-grounded intake
  ([benchmark](docs/benchmarks/2026-11-25-best-vs-worst.md), [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)).
- **The research window.** The context that led to TTW is a roughly five-year window of research
  on AI in project management and on how language models drift. It is summarized in
  [CONTRIBUTING.md](CONTRIBUTING.md#what-led-to-this-project).

## How decisions are made

| Decision | How |
|---|---|
| Bug fix, eval case, translation fix | Pull request → maintainer review → merge |
| New lens | [Lens proposal](https://github.com/Icharu/travelerswatch/issues/new/choose) issue → pull request |
| Change to a design decision (skills, hook, logbook format) | Issue first, then an ADR in [`docs/adr/`](docs/adr/) with the pull request |
| Release | The maintainer tags it (Semantic Versioning); Zenodo archives it with its own DOI |
| Security report | Private advisory only ([SECURITY.md](SECURITY.md)) |

**Rules no proposal can remove.** These define the project. A change that weakens them will not be
merged:

1. Only the PM confirms a course change, a closure, or an accepted contradiction.
2. The Path log and the Checkpoint log are append-only.
3. TTW never runs the bearing in a fully automated session ([ADR 0004](docs/adr/0004-human-in-the-loop.md)).
4. TTW keeps no data outside the user's own repository: no server, no account, no telemetry.

## How AI was used to build TTW

Being open about this is part of what TTW asks of its users.

- Most commits up to v1.1.0 were written with **Claude Code (Claude Opus 5.5)** and carry a
  `Co-Authored-By: Claude` trailer, so `git log` shows exactly which ones.
- The maintainer set the direction, chose what to build, ran the benchmark, and merged every
  pull request. Claude drafted code, tests, and text inside that direction. This is the same
  split TTW describes: repetitive work automated, direction kept by a person.
- In the v1.0.0 benchmark the same model played the PM and the skill. That bias is stated in the
  [benchmark](docs/benchmarks/2026-11-25-best-vs-worst.md) itself.
- The translated READMEs are machine-assisted, and each one says so at the top.

## Continuity

There is one maintainer, so there is a real risk that the project goes quiet. If that happens:
the license allows anyone to fork and keep using TTW for non-commercial purposes, with attribution;
every release is archived on Zenodo ([10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183));
and TTW keeps nothing outside your repository, so your logbooks stay readable Markdown with or
without the tool.

## AI management standards

TTW is **not** certified against ISO/IEC 42001 and does not claim conformity. What it does and does
not cover is mapped, clause by clause, in [docs/iso-iec-42001.md](docs/iso-iec-42001.md).

## Changes to this document

Changes to governance are made by the maintainer, recorded in [CHANGELOG.md](CHANGELOG.md), and
visible in git history.
