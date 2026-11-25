# Contributing to The Traveler's Watch

Thank you for helping keep travelers on their path. Contributions of every size are welcome.

## Ways to contribute

| Contribution | Where |
|---|---|
| A **lens** for a new field (e.g. events, construction, nonprofit programs, product design) | `skills/checkwatch/references/lenses/` |
| A **translation review** by a native speaker | `README.<lang>.md` |
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
- Do not weaken the two core rules: **only the PM confirms a course change**, and **the Path log is
  append-only**.
- Use only standard Agent Skills frontmatter (`name`, `description`, `license`, `metadata`) so the
  skills stay portable.
- Explain behaviour changes in an ADR under `docs/adr/` when they change a design decision.

## Changing the hook

- Bash and awk only, with no other runtime dependencies.
- It must always exit 0, stay silent without a logbook, and keep the output capped.
- **Write the failing test first** in `tests/watchman.test.sh`, then make it pass:

  ```bash
  bash tests/watchman.test.sh
  ```

## Translations

`README.md` (English) is canonical. When you change it, note in the pull request which translated
READMEs are now out of date. Translators: keep the language bar, links, badges, commands, and shell
code blocks identical (the dialogue in *Quick example* may be translated). Update the
`Translated from` note at the top of the file. Arabic: keep prose inside `<div dir="rtl">` and code
blocks outside it.

## Pull requests

1. Fork, then create a branch: `feat/<thing>`, `fix/<thing>`, `docs/<thing>`, or `lens/<field>`.
2. Keep each pull request focused on one change.
3. Run `bash tests/watchman.test.sh` and `claude plugin validate .` if you have Claude Code.
4. Add an entry under **Unreleased** in [CHANGELOG.md](CHANGELOG.md).
5. Use [Conventional Commits](https://www.conventionalcommits.org/) messages (`feat:`, `fix:`, `docs:`).

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).
