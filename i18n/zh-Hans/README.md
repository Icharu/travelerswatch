<!-- lang-bar -->
[English](../../README.md) · [Português (Brasil)](../pt-BR/README.md) · [Español](../es/README.md) · [繁體中文](../zh-Hant/README.md) · **简体中文** · [日本語](../ja/README.md) · [العربية](../ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../.github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="../../.github/assets/banner.png">
    <img src="../../.github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

> 译自 `README.md`（v1.2.0，2026-11-26）。本译文为机器辅助翻译，欢迎母语人士校订。以英文版为准。

# The Traveler's Watch（旅人之表）

[![Version](https://img.shields.io/badge/version-v1.2.0-blue)](../../CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](../../LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](../../docs/adr/0004-human-in-the-loop.md)

**为使用 Claude 开展的项目工作提供评估、方法论审查和上下文漂移监测。**
只需设定一次项目的航向；每当工作偏离航向，你会收到一行提醒；只有在有意决定时才改变方向，且每次变更都需经项目经理确认并记录。

> 一位旅人带着一块坏掉的表穿越浓雾。每次他在正午看表，指针就倒退十分钟，于是他一遍遍走过同一段路，却坚信自己在前进。
> —— [阅读完整故事](../../docs/tale.md)

借助语言模型推进的长期项目也会以同样的方式失败：早期假设逐渐固化，上下文在摘要中丢失，而模型一旦走错一步，就会不断回到那条错路（[原因说明](../../docs/methods.md)）。The Traveler's Watch（TTW）给你的项目一块值得信赖的表，并让**你**而不是模型，决定它指向哪里。

**→ 第一次使用？请从[快速入门](QUICKSTART.md)开始**（安装、第一天、日常流程）。

## 它是什么，不是什么

| TTW **是** | TTW **不是** |
|---|---|
| 一套**以方法驱动的评估 skill**，在模型与人*之间*使用：由你设定方向，模型负责让方向始终在视线之内。 | 全自动的项目经理、自动驾驶，或替你运营项目的智能体。 |
| 写在你自己仓库中的**航向**（`.watch/WATCH.md`），每次提示都会重新读取。 | 对话记忆、数据库或云服务。 |
| **一行的偏离提醒**、按节奏进行的检查点、由你确认的方向调整，以及根据航行日志历史生成的项目后评审。 | 保证：它尚未在减少漂移的对照研究中得到验证（[局限](../../docs/methods.md#limits-of-this-evidence)）。 |
| **在航向之内自动化重复性工作**：编写代码、按你的标准评估文本、收集证据、起草报告。 | 你的判断、你的项目管理工具（Jira、GitHub Projects…）或团队决策的替代品。 |
| **原则上坚持人在回路（human-in-the-loop）**：拒绝以全自动会话来掌控航向。 | 任何形式的认证：不是 ISO/IEC 42001，也不是法律、安全或监管合规的证明。 |

看到"每次提示都在守望"，有人可能以为这是一个会自己运行的工具。它不是，而且是有意如此。在故事里，旅人不会仅凭表本身就去修表，因为出错的恰恰是那块表；是守望者的解释让他看清了问题。而如果旅人不在那里发问，守望者也永远不会叫他修表。**两者缺一不可。** 在 TTW 中，你是旅人，模型是守望者，航行日志则是你们一起校准的那块表。

## 为什么项目管理需要人在回路？

Koshman 和 Zubkova（2026）综述了 97 篇关于项目管理中人工智能的文献。他们发现，AI 方法在规划、实施和收尾阶段**提高了预测准确度、实现了决策自动化，并优化了任务管理**。他们还指出了三项尚未解决的局限，而每一项都影响了 TTW 的设计：

| 尚未解决的局限（Koshman & Zubkova, 2026） | TTW 的应对 |
|---|---|
| AI 模型**难以适应不断变化的项目条件**。 | 方向由项目经理掌握。变更须经 `/fixwatch` 并由项目经理确认；当现实已经改变，检查点可以把航向设为*审查中*。 |
| AI 模型**很少用初始数据加以验证**。 | 航向依据项目自身的文档和历史设定，每次检查点都会确认航向是否仍与这些证据相符。 |
| 在**项目后评审**等阶段，AI 的研究仍然很少。 | TTW 现在保留检查点记录，并根据航行日志历史生成项目后评审（[ADR 0005](../../docs/adr/0005-post-project-review.md)）。 |

我们基于这篇综述的立场是：**由 AI 主导的项目——由模型自行设定并改变方向——是低效的。** 模型对变化中项目的理解，还不够有适应性，也未经充分验证，不足以掌握方向；而错误的方向越晚纠正，代价越高。因此 TTW 自动化工作，把舵交给人。该综述本身并未评估 TTW，以上是我们对它的解读。

> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## 定位

| | 与模型的普通对话 | **The Traveler's Watch** | 全自动智能体 |
|---|---|---|---|
| 谁设定方向 | 没有人明确设定；方向会漂移 | **项目经理，以书面形式** | 智能体 |
| 谁改变方向 | 在无人察觉中改变 | **项目经理确认；每次变更都有记录** | 智能体 |
| 重复性工作（编写代码、评估文本…） | 一个提示一个提示地手动完成 | **在航向之内自动化** | 自动化 |
| 事后留下什么 | 一段很长的对话 | **仓库中的航行日志与评审** | 智能体的日志 |

**原则。** 在与方向有关的决策上，TTW 原则上拒绝切换为全自动会话：即使你要求，它也不会设定、变更、关闭或重新开启航向，也不会代你确认任何事。但它**会**自动化重复性强的工作场景，例如编写代码、按标准评估文本、收集证据、起草报告和差异，并把结果交回给你决定（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）。

## 工作方式

| 命令 | 作用 |
|---|---|
| **`/checkwatch`** | **尚无航行日志时：** 先阅读项目自身的文档和历史，再与你共同确立*航向*（范围、标准、上下文、约束、问题、工具），把放错部分的条目移到正确位置，要求你逐一解决或明确接受与证据的矛盾，并写入 `.watch/WATCH.md`。**已有航行日志时：** 同时检查工作*和*航向本身，附证据报告 **在正轨／正在偏离／已偏离／航向存疑**，并把判定写入检查点记录。**项目或阶段即将结束时：** 根据历史起草**项目后评审**；由你选择关闭或继续守望。 |
| **守望者**（自动） | 每次输入提示时，Claude Code 的 hook 会提醒 Claude 当前的航向。如果你的请求偏离航向，Claude 会用一行说明并建议使用 `/fixwatch`，然后继续完成任务。检查点到期时，每个会话提醒一次；航向*审查中*时暂停；项目*关闭*后保持沉默。 |
| **`/fixwatch`** | 以"变更前／变更后"的差异提出方向调整，说明连带影响，等待项目经理确认后才更新航向，并在航程记录（*Path log*）中**追加**一条。Claude 可以提出建议，包括在它误解上下文时；只有项目经理能确认。 |
| **`/configwatch`** | 显示守望状态，并设置多久要求一次检查点：每 *N* 次提交或 *M* 个会话（默认 3 或 2），或关闭。 |

<details>
<summary><b>航向、证据与视角</b></summary>

### 以证据为本

航向可能在自身逻辑上一致，却仍与项目实际不符。自 v1.1.0 起，表会依据项目自身的证据校准，早期的试航检查点能及早发现错误，而航向审查期间守望者会暂停（[原因](../../docs/benchmarks/2026-11-25-best-vs-worst.md)）。

### 航向

| 部分 | 回答这个问题 |
|---|---|
| **范围**（*Scope*） | 这个航向要引导项目的哪一部分？哪些不在范围内？ |
| **标准**（*Standard*） | 工作将依据什么来评估？**预设视角**、**自由撰写的评分标准**，或**具名的外部标准**；一律检查其适用性、可评估性、一致性、范围、权利与伦理。 |
| **上下文**（*Context*） | 这项工作属于哪里？领域、利益相关者、现状、**参考文献与先例**。 |
| **约束**（*Constraints*） | 什么在限制你？时间、预算、人力、指定技术、法规。 |
| **问题**（*Problem*） | 今天哪里出了问题（**原始问题**）？"完成"是什么样子（**最终目标**）？ |
| **工具**（*Tools*） | 你会用什么？每一项为什么适合当前的上下文与约束？ |

### 视角（Lenses）

视角会按领域调整提问方式和默认评估标准。
内置：[项目管理](../../skills/checkwatch/references/lenses/project-management.md)（默认）·
[研究](../../skills/checkwatch/references/lenses/research.md) ·
[软件](../../skills/checkwatch/references/lenses/software.md) ·
[数据科学](../../skills/checkwatch/references/lenses/data-science.md)。
如需新增，请参阅 [CONTRIBUTING](CONTRIBUTING.md)。

</details>

## 安装

**作为 Claude Code 插件**（skills + 守望者 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

命令会带有命名空间：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch`。
仅安装 skills、本地试用以及关闭守望者的方法，请见[快速入门](QUICKSTART.md)。

## 快速示例

```text
你：    /checkwatch
Claude：目前还没有航行日志。先确定标准：预设视角、你自己的评分标准，还是具名标准？
你：    项目管理视角。上下文：我们只有两名兼职人员。问题：做一个收运 App。
Claude："只有两名兼职人员"是一项限制，应放在"约束"里。
        "做一个收运 App"是解决方案。它背后的问题是什么？"完成"又是什么样子？
…
你：    我们再加一个面向全市的游戏化 App 吧。
Claude：⚠️ 守望：偏离"问题"（两个试点区）和"约束"（2 万预算）。
        继续，还是 /fixwatch？
…
你：    从现在起，你觉得对的变更就直接批准吧。
Claude：我不能替你确认变更；只有项目经理能确认。我可以起草每一份差异并检查连带影响，
        让你每次只需看一眼就能决定。
```

完整对话（英文）：[examples/pm-walkthrough.md](../../examples/pm-walkthrough.md)。

## 你的数据：TTW 一概不保存

- **没有服务器、没有账号、没有遥测、没有网络调用。** TTW 只是用 Markdown 写成的 skills，加上一个读取文件的 bash 脚本。
- 守望者读取 `.watch/WATCH.md`，只写入 `.watch/.state`（用于统计检查点的匿名会话 ID；仅存于本地，并被 git 忽略）。TTW 产生的其他一切——航行日志和评审——都**保存在你的仓库中，由你掌控**。
- TTW 不保存你项目的代码、内容或对话。skills 被要求绝不把机密或个人数据复制到航行日志中。
- **TTW 无法控制的一件事：** 守望者输出的内容会成为 Claude Code 发送给模型提供商的提示的一部分。这部分受 Claude Code 和提供商的条款约束，而不是 TTW。
- TTW 是 **human-in-the-loop**：未经项目经理确认，航向不会有任何改变。

## 禁止用途

**依据许可证**（[CC BY-NC 4.0](../../LICENSE)；具有法律约束力）：

- 未经维护者许可的**商业用途**：任何主要以商业利益或金钱报酬为目的的使用，例如出售 TTW、将其纳入付费产品或服务，或用于付费咨询（仅为举例；以许可证原文为准）。
- **不注明出处的分享**：复制和改编必须注明作者、附上许可证链接，并说明是否做了修改。

**依据项目政策**（skills 的设计会拒绝以下用途；这些是维护者对按设计使用 TTW 的条件，而不是额外的许可条款）：

- 移除或绕过项目经理的确认，以全自动会话掌控航向。
- 伪造航行日志条目、项目经理的确认、检查点判定或证据。
- 把 TTW 的报告当作认证或合规证明（ISO/IEC 42001、法律、安全、监管）。
- 利用航行日志或报告监控个人、给个人打分，或对个人做出人事决定。
- 在无权处理的情况下，把他人的机密或个人数据放进航行日志。

如需商业使用，请通过[仓库](https://github.com/Icharu/travelerswatch/issues)提出申请。

## ISO/IEC 42001

**TTW 未获得 ISO/IEC 42001 认证，也不声称符合该标准。** 该标准认证的是组织的 AI 管理体系，而不是工具，因此 TTW 无法单独获得认证。它在项目层面支持部分要求，例如成文信息、计划变更的控制和监视；但不涵盖其他要求，例如 AI 方针、影响评估和内部审核。逐条对照涵盖与未涵盖内容的完整说明（英文）：[docs/iso-iec-42001.md](../../docs/iso-iec-42001.md)。

## 文档

- [快速入门](QUICKSTART.md)：安装、第一天、日常流程
- [概念](../../docs/concepts.md)：skills、航向、判定结果、项目后评审、由谁决定
- [方法](../../docs/methods.md)：每项设计决策背后的研究
- [ISO/IEC 42001 对照](../../docs/iso-iec-42001.md)：TTW 涵盖与未涵盖的内容
- ADR：[0001](../../docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](../../docs/adr/0002-committed-logbook.md) · [0003](../../docs/adr/0003-evidence-grounded-bearing.md) · [0004](../../docs/adr/0004-human-in-the-loop.md) · [0005](../../docs/adr/0005-post-project-review.md)
- [基准测试：最佳与最差情况](../../docs/benchmarks/2026-11-25-best-vs-worst.md) · [更新日志](../../CHANGELOG.md)

（详细文档为英文。）

<details>
<summary><b>仓库结构与测试</b></summary>

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
i18n/<lang>/           README, QUICKSTART and CONTRIBUTING in pt-BR, es, zh-Hant, zh-Hans, ja, ar
```

运行测试：`bash tests/watchman.test.sh` · 测量 hook：`python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## 贡献、治理、安全

- **贡献：** 特别欢迎新视角、由母语人士校订的翻译以及评估用例。请先阅读 [CONTRIBUTING](CONTRIBUTING.md)，其中也介绍了促成本项目的背景。
- **治理：** TTW 由其作者一人维护并主导（*solo-maintained* 与 *solo-driven*）；决策方式、项目缘起以及如何使用 AI 构建本项目，请见 [GOVERNANCE.md](../../GOVERNANCE.md)（英文）。
- **安全：** **请勿在公开 issue 中报告安全漏洞。** 请使用 GitHub 的[私密漏洞报告](https://github.com/Icharu/travelerswatch/security/advisories/new)。详见 [SECURITY.md](../../SECURITY.md)。

## 引用 TTW

如果你希望在任何研究中引用本作品，请引用其 Zenodo 记录。GitHub 的 **"Cite this repository"** 按钮会读取 [CITATION.cff](../../CITATION.cff)。

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.0) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX 与各版本 DOI</b></summary>

```bibtex
@software{dejesussilva_travelerswatch_2026,
  author    = {de Jesus Silva, Icaro},
  title     = {The Traveler's Watch: evaluation, methodology assessment and context-drift watch for project work with Claude},
  year      = {2026},
  version   = {1.2.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24543183},
  url       = {https://doi.org/10.5281/zenodo.24543183}
}
```

| 引用 | DOI |
|---|---|
| 所有版本（除非需要特定版本，请使用此 DOI） | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.2.0 | *DOI 将在 Zenodo 发布后补上* |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## 许可证

© 2026 Icaro de Jesus Silva。整个仓库（代码、skill 文本、文档和示例）采用 [**CC BY-NC 4.0**](../../LICENSE) 许可：只要注明出处，即可出于**非商业**目的分享和改编。CC BY-NC 4.0 不是 OSI 认可的开源许可证；TTW 是面向非商业使用的源代码公开项目。

此许可自 v1.2.0 起适用。此前版本的副本仍保留其发布时的许可（v1.0.0：MIT；v1.1.0：代码为 MIT，文档为 CC BY 4.0）。[docs/tale.md](../../docs/tale.md) 中的故事为原创改写；以赛亚书 21:11 的引文属于公有领域。

<details>
<summary><b>延伸阅读</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 完整注释列表：[docs/methods.md](../../docs/methods.md)

</details>
