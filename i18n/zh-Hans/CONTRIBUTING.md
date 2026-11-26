<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · **简体中文** · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> 译自 `CONTRIBUTING.md`（v1.2.0，2026-11-26）。本译文为机器辅助翻译，以英文版为准。

# 为 The Traveler's Watch 做贡献

感谢你帮助旅人走在正确的路上。任何规模的贡献都欢迎。

## 促成本项目的背景

TTW 鼓励用户和贡献者在修改之前，先了解是什么促成了它。本项目的设计建立在大约**五年的研究（2021–2026）**之上：语言模型在长时间工作中如何漂移，以及 AI 如何改变项目管理；此外还参考了一项更早的范围蔓延（*scope creep*）研究。

关于 AI 在现代世界中如何运作和被使用的研究，本质上是**跨学科**的（Koshman & Zubkova, 2026），因此欢迎任何领域的贡献。以下两篇综述说明了 TTW 在这些研究中的位置：

- **AI 在项目管理中已经做得好的方面。** Adamantiadou 和 Tsironis（2025）发现，机器学习、深度学习和混合模型显著扩展了项目管理的能力，改进了**成本估算、进度预测和风险分析**。TTW 认真对待这一点：它在航向之内自动化重复性工作。
  *透明度说明：我们依据 Koshman & Zubkova（2026）的转述引用这一发现；原始文章的书目信息已通过其 DOI 核对。*
- **仍未解决的方面。** Koshman 和 Zubkova（2026）综述了 97 篇文献，发现 AI 模型难以适应变化的项目条件、很少用初始数据加以验证，并且在项目后评审等阶段的研究仍然很少。TTW 正是围绕这些空白构建的：方向由项目经理掌握，航向用证据核对，航行日志支持项目后评审。

| 年份 | 文献 | 与本项目的关系 |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | 未经授权的变更会损害项目 → 每次方向调整都须确认并记录 |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | 模型最能利用长上下文的开头和结尾 → 在每次提示旁附上简短的航向 |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM 评审需要明确的标准 → 在做出任何判定前先设定标准 |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | 模型走错路后难以恢复 → 一开始就设定航向 |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | 提醒能降低漂移 → 每次提示都有守望者 |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | AI 改进估算、预测和风险分析 → 自动化重复性工作 |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | 适应性、验证和项目后评审仍未解决 → 人在回路 |

完整的注释列表以及每个来源对设计的影响，请见 [docs/methods.md](../../docs/methods.md)（英文）。项目如何开始、由谁决定，请见 [GOVERNANCE.md](../../GOVERNANCE.md)。

<details>
<summary><b>完整参考文献</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- 其他来源：[docs/methods.md](../../docs/methods.md)。

</details>

## 贡献方式

| 贡献 | 位置 |
|---|---|
| 新领域的**视角**（例如活动、建筑、非营利项目、产品设计） | `skills/checkwatch/references/lenses/` |
| 由母语人士进行的**翻译校订** | `i18n/<lang>/`（README、QUICKSTART、CONTRIBUTING、tale） |
| 新的**评估用例**（一个提示加上预期行为） | `skills/<skill>/evals/evals.json` |
| **错误报告**或想法 | [Issues](https://github.com/Icharu/travelerswatch/issues)。请使用模板。 |
| **安全问题** | **不要**发在 issues。请见 [SECURITY.md](../../SECURITY.md)。 |

## 新增视角

1. 复制一个现有视角（例如 `project-management.md`）为 `lenses/<领域>.md`。
2. 保留相同的四个标题，让 skill 能以相同方式使用任何视角：
   - **How the sections read in this field**：用表格改写上下文、约束、问题、工具
   - **Default criteria**：4–8 条*可观察*的标准（见 `references/standards.md`）
   - **Drift signals**：在这个领域偏离路线是什么样子
   - **Typical tools**
3. **用你自己的话**撰写标准。不要粘贴付费或受版权保护标准的文字；只写出名称并引用章节。
4. 把视角加入 `skills/checkwatch/SKILL.md`（步骤 A1）的列表，以及 README 的 *Lenses* 部分。
5. 在 `skills/checkwatch/evals/evals.json` 中至少新增一个使用该视角的评估用例。

## 修改 skills

- 让每个 `SKILL.md` 保持简短、以决策为导向；细节放在 `references/`。
- 不要削弱核心规则（[GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)）：方向调整、关闭或接受矛盾**只能由项目经理确认**；**Path log 和检查点记录只能追加**；航向**不采用全自动会话**（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）；**不在用户仓库之外保存任何数据**。
- 只使用标准的 Agent Skills frontmatter（`name`、`description`、`license`、`metadata`），让 skills 保持可移植。
- 当行为变更改动了设计决策时，请在 `docs/adr/` 中用 ADR 说明。

## 修改 hook

- 只使用 bash（≥ 3.2，为了 macOS）和 awk；git 为可选。优先使用 bash 内建功能，而不是额外的进程；航行日志用一次 `awk` 解析。
- 它必须始终以 0 退出；没有航行日志或航向为 `closed` 时保持沉默；限制输出长度；不进行网络调用；除 `.watch/.state` 外不写入任何文件。
- **先写会失败的测试**（`tests/watchman.test.sh`），再让它通过，并测量修改前后每次提示的耗时：

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## 修改航行日志格式

hook 会解析固定标签：`## Status`、`- **Bearing:**`（`confirmed` / `under review …` / `closed …`）、`- **Checkpoint cadence:**`（`every N commits or M sessions` / `off`）、`- **Last checkpoint:** <date> @ <sha>`、`**Boundary notes:**`、Relations 中含有 "accepted" 的行，以及 `## Path log` 标题。`## Checkpoint log` 只由 skills 读取。修改这些标签时，必须同时修改 hook、模板（`skills/checkwatch/assets/WATCH.md`）、skills 和测试。

## 翻译

根目录中的英文文件（`README.md`、`QUICKSTART.md`、`CONTRIBUTING.md`）为正式版本。翻译按语言集中放在 `i18n/<lang>/`，让根目录保持整洁。修改英文文件时，请在 pull request 中注明哪些翻译因此过时。译者：请保持语言栏、链接（相对于 `i18n/<lang>/`，例如 `../../docs/methods.md`）、徽章、命令和 shell 代码块完全相同（*快速示例*中的对话可以翻译）。请更新文件顶部的"译自"说明。阿拉伯语：正文放在 `<div dir="rtl">` 内，代码块放在外面。

## Pull requests

1. Fork 后创建分支：`feat/<主题>`、`fix/<主题>`、`docs/<主题>` 或 `lens/<领域>`。
2. 每个 pull request 只聚焦一项变更。
3. 如果你有 Claude Code，请运行 `bash tests/watchman.test.sh` 和 `claude plugin validate .`。
4. 在 [CHANGELOG.md](../../CHANGELOG.md) 的 **Unreleased** 下新增一条。
5. 使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式的提交信息（`feat:`、`fix:`、`docs:`）。

提交贡献即表示你同意你的贡献按与仓库其他部分相同的条款授权：[CC BY-NC 4.0](../../LICENSE)。
