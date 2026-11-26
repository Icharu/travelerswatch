<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · **简体中文** · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> 译自 `CONTRIBUTING.md`（v1.2.3，2026-11-26）。本译文为机器辅助翻译，以英文版为准。

# 为 The Traveler's Watch 做贡献

感谢你帮助旅人走在正确的路上。任何规模的贡献都欢迎。

## 促成本项目的背景

TTW 鼓励用户和贡献者在修改之前，先了解是什么促成了它。本项目的设计参考了 2020–2026 年发表的文献：关于语言模型在长时间工作中如何漂移的研究、关于 AI 如何改变项目管理的综述，以及一项关于范围蔓延（*scope creep*）的研究。

Koshman 和 Zubkova（2026）认为，关于 AI 在现代世界中如何运作和被使用的研究本质上是**跨学科**的，因此欢迎任何领域的贡献。以下两篇综述说明了 TTW 在这些研究中的位置：

- **AI 在项目管理中已经做得好的方面。** Adamantiadou 和 Tsironis（2025）综述了 97 篇同行评审研究（2011–2024）。据其摘要，机器学习、深度学习和混合模型已显示出改进项目管理的潜力，尤其是在**成本估算、工期预测和风险评估**方面。TTW 认真对待这一点：它在航向之内自动化重复性工作。
- **仍未解决的方面。** 据 Koshman 和 Zubkova（2026）的转述，同一篇综述指出：AI 模型对变化的项目条件适应不足，用初始数据进行的验证有限，并且在项目后评审等阶段的研究仍然很少。TTW 正是围绕这些空白构建的：方向由项目经理掌握，航向用证据核对，航行日志支持项目后评审。

*来源说明（阅读了什么）：* Koshman & Zubkova（2026）：已阅读全文。Adamantiadou & Tsironis（2025）：通过 Koshman & Zubkova 的转述，以及其 DOI 记录中的摘要和书目信息阅读；未阅读全文。本文件的早期版本把 97 篇文献的综述归于 Koshman & Zubkova，这是归属错误，已在 v1.2.3 中更正。

| 年份 | 文献 | 与本项目的关系 |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | 未经授权的变更会损害项目 → 每次方向调整都须确认并记录 |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | 模型最能利用长上下文的开头和结尾 → 在每次提示旁附上简短的航向 |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM 评审需要明确的标准 → 在做出任何判定前先设定标准 |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | 模型走错路后难以恢复 → 一开始就设定航向 |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | 提醒能降低漂移 → 每次提示都有守望者 |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | 对 97 篇研究的综述：AI 在估算、预测和风险方面显示出潜力；适应性、验证和后期阶段仍未解决 → 自动化重复性工作，保留人在回路 |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | 对 21 篇文献（2021–2025）和 AI 工具的综述；转述了 97 篇研究的综述；跨学科视角 → 人在回路，欢迎任何领域的贡献 |

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

**保持论断的类型。** 关于 TTW 的每一句话，要么是*设计意图*（“旨在”“技能指示 Claude”），要么是*机制*（“hook 做 X”，可在文件中核实），要么是*结果*（“在 <测试> 中，<数字>”）。译文必须保持同一类型：检查动词，而不只是名词。保持与英文相同的来源和数字，作者–年份引文和原始标题不翻译，不添加本地的论断或来源。西班牙语使用中性的国际西班牙语（无人称 *se* 或 *usted*）。zh-Hans 与 zh-Hant 分别本地化，绝不逐字转换。

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

本术语表为机器辅助翻译，欢迎母语人士修正。

## Pull requests

1. Fork 后创建分支：`feat/<主题>`、`fix/<主题>`、`docs/<主题>` 或 `lens/<领域>`。
2. 每个 pull request 只聚焦一项变更。
3. 如果你有 Claude Code，请运行 `bash tests/watchman.test.sh` 和 `claude plugin validate .`。
4. 在 [CHANGELOG.md](../../CHANGELOG.md) 的 **Unreleased** 下新增一条。
5. 使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式的提交信息（`feat:`、`fix:`、`docs:`）。

提交贡献即表示你同意你的贡献按与仓库其他部分相同的条款授权：[CC BY-NC 4.0](../../LICENSE)。
