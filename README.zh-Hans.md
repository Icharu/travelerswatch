<!-- lang-bar -->
[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [繁體中文](README.zh-Hant.md) · **简体中文** · [日本語](README.ja.md) · [العربية](README.ar.md)

> 译自 `README.md` v1.0.0（2026-11-25）。本文为机器辅助翻译，欢迎母语人士协助校订；以英文版为准。

# The Traveler's Watch（旅人之表）

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending%20(Zenodo)-lightgrey)](CITATION.cff)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**为使用 Claude 开展的项目工作提供评估、方法论审查和上下文漂移监测。**
只需设定一次项目的航向；每当工作偏离航向，你会收到一行提醒；只有在有意决定时才改变方向，且每次变更都需经项目经理确认并记录。

> 一位旅人带着一块坏掉的表穿越浓雾。每次他在正午看表，指针就倒退十分钟，于是他一遍遍走过同一段路，却坚信自己在前进。
> —— [阅读完整故事](docs/tale.md)

借助语言模型推进的长期项目也会以同样的方式失败：早期假设逐渐固化，上下文在摘要中丢失，而模型一旦走错一步，就会不断回到那条错路（[原因说明](docs/methods.md)）。The Traveler's Watch 给你的项目一块值得信赖的表。

## 工作方式

| 命令 | 作用 |
|---|---|
| **`/checkwatch`** | **尚无航行日志时：** 与你共同确立*航向*（标准、上下文、约束、问题、工具），把放错部分的条目移到正确位置，指出各部分之间的张力，并写入 `.watch/WATCH.md`。**已有航行日志时：** 进行检查点评估，并附证据报告 **在正轨／正在偏离／已偏离**。 |
| **守望者**（自动） | 每次输入提示时，Claude Code 的 hook 会提醒 Claude 当前的航向。如果你的请求偏离航向，Claude 会用一行说明并建议使用 `/fixwatch`，然后继续完成任务。 |
| **`/fixwatch`** | 以"变更前／变更后"的差异提出方向调整，说明连带影响，等待项目经理确认后才更新航向，并在航程记录（*Path log*）中**追加**一条。Claude 可以提出建议，包括在它误解上下文时；只有项目经理能确认。 |

### 航向

| 部分 | 回答这个问题 |
|---|---|
| **标准**（*Standard*） | 工作将依据什么来评估？**预设视角**、**自由撰写的评分标准**，或**具名的外部标准**；一律检查其适用性、可评估性、一致性、范围、权利与伦理。 |
| **上下文**（*Context*） | 这项工作属于哪里？领域、利益相关者、现状、**参考文献与先例**。 |
| **约束**（*Constraints*） | 什么在限制你？时间、预算、人力、指定技术、法规。 |
| **问题**（*Problem*） | 今天哪里出了问题（**原始问题**）？"完成"是什么样子（**最终目标**）？ |
| **工具**（*Tools*） | 你会用什么？每一项为什么适合当前的上下文与约束？ |

### 视角（Lenses）

视角会按领域调整提问方式和默认评估标准。
内置：[项目管理](skills/checkwatch/references/lenses/project-management.md)（默认）·
[研究](skills/checkwatch/references/lenses/research.md) ·
[软件](skills/checkwatch/references/lenses/software.md) ·
[数据科学](skills/checkwatch/references/lenses/data-science.md)。
如需新增，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens)。

## 安装

**作为 Claude Code 插件**（skills + 守望者 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

命令会带有命名空间：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`。

**仅安装 skills**（Claude Code 或任何支持 [Agent Skills](https://agentskills.io/) 的智能体；不含 hook）：

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch ~/.claude/skills/
```

命令即为 `/checkwatch` 和 `/fixwatch`。没有 hook 时，请在每次工作会话开始时运行 `/checkwatch`。

**不安装、在本地试用：** `claude --plugin-dir ./travelerswatch`

**暂时关闭守望者：** `export TRAVELERSWATCH_DISABLE=1`

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
```

完整对话（英文）：[examples/pm-walkthrough.md](examples/pm-walkthrough.md)。

## 仓库结构

```text
.claude-plugin/        插件与 marketplace 清单
skills/checkwatch/     SKILL.md · references/（标准、各部分、关系、视角）· assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
hooks/                 hooks.json · watchman.sh（仅需 bash + awk）
tests/                 watchman.test.sh
docs/                  故事 · 概念 · 方法（文献）· adr/
examples/              项目管理实例
```

运行测试：`bash tests/watchman.test.sh`

## 文档

- [概念](docs/concepts.md)：skills、航向、判定结果、由谁决定
- [方法](docs/methods.md)：每项设计决策背后的研究
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md)
- [更新日志](CHANGELOG.md)

（详细文档为英文。）

## 贡献

欢迎各种贡献，尤其是其他领域的**新视角**、由母语人士校订的翻译，以及新的评估用例。提交 pull request 前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 安全

**请勿在公开 issue 中报告安全漏洞。** 请使用 GitHub 的[私密漏洞报告](https://github.com/Icharu/travelerswatch/security/advisories/new)（**Security** 标签页 → **Report a vulnerability**）。响应时间为尽力而为，并取决于严重程度。适用范围、响应时间表以及等待期间的建议，请见 [SECURITY.md](SECURITY.md)。

## 引用

如果你在研究或教学中使用 The Traveler's Watch，请予以引用。GitHub 的 **"Cite this repository"** 按钮会读取 [CITATION.cff](CITATION.cff)。v1.0.0 发布后，将在此添加 Zenodo DOI。

## 许可证

[MIT](LICENSE) © 2026 Icaro de Jesus Silva。[docs/tale.md](docs/tale.md) 中的故事为原创改写；以赛亚书 21:11 的引文属于公有领域。

## 延伸阅读

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 完整注释列表：[docs/methods.md](docs/methods.md)
