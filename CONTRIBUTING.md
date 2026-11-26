<!-- lang-bar -->
**English** · [Português (Brasil)](i18n/pt-BR/CONTRIBUTING.md) · [Español](i18n/es/CONTRIBUTING.md) · [繁體中文](i18n/zh-Hant/CONTRIBUTING.md) · [简体中文](i18n/zh-Hans/CONTRIBUTING.md) · [日本語](i18n/ja/CONTRIBUTING.md) · [العربية](i18n/ar/CONTRIBUTING.md)

# Contributing to The Traveler's Watch

Thank you for helping keep travelers on their path. Contributions of every size are welcome.

## What led to this project

TTW encourages both users and contributors to understand what led to it before changing it. The
design draws on literature published 2020–2026: studies of how language models drift in long work,
reviews of how AI is changing project management, and one study on scope creep.

Koshman and Zubkova (2026) describe research on how AI works and is used in the modern world as
**interdisciplinary** in nature, so contributions from any field are welcome. Two reviews frame
TTW's place in that research:

- **What AI already does well in project management.** Adamantiadou and Tsironis (2025) reviewed 97
  peer-reviewed studies (2011–2024). Their abstract reports that machine learning, deep learning,
  and hybrid models have shown potential to enhance project management, notably **cost estimation,
  duration forecasting, and risk assessment**. TTW takes that seriously: it automates repetitive
  work inside the bearing.
- **What is still unresolved.** The same review, as summarized by Koshman and Zubkova (2026),
  reports that AI models adapt insufficiently to changing project conditions, have limited
  validation against the initial data, and are little researched in phases such as the post-project
  review. TTW is built around those gaps: the PM keeps the direction, the bearing is checked against
  evidence, and the logbook supports a post-project review.

*Source note (what was read):* Koshman & Zubkova (2026): full text. Adamantiadou & Tsironis (2025):
read through Koshman & Zubkova's summary and through the abstract and bibliographic metadata of its
DOI record; the full text was not read. Earlier versions of this file credited the 97-publication
review to Koshman & Zubkova; that was an attribution error, corrected in v1.2.3.

| Year | Reference | Why it matters here |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | Unauthorized change hurts projects → every course change is confirmed and logged |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | Models use the edges of a long context best → a short bearing next to each prompt |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM judges need explicit criteria → the Standard is set before any verdict |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | Models take wrong turns and do not recover → the bearing is set up front |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | Reminders lower drift → the watchman on every prompt |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | Review of 97 studies: AI shows potential in estimation, forecasting, and risk; adaptability, validation, and late phases unresolved → automate repetitive work, keep a human in the loop |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | Review of 21 publications (2021–2025) and of AI tools; summarizes the 97-study review; interdisciplinary framing → human in the loop, contributions from any field |

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
| A **translation review** by a native speaker | `i18n/<lang>/` (README, QUICKSTART, CONTRIBUTING, tale) |
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

The English files (`README.md`, `QUICKSTART.md`, `CONTRIBUTING.md` at the root, and `docs/tale.md`) are canonical.
Translations are grouped by language under `i18n/<lang>/`, so the root stays uncluttered. When you
change an English file, note in the pull request which translations are now out of date.
Translators: keep the language bar, links (relative to `i18n/<lang>/`, e.g. `../../docs/methods.md`),
badges, commands, and shell code blocks identical (the dialogue in *Quick example* may be
translated). Update the `Translated from` note at the top of the file. Arabic: keep prose inside
`<div dir="rtl">` and code blocks outside it.

**Keep the claim type.** Every sentence about TTW is a *design intent* ("is designed to", "the skill
instructs Claude to"), a *mechanism* ("the hook does X", checkable in a file), or a *result* ("in
<test>, <number>"). A translation must keep the same type: check the verb, not only the noun. Keep
the same sources and numbers as the English, keep author–year citations and original titles
untranslated, and add no local claims or sources. Spanish uses neutral international Spanish
(impersonal *se* or *usted*). zh-Hans and zh-Hant are localized separately, never converted
character by character.

| English | pt-BR | es | zh-Hans | zh-Hant | ja | ar |
|---|---|---|---|---|---|---|
| is designed to | foi projetado para | está diseñado para | 旨在 | 旨在 | 〜を目的として設計されている | صُمّم لـ |
| the skill instructs Claude to | a skill instrui o Claude a | la skill indica a Claude que | 技能指示 Claude | 技能指示 Claude | スキルは Claude に〜するよう指示する | توجّه المهارةُ Claude إلى |
| tested by evals, not enforced by code | testado por evals, não imposto por código | probado con evals, no impuesto por código | 由评测检验，而非由代码强制 | 由評測檢驗，而非由程式碼強制 | eval で検証されており、コードで強制されてはいない | تُختبَر بالتقييمات ولا تفرضها الشيفرة |
| may / can | pode | puede | 可能 | 可能 | 〜可能性がある | قد |
| according to | segundo | según | 据 | 據 | 〜によれば | وفقًا لـ |
| as summarized by | conforme resumido por | según el resumen de | 据…的综述 | 據…的回顧 | 〜の要約による | كما لخّصه |
| design premise | premissa de projeto | premisa de diseño | 设计前提 | 設計前提 | 設計上の前提 | فرضية التصميم |
| guarantees | *avoid*: foi projetado para | *avoid*: está diseñado para | *avoid*: 旨在 | *avoid*: 旨在 | *avoid*: 〜設計されている | *avoid*: صُمّم لـ |
| always (rules only) | sempre | siempre | 始终 | 始終 | 必ず | دائمًا |
| significant (statistical only) | significativo | significativo | 显著 | 顯著 | 有意 | دالّ إحصائيًا |
| substantial (non-statistical) | substancial | sustancial | 较大 | 較大 | 大きな | كبير |
| evidence | evidência | evidencia | 证据 | 證據 | 根拠 | الأدلة |
| indicates (not "proves") | indica | indica | 表明 | 顯示 | 示唆する | تشير إلى |
| efficient | eficiente | eficiente | 高效 | 高效 | 効率的 | ذو كفاءة |
| effective | eficaz | eficaz | 有效 | 有效 | 効果的 | فعّال |
| drift | desvio | desvío | 漂移 | 偏移 | ずれ | الانحراف |
| bearing | rumo | rumbo | 航向 | 航向 | 針路 | المسار |
| human in the loop | humano no circuito | humano en el circuito | 人在回路中 | 人在迴路中 | ヒューマン・イン・ザ・ループ | الإنسان ضمن الحلقة |

The glossary is machine-assisted; native-speaker corrections are welcome.

## Pull requests

1. Fork, then create a branch: `feat/<thing>`, `fix/<thing>`, `docs/<thing>`, or `lens/<field>`.
2. Keep each pull request focused on one change.
3. Run `bash tests/watchman.test.sh` and `claude plugin validate .` if you have Claude Code.
4. Add an entry under **Unreleased** in [CHANGELOG.md](CHANGELOG.md).
5. Use [Conventional Commits](https://www.conventionalcommits.org/) messages (`feat:`, `fix:`, `docs:`).

By contributing, you agree that your contributions are licensed under the same terms as the rest of
the repository: [CC BY-NC 4.0](LICENSE).
