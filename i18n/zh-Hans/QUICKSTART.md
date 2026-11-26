<!-- lang-bar -->
[English](../../QUICKSTART.md) · [Português (Brasil)](../pt-BR/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [繁體中文](../zh-Hant/QUICKSTART.md) · **简体中文** · [日本語](../ja/QUICKSTART.md) · [العربية](../ar/QUICKSTART.md)

> 译自 `QUICKSTART.md`（v1.2.2，2026-11-26）。本译文为机器辅助翻译，以英文版为准。

# 快速入门

安装 The Traveler's Watch（TTW），在第一天设定项目的航向，之后每天使用它。返回 [README](README.md)。

**TTW 以每日为单位、由你主导（daily-led）。** 每天的工作由你带领。守望者在每次提示时让航向保持在视线之内，航行日志保存历史；因此每一天都从项目的真实状态开始，而不是从模型记得的内容开始。

## 1. 安装

任选其一。

| 方式 | 命令 | 你会得到 |
|---|---|---|
| **Claude Code 插件**（推荐） | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | skills + 自动守望者。命令：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch` |
| **仅安装 skills**（Claude Code 或任何 [Agent Skills](https://agentskills.io/) 智能体） | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | skills，不含守望者。命令：`/checkwatch`、`/fixwatch`、`/configwatch`。请在每次会话开始时手动运行 `/checkwatch`。 |
| **不安装直接试用** | `claude --plugin-dir ./travelerswatch` | 全部功能，仅限本次会话 |

要求：守望者需要 Claude Code；需要 `bash` 和 `awk`（macOS 和 Linux 均自带）；`git` 为可选，但能启用提交次数统计和完整的项目后评审。

## 2. 第一天：设定航向

1. 在项目根目录打开 Claude Code。
2. 运行 **`/checkwatch`**。用一行回答：这个项目是什么，以及这个航向要引导哪一部分。
3. Claude 会阅读你的 README、`docs/` 和近期的 git 历史，然后展示一张**证据卡**和各部分的**草稿**。由你修改；它会询问缺漏、放错部分的条目，以及你的回答与证据相矛盾的地方。大约需要五轮。
4. 确认航向。Claude 会写入 `.watch/WATCH.md`，并把 `.watch/.state` 加入 `.gitignore`。
5. **提交航行日志**：`git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`。

从此以后，未经你确认，航向不会有任何改变。

## 3. 每一天

| 时机 | 你要做的事 | TTW 会做的事 |
|---|---|---|
| **一天开始** | 打开 Claude Code，照常工作。 | 守望者在你第一次提示时重新读取 `.watch/WATCH.md`，因此昨天确认的变更已经生效。 |
| **工作期间** | 提出你需要的：代码、评审、草稿。 | 重复性工作在航向之内完成。如果某个请求偏离航向，Claude 会用**一行**说明并继续。 |
| **出现偏离提醒** | 判断：这只是绕路，还是路线真的在改变？ | 绕路：直接继续。真正的改变：运行 **`/fixwatch`**，查看差异和连带影响，然后确认或取消。 |
| **"检查点到期"** | 有空时运行 **`/checkwatch`**。 | 附证据报告*在正轨／正在偏离／已偏离／航向存疑*，并在检查点记录中新增一行。 |
| **一天结束** | 如果 `.watch/WATCH.md` 有变更，和你的工作一起提交。 | 不做其他事。TTW 不在你的仓库之外保存任何数据。 |
| **阶段或项目结束时** | 告诉 Claude："这个阶段要结束了，我们来做项目后评审。" | 根据检查点记录、Path log 和 git 历史起草评审。由你选择**评审并关闭**或**仅评审**。 |

### TTW 知道什么，何时知道

TTW 通过航行日志和 git 掌握项目每天的变化，而不是监视你的文件。准确地说：

| 时机 | 会读取 | **不会**读取 |
|---|---|---|
| **每次提示**（守望者） | `.watch/WATCH.md` 中的航向和 Status；自上次检查点以来的提交数和会话数。 | 你的代码、差异或其他文件。 |
| **检查点**（`/checkwatch`） | 对话内容、自上次检查点以来的 `git log`、变更过的文件、*Evidence scanned* 中列出的文档。 | 项目文件夹以外的任何内容。 |
| **项目后评审** | 完整的航行日志（检查点记录 + Path log）以及 `.watch/WATCH.md` 的 git 历史。 | 项目文件夹以外的任何内容。 |

## 4. 命令一览

| 命令 | 用途 |
|---|---|
| `/checkwatch` | 设定航向（第一次）· 运行检查点 · 运行项目后评审 |
| `/fixwatch` | 有意调整方向 · 结束审查 · 重新开启已关闭的项目 |
| `/configwatch` | 查看状态 · 设置检查点频率：试航 `every 3 commits or 2 sessions`（默认）、稳定 `every 10 commits or 5 sessions`、自定义，或 `off` |

## 5. TTW 不会替你做的事

即使你要求，TTW 也不会代你确认变更、接受矛盾或关闭项目。它会起草差异、检查连带影响并收集证据，让你每次只需看一眼就能做决定。这是有意的设计：请见 README 中的"它是什么，不是什么"（[README](README.md)）。

## 6. 关闭或暂停

- 仅限当前终端：`export TRAVELERSWATCH_DISABLE=1`
- 永久关闭：`/plugin` → travelerswatch → disable（skills 仍可手动使用）。
- 减少检查点提醒：`/configwatch` → 稳定或 `off`。

## 下一步

[概念](../../docs/concepts.md) · [完整示例](../../examples/pm-walkthrough.md) ·
[方法](../../docs/methods.md) · [贡献指南](CONTRIBUTING.md)
