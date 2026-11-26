<!-- lang-bar -->
[English](../../QUICKSTART.md) · [Português (Brasil)](../pt-BR/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · **繁體中文** · [简体中文](../zh-Hans/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [العربية](../ar/QUICKSTART.md)

> 譯自 `QUICKSTART.md`（v1.2.0，2026-11-26）。本譯文為機器輔助翻譯，以英文版為準。

# 快速入門

安裝 The Traveler's Watch（TTW），在第一天設定專案的航向，之後每天使用它。返回 [README](README.md)。

**TTW 以每日為單位、由你主導（daily-led）。** 每天的工作由你帶領。守望者在每次提示時讓航向保持在視線之內，航行日誌保存歷史；因此每一天都從專案的真實狀態開始，而不是從模型記得的內容開始。

## 1. 安裝

擇一即可。

| 方式 | 指令 | 你會得到 |
|---|---|---|
| **Claude Code 外掛**（建議） | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | skills + 自動守望者。指令：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch` |
| **只安裝 skills**（Claude Code 或任何 [Agent Skills](https://agentskills.io/) 代理） | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | skills，不含守望者。指令：`/checkwatch`、`/fixwatch`、`/configwatch`。請在每次工作階段開始時手動執行 `/checkwatch`。 |
| **不安裝直接試用** | `claude --plugin-dir ./travelerswatch` | 所有功能，僅限本次工作階段 |

需求：守望者需要 Claude Code；需要 `bash` 與 `awk`（macOS 與 Linux 皆內建）；`git` 為選用，但能啟用提交次數計算與完整的專案後檢討。

## 2. 第一天：設定航向

1. 在專案根目錄開啟 Claude Code。
2. 執行 **`/checkwatch`**。用一行回答：這個專案是什麼，以及這個航向要引導哪一部分。
3. Claude 會閱讀你的 README、`docs/` 與近期的 git 歷史，接著顯示一張**證據卡**與各區塊的**草稿**。由你修正；它會詢問缺漏、放錯區塊的項目，以及你的回答與證據相矛盾之處。大約需要五輪。
4. 確認航向。Claude 會寫入 `.watch/WATCH.md`，並把 `.watch/.state` 加入 `.gitignore`。
5. **提交航行日誌**：`git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`。

從此以後，未經你確認，航向不會有任何改變。

## 3. 每一天

| 時機 | 你要做的事 | TTW 會做的事 |
|---|---|---|
| **一天的開始** | 開啟 Claude Code，照常工作。 | 守望者在你第一次提示時重新讀取 `.watch/WATCH.md`，因此昨天確認的變更已經生效。 |
| **工作期間** | 提出你需要的：程式碼、審查、草稿。 | 重複性工作在航向之內完成。若某個請求偏離航向，Claude 會用**一行**說明並繼續。 |
| **出現偏移提醒** | 判斷：這只是繞路，還是路線真的在改變？ | 繞路：直接繼續。真正的改變：執行 **`/fixwatch`**，檢視差異與連帶影響，然後確認或取消。 |
| **「檢查點到期」** | 有空時執行 **`/checkwatch`**。 | 附證據回報*在路上／正在偏移／已偏離／航向存疑*，並在檢查點記錄中新增一行。 |
| **一天的結束** | 若 `.watch/WATCH.md` 有變更，與你的工作一起提交。 | 不做其他事。TTW 不在你的儲存庫之外保存任何資料。 |
| **階段或專案結束時** | 告訴 Claude：「這個階段要結束了，我們來做專案後檢討。」 | 根據檢查點記錄、Path log 與 git 歷史起草檢討。由你選擇**檢討並結案**或**僅檢討**。 |

### TTW 知道什麼，何時知道

TTW 透過航行日誌與 git 掌握專案每天的變化，而不是監看你的檔案。準確地說：

| 時機 | 會讀取 | **不會**讀取 |
|---|---|---|
| **每次提示**（守望者） | `.watch/WATCH.md` 中的航向與 Status；自上次檢查點以來的提交數與工作階段數。 | 你的程式碼、差異或其他檔案。 |
| **檢查點**（`/checkwatch`） | 對話內容、自上次檢查點以來的 `git log`、變更過的檔案、*Evidence scanned* 中列出的文件。 | 專案資料夾以外的任何東西。 |
| **專案後檢討** | 完整的航行日誌（檢查點記錄 + Path log）以及 `.watch/WATCH.md` 的 git 歷史。 | 專案資料夾以外的任何東西。 |

## 4. 指令一覽

| 指令 | 用途 |
|---|---|
| `/checkwatch` | 設定航向（第一次）· 執行檢查點 · 執行專案後檢討 |
| `/fixwatch` | 刻意調整方向 · 結束審查 · 重新開啟已結案的專案 |
| `/configwatch` | 查看狀態 · 設定檢查點頻率：試航 `every 3 commits or 2 sessions`（預設）、穩定 `every 10 commits or 5 sessions`、自訂，或 `off` |

## 5. TTW 不會替你做的事

即使你要求，TTW 也不會代你確認變更、接受矛盾或結束專案。它會起草差異、檢查連帶影響並蒐集證據，讓你每次只需看一眼就能做決定。這是刻意的設計：請見 README 中的〈它是什麼，不是什麼〉（[README](README.md)）。

## 6. 關閉或暫停

- 僅限目前的終端機：`export TRAVELERSWATCH_DISABLE=1`
- 永久關閉：`/plugin` → travelerswatch → disable（skills 仍可手動使用）。
- 減少檢查點提醒：`/configwatch` → 穩定或 `off`。

## 下一步

[概念](../../docs/concepts.md) · [完整範例](../../examples/pm-walkthrough.md) ·
[方法](../../docs/methods.md) · [貢獻指南](CONTRIBUTING.md)
