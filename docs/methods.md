# Methods — the literature behind the design

Each design choice in The Traveler's Watch maps to a finding below. Citations were checked against
their arXiv / publisher listings on 2026-11-25. Where authors are not listed, cite by title and ID.

## 1. Why a watch is needed: LLMs drift across turns

| Source | Finding | Design consequence |
|---|---|---|
| Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2025). *LLMs Get Lost In Multi-Turn Conversation.* [arXiv:2505.06120](https://arxiv.org/abs/2505.06120) (ICLR 2026). | Across 200,000+ simulated conversations, top models performed on average 39% worse when a task was spread over several turns than when given in one. Models make early assumptions, attempt final answers too soon, and "when LLMs take a wrong turn… they get lost and do not recover." | The rewinding watch. `/checkwatch` gathers the full bearing **up front** so the problem is fully specified, and `/fixwatch` gives an explicit way to recover from a wrong turn. |
| *Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation.* [arXiv:2602.07338](https://arxiv.org/abs/2602.07338) | Links multi-turn failure to a mismatch between what the user intends and what the model assumes. | The Problem section asks separately for the **original problem** and the **final objective**, and misfiling checks catch solutions posing as problems. |
| Dongre, V., Rossi, R. A., Lai, V. D., Yoon, D. S., Hakkani-Tür, D., & Bui, T. (2025). *Drift No More? Context Equilibria in Multi-Turn LLM Interactions.* [arXiv:2510.07777](https://arxiv.org/abs/2510.07777) | Drift tends to settle at a bounded level rather than grow without limit, and simple **reminder interventions** shift that level downward. | The watchman hook: a short goal reminder on every prompt ([ADR 0001](adr/0001-hook-for-per-prompt-watch.md)). |
| Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). *Lost in the Middle: How Language Models Use Long Contexts.* TACL 12, 157–173. [doi:10.1162/tacl_a_00638](https://doi.org/10.1162/tacl_a_00638) · [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) | Models use information at the start and end of a long context better than information in the middle (a U-shaped curve). | The bearing is injected at the newest edge of the context (with the user's prompt) and kept short (≤ 4,000 chars). |

## 2. Why the evaluator must state its standard

| Source | Finding | Design consequence |
|---|---|---|
| *A Survey on LLM-as-a-Judge.* [arXiv:2411.15594](https://arxiv.org/abs/2411.15594) | Reliability is the core open problem for LLM judges; it needs careful design and standardization. | The **Standard** is set explicitly before any judgement, and every ⚠️/❌ in a report must cite evidence. |
| *LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods.* [arXiv:2412.05579](https://arxiv.org/abs/2412.05579) | LLM judges can adapt criteria to task context instead of fixed metrics — useful, but a source of inconsistency. | Three standard modes (lens / rubric / named standard) plus a **boundary check** so the criteria are fixed, evaluable, and in scope. |

## 3. Why course changes must be authorized and logged

| Source | Finding | Design consequence |
|---|---|---|
| Komal, B., Janjua, U. I., Anwar, F., Madni, T. M., Cheema, M. F., Malik, M. N., & Shahid, A. R. (2020). *The Impact of Scope Creep on Project Success: An Empirical Investigation.* IEEE Access 8, 125755–125775. [doi:10.1109/ACCESS.2020.3007098](https://doi.org/10.1109/ACCESS.2020.3007098) | Scope-creep factors identified by a systematic review and confirmed empirically are negatively associated with software project success. | Drift detection on every prompt; the PM lens's "changes are controlled" criterion. |
| PMI. *Top five causes of scope creep… and what to do about them.* [pmi.org](https://www.pmi.org/learning/library/top-five-causes-scope-creep-6675) | Scope creep is not the same as change; the issue is whether the change was authorized. | `/fixwatch`: Claude may propose, **only the PM confirms**, and every change is logged. |
| *Context Branching for LLM Conversations: A Version Control Approach to Exploratory Programming.* [arXiv:2512.13914](https://arxiv.org/abs/2512.13914) | Applies version-control ideas to managing conversation context. | The append-only Path log plus a committed logbook ([ADR 0002](adr/0002-committed-logbook.md)). |

## 4. Why it is packaged as a skill

| Source | Point | Design consequence |
|---|---|---|
| Anthropic (2025). *Equipping agents for the real world with Agent Skills.* [anthropic.com/engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) | Progressive disclosure: name and description first, body on demand, references only when needed. | Short `SKILL.md` bodies; lenses and checklists live in `references/`. |
| Agent Skills specification. [agentskills.io](https://agentskills.io/) | Open, vendor-neutral format for skills. | The skills use only standard frontmatter so they run outside Claude Code too. |

## 5. Why a human stays in the loop

| Source | Finding | Design consequence |
|---|---|---|
| Koshman, Y., & Zubkova, A. (2026). *Artificial intelligence in project management.* Development Management, 25(1), 23–31. [doi:10.63341/devt/1.2026.23](https://doi.org/10.63341/devt/1.2026.23) | A review of 97 publications: AI methods improved forecast accuracy, automated decision-making, and optimised task management in the planning, implementation, and closure stages. Unresolved: AI models adapt poorly to changing project conditions, are rarely validated against the initial data, and are little studied in phases such as the post-project review. | Direction stays with the PM ([ADR 0004](adr/0004-human-in-the-loop.md)); the bearing is checked against the project's evidence ([ADR 0003](adr/0003-evidence-grounded-bearing.md)); a post-project review is built from the logbook ([ADR 0005](adr/0005-post-project-review.md)). |
| Adamantiadou, D. S., & Tsironis, L. (2025). *Leveraging Artificial Intelligence in Project Management: A Systematic Review of Applications, Challenges, and Future Directions.* Computers, 14(2), 66. [doi:10.3390/computers14020066](https://doi.org/10.3390/computers14020066) — *cited here as it is cited in Koshman & Zubkova (2026).* | Machine learning, deep learning, and hybrid models have expanded what project management can do, improving cost estimation, schedule forecasting, and risk analysis. | TTW automates repetitive work inside the bearing (coding, evaluating texts, gathering evidence) and keeps the decisions with a person. |

## Limits of this evidence

Findings on multi-turn degradation are strongest for reasoning and generation tasks; at least one
study ([arXiv:2512.20662](https://arxiv.org/abs/2512.20662)) found little degradation for pure fact
retrieval over long chats. The Traveler's Watch targets the first case — open-ended project work —
and has not been evaluated in a controlled study. The evals in `skills/*/evals/` are behavioural
checks, not a measurement of drift reduction.
