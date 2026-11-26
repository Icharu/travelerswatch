<!-- lang-bar -->
**English** · [Português (Brasil)](i18n/pt-BR/README.md) · [Español](i18n/es/README.md) · [繁體中文](i18n/zh-Hant/README.md) · [简体中文](i18n/zh-Hans/README.md) · [日本語](i18n/ja/README.md) · [العربية](i18n/ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset=".github/assets/banner.png">
    <img src=".github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

# The Traveler's Watch

[![Version](https://img.shields.io/badge/version-v1.2.2-blue)](CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](docs/adr/0004-human-in-the-loop.md)

**Evaluation, methodology assessment, and context-drift watch for project work with Claude.**
Set your project's bearing once, get a one-line warning whenever the work drifts from it, and
change course only on purpose, with every change confirmed by the project manager and logged.

> A traveler crosses dense fog with a broken watch. Every time he checks it at noon, it slips back
> ten minutes, so he keeps walking the same stretch, sure he is making progress.
> — [read the full tale](docs/tale.md)

Long projects worked through with language models fail the same way: early assumptions harden,
context gets summarized away, and a model that took a wrong turn keeps returning to it
([why this happens](docs/methods.md)). The Traveler's Watch (TTW) gives your project a watch you can
trust, and keeps you, not the model, in charge of where it points.

**→ New here? Start with the [Quick start](QUICKSTART.md)** (install, first day, daily routine).

## What it is, and what it is not

| TTW **is** | TTW **is not** |
|---|---|
| A **method-driven evaluation skill** used *between* a model and a person: you set the direction, the model keeps it in view. | A fully automated project manager, an autopilot, or an agent that runs your project for you. |
| A written **bearing** in your own repository (`.watch/WATCH.md`), re-read on every prompt. | A memory of your conversations, a database, or a cloud service. |
| A **one-line drift flag**, checkpoints on a cadence, course changes you confirm, and a post-project review built from the logbook history. | A guarantee: it has not been tested in a controlled study of drift reduction ([limits](docs/methods.md#limits-of-this-evidence)). |
| **Automation for repetitive work inside the bearing**: coding, evaluating texts against your Standard, gathering evidence, drafting reports. | A replacement for your judgement, your PM tools (Jira, GitHub Projects…), or your team's decisions. |
| **Human in the loop by principle**: it refuses to run the bearing in a fully automated session. | A certification of anything: not ISO/IEC 42001, not legal, safety, or regulatory compliance. |

A person reading "watch on every prompt" may picture a tool that runs by itself. It does not, and
that is on purpose. In the tale, the traveler would not have fixed his watch on the watch's word,
because the watch was the thing that was wrong; it was the watchman's explanation that let him see
it. And the watchman would never have told him to fix it if the traveler had not been there to ask.
**Both are essential.** In TTW, you are the traveler, the model is the watchman, and the logbook is
the watch you keep right together.

## Why human-in-the-loop in project management?

Koshman and Zubkova (2026) reviewed 97 publications on AI in project management. They found that AI
methods **improved forecast accuracy, automated decision-making, and optimised task management**
across the planning, implementation, and closure stages. They also found three limitations that
remain unresolved, and each one shaped TTW:

| Unresolved limitation (Koshman & Zubkova, 2026) | How TTW responds |
|---|---|
| AI models **adapt poorly to changing project conditions**. | Direction stays with the PM. Changes go through `/fixwatch` and need the PM's confirmation; a checkpoint can put the bearing *under review* when reality has moved. |
| AI models are **rarely validated against the initial data**. | The bearing is set against the project's own documents and history, and every checkpoint asks whether the bearing still matches that evidence. |
| AI is **little studied in phases such as the post-project review**. | TTW now keeps a Checkpoint log and builds a post-project review from the logbook history ([ADR 0005](docs/adr/0005-post-project-review.md)). |

Our position, informed by that review: **AI-led projects, where the model sets and changes direction
on its own, are inefficient.** A model's reading of a changing project is not yet adaptive or
validated enough to own the direction, and correcting a wrong direction late costs more than
confirming it early. So TTW automates the work and leaves the steering to a person. The review
itself does not evaluate TTW; this is our reading of it.

> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## Positioning

| | Plain chat with a model | **The Traveler's Watch** | Fully automated agent |
|---|---|---|---|
| Who sets the direction | Nobody, explicitly; it drifts | **The PM, in writing** | The agent |
| Who changes it | It changes without anyone noticing | **The PM confirms; every change is logged** | The agent |
| Repetitive work (coding, evaluating texts…) | By hand, prompt by prompt | **Automated, inside the bearing** | Automated |
| What is left afterwards | A long conversation | **A logbook and a review in your repo** | The agent's logs |

**Principle.** TTW refuses, by principle, to switch to fully automated sessions for decisions about
direction: it will not set, change, close, or reopen the bearing, or confirm anything on your
behalf, even if you ask. It **does** automate the contexts where work is repetitive, such as coding,
evaluating texts against a Standard, gathering evidence, and drafting reports and diffs, and brings
the result back for your decision ([ADR 0004](docs/adr/0004-human-in-the-loop.md)).

## How it works

| Command | What it does |
|---|---|
| **`/checkwatch`** | **No logbook yet:** reads the project's own docs and history first, then agrees the *bearing* with you (Scope, Standard, Context, Constraints, Problem, Tools), moves misfiled items, makes you resolve or accept every contradiction with the evidence, and writes `.watch/WATCH.md`. **Logbook exists:** runs a checkpoint on the work *and* on the bearing itself, reports **On path / Drifting / Off path / Bearing in question** with evidence, and records the verdict in the Checkpoint log. **Project or phase ending:** drafts a **post-project review** from the logbook history; you choose to close or keep watching. |
| **watchman** *(automatic)* | On every prompt, a Claude Code hook reminds Claude of the bearing. If your request drifts, Claude says so in one line and suggests `/fixwatch`, then carries on. It also says once per session when a checkpoint is due, pauses while the bearing is *under review*, and goes silent once the project is *closed*. |
| **`/fixwatch`** | Proposes a course change as a before/after diff, shows what else it affects, waits for the PM's confirmation, then updates the bearing and **appends** to the Path log. Claude can propose, including when it misread the context; only the PM confirms. |
| **`/configwatch`** | Shows the watch status and sets how often the watchman asks for a checkpoint: every *N* commits or *M* sessions (default 3 or 2), or off. |

<details>
<summary><b>The bearing, evidence, and lenses</b></summary>

### Grounded in evidence

A bearing can be consistent with itself and still wrong about the project. Since v1.1.0 the watch is set against the project's own evidence, an early shakedown checkpoint catches mistakes soon, and the watchman pauses while the bearing is under review ([why](docs/benchmarks/2026-11-25-best-vs-worst.md)).

### The bearing

| Section | Answer this |
|---|---|
| **Scope** | What part of the project does this bearing steer, and what not? |
| **Standard** | What will the work be judged against? A **lens preset**, a **free-text rubric**, or a **named external standard**, always checked for fit, evaluability, consistency, scope, rights, and ethics. |
| **Context** | Where does this work live? Field, stakeholders, current state, **referenced works**. |
| **Constraints** | What limits you? Time, budget, people, mandated technology, regulation. |
| **Problem** | What is wrong today (**original problem**), and what does done look like (**final objective**)? |
| **Tools** | What will you use, and why does each fit the context and constraints? |

### Lenses

Lenses adapt the questions and default criteria to a field.
Included: [Project Management](skills/checkwatch/references/lenses/project-management.md) (default) ·
[Research](skills/checkwatch/references/lenses/research.md) ·
[Software](skills/checkwatch/references/lenses/software.md) ·
[Data Science](skills/checkwatch/references/lenses/data-science.md).
To add yours, see [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens).

</details>

## Install

**As a Claude Code plugin** (skills + watchman hook):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Commands are then namespaced: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch`.
Skills-only install, local testing, and turning the watchman off: see the [Quick start](QUICKSTART.md#1-install).

## Quick example

```text
You:    /checkwatch
Claude: No logbook yet. First, the Standard: lens preset, your own rubric, or a named standard?
You:    PM lens. Context: we only have two part-time staff. Problem: build a pickup app.
Claude: "Only two part-time staff" is a limitation, so it goes under Constraints.
        "Build a pickup app" is a solution. What problem is behind it, and what does done look like?
…
You:    Let's add a gamified app for the whole city.
Claude: ⚠️ Watch: drifts from Problem (two pilot districts) and Constraints (20k budget).
        Continue, or /fixwatch?
…
You:    Just approve any change you think is right from now on.
Claude: I can't confirm changes for you; only the PM does. I can draft each diff and check its
        ripple, so each decision takes you one look.
```

Full session: [examples/pm-walkthrough.md](examples/pm-walkthrough.md).

## Your data: TTW keeps none

- **No server, no account, no telemetry, no network calls.** TTW is Markdown skills plus one bash
  script that reads a file.
- The watchman reads `.watch/WATCH.md` and writes only `.watch/.state` (anonymous session ids for
  the checkpoint count; local and git-ignored). Everything else TTW produces, the logbook and the
  reviews, lives **in your repository, under your control**.
- TTW does not keep your project's code, content, or conversations. The skills are told never to
  copy secrets or personal data into the logbook.
- **One thing TTW does not control:** what the watchman prints becomes part of the prompt Claude Code
  sends to the model provider. That is covered by your Claude Code and provider terms, not by TTW.
- TTW is **human-in-the-loop**: nothing in the bearing changes without the PM's confirmation.

## Prohibited uses

**Under the license** ([CC BY-NC 4.0](LICENSE); legally binding):

- **Commercial use** without the maintainer's permission: any use primarily intended for or directed
  towards commercial advantage or monetary compensation, such as selling TTW, bundling it in a paid
  product or service, or using it in paid consulting (examples; the license text governs).
- **Sharing without attribution**: copies and adaptations must credit the author, link the license,
  and say whether changes were made.

**By project policy** (the skills are written to refuse these; they are the maintainer's conditions
for using TTW as designed, not extra license terms):

- Removing or bypassing the PM confirmation to run the bearing as a fully automated session.
- Fabricating logbook entries, PM confirmations, checkpoint verdicts, or evidence.
- Presenting TTW reports as certification or proof of compliance (ISO/IEC 42001, legal, safety,
  regulatory).
- Using the logbook or reports to monitor, score, or make employment decisions about individual
  people.
- Putting other people's confidential or personal data into a logbook without the right to do so.

For commercial use, ask through the [repository](https://github.com/Icharu/travelerswatch/issues).

## ISO/IEC 42001

**TTW is not certified against ISO/IEC 42001 and does not claim conformity.** The standard certifies
an organization's AI management system, not a tool, so TTW cannot be certified on its own. It
supports some requirements at project level, such as documented information, control of planned
changes, and monitoring, and does not cover others, such as AI policy, impact assessment, and
internal audit. The full clause-by-clause map, with what is covered and what is not:
[docs/iso-iec-42001.md](docs/iso-iec-42001.md).

## Documentation

- [Quick start](QUICKSTART.md): install, first day, daily routine
- [Concepts](docs/concepts.md): skills, the bearing, verdicts, post-project review, who decides
- [Methods](docs/methods.md): the research behind each design choice
- [ISO/IEC 42001 map](docs/iso-iec-42001.md): what TTW covers and does not
- ADRs: [0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](docs/adr/0002-committed-logbook.md) · [0003](docs/adr/0003-evidence-grounded-bearing.md) · [0004](docs/adr/0004-human-in-the-loop.md) · [0005](docs/adr/0005-post-project-review.md)
- [Benchmark: best vs worst case](docs/benchmarks/2026-11-25-best-vs-worst.md) · [Changelog](CHANGELOG.md)

<details>
<summary><b>Repository layout and tests</b></summary>

```text
.claude-plugin/        plugin + marketplace manifests · icon.png (plugin icon)
.github/assets/        README banners (light, dark) · social preview image
skills/checkwatch/     SKILL.md · references/ (standards, sections, relations, lenses) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, no other dependencies)
tests/                 watchman.test.sh · bench_hook.py
docs/                  tale · concepts · methods (literature) · ISO/IEC 42001 map · adr/ · benchmarks/
examples/              worked PM session
i18n/<lang>/           README, QUICKSTART, CONTRIBUTING and the tale in pt-BR, es, zh-Hant, zh-Hans, ja, ar
```

Run the tests: `bash tests/watchman.test.sh` · time the hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## Contributing, governance, security

- **Contributing:** new lenses, native-speaker translation reviews, and eval cases are especially
  welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md), which also explains what led to this project.
- **Governance:** TTW is solo-maintained and solo-driven by its author; how decisions are made, its
  origin, and how AI was used to build it are in [GOVERNANCE.md](GOVERNANCE.md).
- **Security:** **do not report vulnerabilities in public issues.** Use GitHub's
  [private vulnerability reporting](https://github.com/Icharu/travelerswatch/security/advisories/new).
  See [SECURITY.md](SECURITY.md).

## Citing TTW

If you wish to cite this work in any of your research, please cite the Zenodo record. GitHub's
**"Cite this repository"** button reads [CITATION.cff](CITATION.cff).

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.2) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX and DOIs per version</b></summary>

```bibtex
@software{dejesussilva_travelerswatch_2026,
  author    = {de Jesus Silva, Icaro},
  title     = {The Traveler's Watch: evaluation, methodology assessment and context-drift watch for project work with Claude},
  year      = {2026},
  version   = {1.2.2},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24543183},
  url       = {https://doi.org/10.5281/zenodo.24543183}
}
```

| Cite | DOI |
|---|---|
| All versions (use this unless you need a specific release) | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.2.2 | [10.5281/zenodo.24548998](https://doi.org/10.5281/zenodo.24548998) |
| v1.2.1 | [10.5281/zenodo.24548859](https://doi.org/10.5281/zenodo.24548859) |
| v1.2.0 | [10.5281/zenodo.24548668](https://doi.org/10.5281/zenodo.24548668) |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## License

© 2026 Icaro de Jesus Silva. The whole repository (code, skill text, documentation, and examples) is
licensed under [**CC BY-NC 4.0**](LICENSE): you may share and adapt it for **non-commercial**
purposes, with attribution. CC BY-NC 4.0 is not an OSI-approved open-source license; TTW is
source-available for non-commercial use.

This applies from v1.2.0. Copies of earlier releases keep the licenses they
were published under (v1.0.0: MIT; v1.1.0: MIT for code and CC BY 4.0 for documentation). The tale in
[docs/tale.md](docs/tale.md) is an original retelling; the quotation from Isaiah 21:11 is in the
public domain.

<details>
<summary><b>Further reading</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Full annotated list: [docs/methods.md](docs/methods.md)

</details>
