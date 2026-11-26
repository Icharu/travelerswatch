<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · **繁體中文** · [简体中文](../zh-Hans/CONTRIBUTING.md) · [日本語](../ja/CONTRIBUTING.md) · [العربية](../ar/CONTRIBUTING.md)

> 譯自 `CONTRIBUTING.md`（Unreleased，2026-11-25）。本譯文為機器輔助翻譯，以英文版為準。

# 為 The Traveler's Watch 貢獻

感謝你幫助旅人走在正確的路上。任何規模的貢獻都歡迎。

## 促成本專案的背景

TTW 鼓勵使用者與貢獻者在修改之前，先了解是什麼促成了它。本專案的設計建立在大約**五年的研究（2021–2026）**之上：語言模型在長時間工作中如何偏移，以及 AI 如何改變專案管理；另外還參考了一項更早的範疇蔓延（*scope creep*）研究。

關於 AI 在現代世界中如何運作與被使用的研究，本質上是**跨領域**的（Koshman & Zubkova, 2026），因此歡迎任何領域的貢獻。以下兩篇回顧說明了 TTW 在這些研究中的位置：

- **AI 在專案管理中已經做得好的部分。** Adamantiadou 與 Tsironis（2025）發現，機器學習、深度學習與混合模型大幅擴展了專案管理的能力，改善了**成本估算、時程預測與風險分析**。TTW 認真看待這一點：它在航向之內自動化重複性工作。
  *透明度說明：我們依據 Koshman & Zubkova（2026）的轉述引用此發現；原始文章的書目資料已透過其 DOI 核對。*
- **仍未解決的部分。** Koshman 與 Zubkova（2026）回顧了 97 篇文獻，發現 AI 模型難以適應變動的專案條件、很少以初始資料加以驗證，且在專案後檢討等階段的研究仍然很少。TTW 正是圍繞這些缺口打造的：方向由專案經理掌握、航向以證據核對，而航行日誌支援專案後檢討。

| 年份 | 文獻 | 與本專案的關係 |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | 未經授權的變更會傷害專案 → 每次方向調整都須確認並記錄 |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | 模型最能利用長脈絡的開頭與結尾 → 在每次提示旁附上簡短的航向 |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM 評審需要明確的準則 → 在做出任何判定前先設定標準 |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | 模型走錯路後難以恢復 → 一開始就設定航向 |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | 提醒能降低偏移 → 每次提示都有守望者 |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | AI 改善估算、預測與風險分析 → 自動化重複性工作 |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | 適應性、驗證與專案後檢討仍未解決 → 人在迴路中 |

完整的附註清單與每項來源對設計的影響，請見 [docs/methods.md](../../docs/methods.md)（英文）。專案如何開始、由誰決定，請見 [GOVERNANCE.md](../../GOVERNANCE.md)。

<details>
<summary><b>完整參考文獻</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- 其他來源：[docs/methods.md](../../docs/methods.md)。

</details>

## 貢獻方式

| 貢獻 | 位置 |
|---|---|
| 新領域的**視角**（例如活動、營建、非營利計畫、產品設計） | `skills/checkwatch/references/lenses/` |
| 由母語人士進行的**翻譯校訂** | `i18n/<lang>/`（README、QUICKSTART、CONTRIBUTING） |
| 新的**評估案例**（一個提示加上預期行為） | `skills/<skill>/evals/evals.json` |
| **錯誤回報**或想法 | [Issues](https://github.com/Icharu/travelerswatch/issues)。請使用範本。 |
| **安全問題** | **不要**發在 issues。請見 [SECURITY.md](../../SECURITY.md)。 |

## 新增視角

1. 複製一個現有視角（例如 `project-management.md`）為 `lenses/<領域>.md`。
2. 保留相同的四個標題，讓 skill 能以相同方式使用任何視角：
   - **How the sections read in this field**：以表格改寫脈絡、限制、問題、工具
   - **Default criteria**：4–8 項*可觀察*的準則（見 `references/standards.md`）
   - **Drift signals**：在這個領域裡偏離路線是什麼樣子
   - **Typical tools**
3. **用你自己的話**撰寫準則。不要貼上付費或受版權保護標準的文字；只寫出名稱並引用章節。
4. 將視角加入 `skills/checkwatch/SKILL.md`（步驟 A1）的清單，以及 README 的 *Lenses* 區段。
5. 在 `skills/checkwatch/evals/evals.json` 中至少新增一個使用該視角的評估案例。

## 修改 skills

- 讓每個 `SKILL.md` 保持簡短、以決策為導向；細節放在 `references/`。
- 不要削弱核心規則（[GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)）：方向調整、結案或接受矛盾**只能由專案經理確認**；**Path log 與檢查點記錄只能追加**；航向**不採用全自動工作階段**（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）；**不在使用者的儲存庫之外保存任何資料**。
- 只使用標準的 Agent Skills frontmatter（`name`、`description`、`license`、`metadata`），讓 skills 保持可攜。
- 當行為變更改動了設計決策時，請在 `docs/adr/` 中以 ADR 說明。

## 修改 hook

- 只使用 bash（≥ 3.2，為了 macOS）與 awk；git 為選用。優先使用 bash 內建功能，而非額外的程序；航行日誌以單次 `awk` 解析。
- 它必須永遠以 0 結束；沒有航行日誌或航向為 `closed` 時保持沉默；限制輸出長度；不進行網路連線；除了 `.watch/.state` 之外不寫入任何檔案。
- **先寫會失敗的測試**（`tests/watchman.test.sh`），再讓它通過，並測量修改前後每次提示的耗時：

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## 修改航行日誌格式

hook 會解析固定標籤：`## Status`、`- **Bearing:**`（`confirmed` / `under review …` / `closed …`）、`- **Checkpoint cadence:**`（`every N commits or M sessions` / `off`）、`- **Last checkpoint:** <date> @ <sha>`、`**Boundary notes:**`、Relations 中含有 "accepted" 的行，以及 `## Path log` 標題。`## Checkpoint log` 只由 skills 讀取。要修改這些標籤，必須同時修改 hook、範本（`skills/checkwatch/assets/WATCH.md`）、skills 與測試。

## 翻譯

根目錄中的英文檔案（`README.md`、`QUICKSTART.md`、`CONTRIBUTING.md`）為正式版本。翻譯依語言集中放在 `i18n/<lang>/`，讓根目錄保持整潔。修改英文檔案時，請在 pull request 中註明哪些翻譯因此過時。譯者：請保持語言列、連結（相對於 `i18n/<lang>/`，例如 `../../docs/tale.md`）、徽章、指令與 shell 程式碼區塊完全相同（*快速範例*中的對話可以翻譯）。請更新檔案頂端的「譯自」說明。阿拉伯文：正文放在 `<div dir="rtl">` 內，程式碼區塊放在外面。

## Pull requests

1. Fork 後建立分支：`feat/<主題>`、`fix/<主題>`、`docs/<主題>` 或 `lens/<領域>`。
2. 每個 pull request 只聚焦一項變更。
3. 若你有 Claude Code，請執行 `bash tests/watchman.test.sh` 與 `claude plugin validate .`。
4. 在 [CHANGELOG.md](../../CHANGELOG.md) 的 **Unreleased** 下新增一筆。
5. 使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式的訊息（`feat:`、`fix:`、`docs:`）。

提交貢獻即表示你同意你的貢獻以與儲存庫其他部分相同的條款授權：[CC BY-NC 4.0](../../LICENSE)。
