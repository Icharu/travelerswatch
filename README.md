<!-- lang-bar -->
**English** · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [العربية](README.ar.md)

# The Traveler's Watch

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending%20(Zenodo)-lightgrey)](CITATION.cff)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**Evaluation, methodology assessment, and context-drift watch for project work with Claude.**
Set your project's bearing once, get a one-line warning whenever the work drifts from it, and
change course only on purpose, with every change confirmed by the project manager and logged.

> A traveler crosses dense fog with a broken watch. Every time he checks it at noon, it slips back
> ten minutes, so he keeps walking the same stretch, sure he is making progress.
> — [read the full tale](docs/tale.md)

Long projects worked through with language models fail the same way: early assumptions harden,
context gets summarized away, and a model that took a wrong turn keeps returning to it
([why this happens](docs/methods.md)). The Traveler's Watch gives your project a watch you can trust.

## How it works

| Command | What it does |
|---|---|
| **`/checkwatch`** | **No logbook yet:** reads the project's own docs and history first, then agrees the *bearing* with you (Scope, Standard, Context, Constraints, Problem, Tools), moves misfiled items, makes you resolve or accept every contradiction with the evidence, and writes `.watch/WATCH.md`. **Logbook exists:** runs a checkpoint on the work *and* on the bearing itself, and reports **On path / Drifting / Off path / Bearing in question** with evidence. |
| **watchman** *(automatic)* | On every prompt, a Claude Code hook reminds Claude of the bearing. If your request drifts, Claude says so in one line and suggests `/fixwatch`, then carries on. It also says once per session when a checkpoint is due, and pauses while the bearing is *under review*. |
| **`/fixwatch`** | Proposes a course change as a before/after diff, shows what else it affects, waits for the PM's confirmation, then updates the bearing and **appends** to the Path log. Claude can propose, including when it misread the context; only the PM confirms. |
| **`/configwatch`** | Shows the watch status and sets how often the watchman asks for a checkpoint: every *N* commits or *M* sessions (default 3 or 2), or off. |

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

## Install

**As a Claude Code plugin** (skills + watchman hook):

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

Commands are then namespaced: `/travelerswatch:checkwatch`, `/travelerswatch:fixwatch`, `/travelerswatch:configwatch`.

**Skills only** (Claude Code or any agent that reads [Agent Skills](https://agentskills.io/); no hook):

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/
```

Commands are then `/checkwatch`, `/fixwatch` and `/configwatch`. Without the hook, run `/checkwatch` at the start
of each working session.

**Try it locally without installing:** `claude --plugin-dir ./travelerswatch`

**Turn the watchman off temporarily:** `export TRAVELERSWATCH_DISABLE=1`

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
```

Full session: [examples/pm-walkthrough.md](examples/pm-walkthrough.md).

## Repository layout

```text
.claude-plugin/        plugin + marketplace manifests
skills/checkwatch/     SKILL.md · references/ (standards, sections, relations, lenses) · assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh (bash + awk, no other dependencies)
tests/                 watchman.test.sh
docs/                  tale · concepts · methods (literature) · adr/
examples/              worked PM session
```

Run the tests: `bash tests/watchman.test.sh` · time the hook: `python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

## Documentation

- [Concepts](docs/concepts.md): skills, the bearing, verdicts, who decides
- [Methods](docs/methods.md): the research behind each design choice
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md) · [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)
- [Benchmark: best vs worst case](docs/benchmarks/2026-11-25-best-vs-worst.md): what v1.0.0 missed, what v1.1.0 fixed, hook time per prompt
- [Changelog](CHANGELOG.md)

## Contributing

Contributions are welcome, especially **new lenses** for other fields, translations reviewed by
native speakers, and new eval cases. Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull
request.

## Security

**Do not report vulnerabilities in public issues.** Use GitHub's
[private vulnerability reporting](https://github.com/Icharu/travelerswatch/security/advisories/new)
(the **Security** tab, then **Report a vulnerability**). Response times are best-effort and depend on
severity. See [SECURITY.md](SECURITY.md) for the scope, the response table, and what to do while
you wait.

## Citation

If you use The Traveler's Watch in research or teaching, please cite it. GitHub's
**"Cite this repository"** button reads [CITATION.cff](CITATION.cff). A Zenodo DOI will be
added here once v1.0.0 is released.

## License

[MIT](LICENSE) © 2026 Icaro de Jesus Silva. The tale in [docs/tale.md](docs/tale.md) is an
original retelling; the quotation from Isaiah 21:11 is in the public domain.

## Further reading

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- Full annotated list: [docs/methods.md](docs/methods.md)
