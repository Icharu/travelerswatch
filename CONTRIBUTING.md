<!-- lang-bar -->
**English** · [Português (Brasil)](i18n/pt-BR/CONTRIBUTING.md) · [Español](i18n/es/CONTRIBUTING.md) · [繁體中文](i18n/zh-Hant/CONTRIBUTING.md) · [简体中文](i18n/zh-Hans/CONTRIBUTING.md) · [日本語](i18n/ja/CONTRIBUTING.md) · [العربية](i18n/ar/CONTRIBUTING.md)

# Contributing to The Traveler's Watch

Thank you for helping keep travelers on their path. Contributions of every size are welcome.

## What led to this project

TTW encourages both users and contributors to understand what led to it before changing it. The
design rests on roughly **five years of research (2021–2026)** on how language models drift in long
work and on how AI is changing project management, plus one earlier study on scope creep.

Research on how AI works and is used in the modern world is **interdisciplinary** in nature
(Koshman & Zubkova, 2026), so contributions from any field are welcome. Two reviews frame TTW's
place in that research:

- **What AI already does well in project management.** Adamantiadou and Tsironis (2025) found that
  machine learning, deep learning, and hybrid models have significantly expanded what project
  management can do, improving **cost estimation, schedule forecasting, and risk analysis**. TTW
  takes that seriously: it automates repetitive work inside the bearing.
  *Transparency note: we cite this finding as it is reported in Koshman & Zubkova (2026); we checked
  the original article's details through its DOI.*
- **What is still unresolved.** Koshman and Zubkova (2026) reviewed 97 publications and found that AI
  models adapt poorly to changing project conditions, are rarely validated against the initial data,
  and are little studied in phases such as the post-project review. TTW is built around those gaps:
  the PM keeps the direction, the bearing is checked against evidence, and the logbook supports a
  post-project review.

| Year | Reference | Why it matters here |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | Unauthorized change hurts projects → every course change is confirmed and logged |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | Models use the edges of a long context best → a short bearing next to each prompt |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM judges need explicit criteria → the Standard is set before any verdict |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | Models take wrong turns and do not recover → the bearing is set up front |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | Reminders lower drift → the watchman on every prompt |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | AI improves estimation, forecasting, risk analysis → automate the repetitive work |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | Adaptability, validation, and post-project review are unresolved → human in the loop |

The full annotated list, with the design consequence of each source, is in
[docs/methods.md](docs/methods.md). How the project started and who decides is in
[GOVERNANCE.md](GOVERNANCE.md).

<details>
<summary><b>References in full</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- Other sources: [docs/methods.md](docs/methods.md).

</details>

## Ways to contribute

| Contribution | Where |
|---|---|
| A **lens** for a new field (e.g. events, construction, nonprofit programs, product design) | `skills/checkwatch/references/lenses/` |
| A **translation review** by a native speaker | `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING) |
| A new **eval case** (a prompt plus the behaviour you expect) | `skills/<skill>/evals/evals.json` |
| A **bug report** or idea | [Issues](https://github.com/Icharu/travelerswatch/issues). Use the templates. |
| A **security problem** | **Not** in issues. See [SECURITY.md](SECURITY.md). |

## Adding a lens

1. Copy an existing lens (e.g. `project-management.md`) to `lenses/<field>.md`.
2. Keep the same four headings so the skill can use any lens the same way:
   - **How the sections read in this field**: a table rephrasing Context, Constraints, Problem, Tools
   - **Default criteria**: 4–8 *observable* criteria (see `references/standards.md`)
   - **Drift signals**: what wandering off the path looks like in this field
   - **Typical tools**
3. Write criteria **in your own words**. Do not paste text from paid or copyrighted standards; name
   them and reference sections only.
4. Add the lens to the list in `skills/checkwatch/SKILL.md` (step A1) and in the README's *Lenses*
   section.
5. Add at least one eval case in `skills/checkwatch/evals/evals.json` that uses the lens.

## Changing the skills

- Keep each `SKILL.md` short and decision-oriented; put detail in `references/`.
- Do not weaken the core rules ([GOVERNANCE.md](GOVERNANCE.md#how-decisions-are-made)): **only the
  PM confirms** a course change, closure, or accepted contradiction; **the Path log and the
  Checkpoint log are append-only**; **no fully automated sessions** for the bearing
  ([ADR 0004](docs/adr/0004-human-in-the-loop.md)); **no data kept** outside the user's repository.
- Use only standard Agent Skills frontmatter (`name`, `description`, `license`, `metadata`) so the
  skills stay portable.
- Explain behaviour changes in an ADR under `docs/adr/` when they change a design decision.

## Changing the hook

- Bash (≥ 3.2, for macOS) and awk only; git is optional. Prefer bash built-ins over extra
  processes; the logbook is parsed in a single `awk` pass.
- It must always exit 0, stay silent without a logbook or with a `closed` bearing, keep the output
  capped, make no network calls, and write nothing but `.watch/.state`.
- **Write the failing test first** in `tests/watchman.test.sh`, then make it pass, and measure the
  per-prompt time before and after:

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## Changing the logbook format

The hook parses exact labels: `## Status`, `- **Bearing:**` (`confirmed` / `under review …` /
`closed …`), `- **Checkpoint cadence:**` (`every N commits or M sessions` / `off`),
`- **Last checkpoint:** <date> @ <sha>`, `**Boundary notes:**`, Relations lines containing
"accepted", and the `## Path log` heading. `## Checkpoint log` is read by the skills only. Change
them only together with the hook, the template (`skills/checkwatch/assets/WATCH.md`), the skills,
and the tests.

## Translations

The English files at the root (`README.md`, `QUICKSTART.md`, `CONTRIBUTING.md`) are canonical.
Translations are grouped by language under `i18n/<lang>/`, so the root stays uncluttered. When you
change an English file, note in the pull request which translations are now out of date.
Translators: keep the language bar, links (relative to `i18n/<lang>/`, e.g. `../../docs/tale.md`),
badges, commands, and shell code blocks identical (the dialogue in *Quick example* may be
translated). Update the `Translated from` note at the top of the file. Arabic: keep prose inside
`<div dir="rtl">` and code blocks outside it.

## Pull requests

1. Fork, then create a branch: `feat/<thing>`, `fix/<thing>`, `docs/<thing>`, or `lens/<field>`.
2. Keep each pull request focused on one change.
3. Run `bash tests/watchman.test.sh` and `claude plugin validate .` if you have Claude Code.
4. Add an entry under **Unreleased** in [CHANGELOG.md](CHANGELOG.md).
5. Use [Conventional Commits](https://www.conventionalcommits.org/) messages (`feat:`, `fix:`, `docs:`).

By contributing, you agree that your contributions are licensed under the same terms as the rest of
the repository: [CC BY-NC 4.0](LICENSE).
