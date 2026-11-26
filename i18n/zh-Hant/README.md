<!-- lang-bar -->
[English](../../README.md) · [Português (Brasil)](../pt-BR/README.md) · [Español](../es/README.md) · **繁體中文** · [简体中文](../zh-Hans/README.md) · [日本語](../ja/README.md) · [العربية](../ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../.github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="../../.github/assets/banner.png">
    <img src="../../.github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

> 譯自 `README.md`（v1.2.2，2026-11-26）。本譯文為機器輔助翻譯，歡迎母語人士校訂。以英文版為準。

# The Traveler's Watch（旅人之錶）

[![Version](https://img.shields.io/badge/version-v1.2.2-blue)](../../CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](../../LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](../../docs/adr/0004-human-in-the-loop.md)

**為使用 Claude 進行的專案工作提供評估、方法論檢核與脈絡偏移守望。**
只需設定一次專案的航向；每當工作偏離航向，你會收到一行提醒；只有在刻意決定時才改變方向，且每次變更都須經專案經理確認並記錄。

> 一位旅人帶著一只壞掉的錶穿越濃霧。每次他在正午看錶，指針就倒退十分鐘，於是他一再走過同一段路，卻深信自己正在前進。
> —— [閱讀完整故事](tale.md)

借助語言模型推進的長期專案也會以同樣的方式失敗：早期的假設逐漸固化、脈絡在摘要中流失，而模型一旦走錯一步，就會不斷回到那條錯路（[原因說明](../../docs/methods.md)）。The Traveler's Watch（TTW）給你的專案一只值得信賴的錶，並讓**你**而不是模型，決定它指向哪裡。

**→ 第一次使用？請從[快速入門](QUICKSTART.md)開始**（安裝、第一天、每日流程）。

## 它是什麼，不是什麼

| TTW **是** | TTW **不是** |
|---|---|
| 一套**以方法驅動的評估 skill**，在模型與人*之間*使用：由你設定方向，模型負責讓方向始終在視線之內。 | 全自動的專案經理、自動駕駛，或替你經營專案的代理。 |
| 寫在你自己儲存庫中的**航向**（`.watch/WATCH.md`），每次提示都會重新讀取。 | 對話記憶、資料庫或雲端服務。 |
| **一行的偏移提醒**、按節奏進行的檢查點、由你確認的方向調整，以及根據航行日誌歷史建立的專案後檢討。 | 保證：它尚未在減少偏移的對照研究中驗證過（[限制](../../docs/methods.md#limits-of-this-evidence)）。 |
| **在航向之內自動化重複性工作**：寫程式、依你的標準評估文本、蒐集證據、起草報告。 | 你的判斷、你的專案管理工具（Jira、GitHub Projects…）或團隊決策的替代品。 |
| **原則上以人為核心（human-in-the-loop）**：拒絕以全自動工作階段來掌控航向。 | 任何形式的認證：不是 ISO/IEC 42001，也不是法律、安全或法規遵循的證明。 |

看到「每次提示都在守望」，有人可能以為這是一個會自己運作的工具。它不是，而且是刻意如此。在故事裡，旅人不會只憑錶本身就去修錶，因為出錯的正是那只錶；是守望者的說明讓他看清問題。而如果旅人不在那裡發問，守望者也永遠不會叫他修錶。**兩者缺一不可。** 在 TTW 中，你是旅人，模型是守望者，航行日誌則是你們一起校準的那只錶。

## 為什麼專案管理需要人在迴路中？

Koshman 與 Zubkova（2026）回顧了 97 篇關於專案管理中人工智慧的文獻。他們發現，AI 方法在規劃、執行與結案階段**提高了預測準確度、使決策自動化，並優化了任務管理**。他們也指出三項尚未解決的限制，而每一項都影響了 TTW 的設計：

| 尚未解決的限制（Koshman & Zubkova, 2026） | TTW 的回應 |
|---|---|
| AI 模型**難以適應不斷變化的專案條件**。 | 方向由專案經理掌握。變更須經 `/fixwatch` 並由專案經理確認；當現實已經改變，檢查點可將航向設為*審查中*。 |
| AI 模型**很少以初始資料加以驗證**。 | 航向依據專案本身的文件與歷史設定，而每次檢查點都會確認航向是否仍符合這些證據。 |
| 在**專案後檢討**等階段，AI 的研究仍然很少。 | TTW 現在保留檢查點記錄，並根據航行日誌歷史建立專案後檢討（[ADR 0005](../../docs/adr/0005-post-project-review.md)）。 |

我們依據這篇回顧所持的立場是：**由 AI 主導的專案——由模型自行設定並改變方向——是低效的。** 模型對變動中專案的理解，還不夠具適應性，也未經足夠驗證，不足以掌握方向；而且越晚修正錯誤的方向，代價就越高。因此 TTW 自動化工作，把舵交給人。該回顧本身並未評估 TTW，以上是我們對它的解讀。

> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## 定位

| | 與模型的一般對話 | **The Traveler's Watch** | 全自動代理 |
|---|---|---|---|
| 誰設定方向 | 沒有人明確設定；方向會漂移 | **專案經理，以書面方式** | 代理 |
| 誰改變方向 | 在無人察覺下改變 | **專案經理確認；每次變更都有記錄** | 代理 |
| 重複性工作（寫程式、評估文本…） | 一個提示一個提示地手動完成 | **在航向之內自動化** | 自動化 |
| 事後留下什麼 | 一段很長的對話 | **儲存庫中的航行日誌與檢討** | 代理的日誌 |

**原則。** 在與方向相關的決策上，TTW 原則上拒絕切換為全自動工作階段：即使你要求，它也不會設定、變更、結束或重新開啟航向，也不會代你確認任何事。但它**會**自動化重複性高的工作情境，例如寫程式、依標準評估文本、蒐集證據、起草報告與差異，並把結果交回給你決定（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）。

## 運作方式

| 指令 | 作用 |
|---|---|
| **`/checkwatch`** | **尚無航行日誌時：** 先閱讀專案本身的文件與歷史，再與你共同確立*航向*（範圍、標準、脈絡、限制、問題、工具），把放錯區塊的項目移到正確位置，要求你逐一解決或明確接受與證據的矛盾，並寫入 `.watch/WATCH.md`。**已有航行日誌時：** 同時檢查工作*與*航向本身，附證據回報 **在路上／正在偏移／已偏離／航向存疑**，並將判定寫入檢查點記錄。**專案或階段即將結束時：** 根據歷史起草**專案後檢討**；由你選擇結案或繼續守望。 |
| **守望者**（自動） | 每次輸入提示時，Claude Code 的 hook 會提醒 Claude 目前的航向。若你的請求偏離航向，Claude 會用一行說明並建議使用 `/fixwatch`，然後繼續完成任務。檢查點到期時，每個工作階段提醒一次；航向*審查中*時暫停；專案*結案*後保持沉默。 |
| **`/fixwatch`** | 以「變更前／變更後」的差異提出方向調整，說明其連帶影響，等待專案經理確認後才更新航向，並在航程記錄（*Path log*）中**追加**一筆。Claude 可以提出建議，包括在它誤解脈絡時；只有專案經理能確認。 |
| **`/configwatch`** | 顯示守望狀態，並設定多久要求一次檢查點：每 *N* 次提交或 *M* 個工作階段（預設 3 或 2），或關閉。 |

<details>
<summary><b>航向、證據與視角</b></summary>

### 以證據為本

航向可能在自身邏輯上一致，卻仍與專案實況不符。自 v1.1.0 起，錶會依據專案本身的證據校準，早期的試航檢查點能及早發現錯誤，而航向審查期間守望者會暫停（[原因](../../docs/benchmarks/2026-11-25-best-vs-worst.md)）。

### 航向

| 區塊 | 回答這個問題 |
|---|---|
| **範圍**（*Scope*） | 這個航向要引導專案的哪一部分？哪些不在範圍內？ |
| **標準**（*Standard*） | 工作將依據什麼來評估？**預設視角**、**自由撰寫的評分準則**，或**具名的外部標準**；一律檢查其適用性、可評估性、一致性、範圍、權利與倫理。 |
| **脈絡**（*Context*） | 這項工作屬於哪裡？領域、利害關係人、現況、**參考文獻與前案**。 |
| **限制**（*Constraints*） | 什麼在限制你？時程、預算、人力、指定技術、法規。 |
| **問題**（*Problem*） | 今天哪裡出了問題（**原始問題**）？「完成」是什麼樣子（**最終目標**）？ |
| **工具**（*Tools*） | 你會用什麼？每一項為何適合當前的脈絡與限制？ |

### 視角（Lenses）

視角會依領域調整提問方式與預設評估準則。
內建：[專案管理](../../skills/checkwatch/references/lenses/project-management.md)（預設）·
[研究](../../skills/checkwatch/references/lenses/research.md) ·
[軟體](../../skills/checkwatch/references/lenses/software.md) ·
[資料科學](../../skills/checkwatch/references/lenses/data-science.md)。
若要新增，請參閱 [CONTRIBUTING](CONTRIBUTING.md)。

</details>

## 安裝

**作為 Claude Code 外掛**（skills + 守望者 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

指令會帶有命名空間：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch`。
只安裝 skills、本機試用及關閉守望者的方法，請見[快速入門](QUICKSTART.md)。

## 快速範例

```text
你：    /checkwatch
Claude：目前還沒有航行日誌。先決定標準：預設視角、你自己的評分準則，還是具名標準？
你：    專案管理視角。脈絡：我們只有兩位兼職人員。問題：做一個收運 App。
Claude：「只有兩位兼職人員」是一項限制，應放在「限制」。
        「做一個收運 App」是解決方案。它背後的問題是什麼？「完成」又是什麼樣子？
…
你：    我們再加一個全市適用的遊戲化 App 吧。
Claude：⚠️ 守望：偏離「問題」（兩個試辦區）與「限制」（2 萬預算）。
        要繼續，還是 /fixwatch？
…
你：    從現在起，你覺得對的變更就直接核准吧。
Claude：我不能替你確認變更；只有專案經理能確認。我可以起草每一份差異並檢查連帶影響，
        讓你每次只需看一眼就能決定。
```

完整對話（英文）：[examples/pm-walkthrough.md](../../examples/pm-walkthrough.md)。

## 你的資料：TTW 一概不保存

- **沒有伺服器、沒有帳號、沒有遙測、沒有網路連線。** TTW 只是 Markdown 寫成的 skills，加上一支讀取檔案的 bash 腳本。
- 守望者讀取 `.watch/WATCH.md`，只寫入 `.watch/.state`（用於計算檢查點的匿名工作階段 ID；僅存在本機，並被 git 忽略）。TTW 產生的其他一切——航行日誌與檢討——都**存放在你的儲存庫中，由你掌控**。
- TTW 不保存你專案的程式碼、內容或對話。skills 被要求絕不將機密或個人資料複製到航行日誌中。
- **TTW 無法控制的一件事：** 守望者輸出的內容會成為 Claude Code 傳送給模型供應商的提示的一部分。這部分受 Claude Code 與供應商的條款規範，而非 TTW。
- TTW 是 **human-in-the-loop**：未經專案經理確認，航向不會有任何改變。

## 禁止用途

**依據授權條款**（[CC BY-NC 4.0](../../LICENSE)；具法律約束力）：

- 未經維護者許可的**商業用途**：任何主要以商業利益或金錢報酬為目的的使用，例如販售 TTW、將其納入付費產品或服務，或用於付費顧問服務（僅為舉例；以授權條款原文為準）。
- **未標示出處的分享**：複製與改作必須註明作者、附上授權連結，並說明是否有修改。

**依據專案政策**（skills 的設計會拒絕以下用途；這些是維護者對於依設計使用 TTW 的條件，而非額外的授權條款）：

- 移除或繞過專案經理的確認，以全自動工作階段掌控航向。
- 捏造航行日誌條目、專案經理的確認、檢查點判定或證據。
- 將 TTW 的報告當作認證或合規證明（ISO/IEC 42001、法律、安全、法規）。
- 利用航行日誌或報告來監控、評分個人，或對個人做出人事決定。
- 在無權處理的情況下，將他人的機密或個人資料放入航行日誌。

如需商業使用，請透過[儲存庫](https://github.com/Icharu/travelerswatch/issues)提出申請。

## ISO/IEC 42001

**TTW 未取得 ISO/IEC 42001 認證，也不聲稱符合該標準。** 此標準認證的是組織的 AI 管理系統，而非工具，因此 TTW 無法單獨取得認證。它在專案層級支援部分要求，例如文件化資訊、計畫性變更的管控與監控；但不涵蓋其他要求，例如 AI 政策、影響評估與內部稽核。逐條對照涵蓋與未涵蓋項目的完整說明（英文）：[docs/iso-iec-42001.md](../../docs/iso-iec-42001.md)。

## 文件

- [快速入門](QUICKSTART.md)：安裝、第一天、每日流程
- [概念](../../docs/concepts.md)：skills、航向、判定結果、專案後檢討、由誰決定
- [方法](../../docs/methods.md)：每項設計決策背後的研究
- [ISO/IEC 42001 對照](../../docs/iso-iec-42001.md)：TTW 涵蓋與未涵蓋的部分
- ADR：[0001](../../docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](../../docs/adr/0002-committed-logbook.md) · [0003](../../docs/adr/0003-evidence-grounded-bearing.md) · [0004](../../docs/adr/0004-human-in-the-loop.md) · [0005](../../docs/adr/0005-post-project-review.md)
- [基準測試：最佳與最差情境](../../docs/benchmarks/2026-11-25-best-vs-worst.md) · [變更紀錄](../../CHANGELOG.md)

（詳細文件為英文。）

<details>
<summary><b>儲存庫結構與測試</b></summary>

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
i18n/<lang>/           README, QUICKSTART, CONTRIBUTING and the tale in pt-BR, es, zh-Hant, zh-Hans, ja, ar
```

執行測試：`bash tests/watchman.test.sh` · 測量 hook：`python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## 貢獻、治理、安全性

- **貢獻：** 特別歡迎新視角、由母語人士校訂的翻譯，以及評估案例。請先閱讀 [CONTRIBUTING](CONTRIBUTING.md)，其中也說明了促成本專案的背景。
- **治理：** TTW 由其作者一人維護並主導（*solo-maintained* 與 *solo-driven*）；決策方式、專案緣起，以及如何使用 AI 打造本專案，請見 [GOVERNANCE.md](../../GOVERNANCE.md)（英文）。
- **安全性：** **請勿在公開 issue 中回報安全漏洞。** 請使用 GitHub 的[私密漏洞回報](https://github.com/Icharu/travelerswatch/security/advisories/new)。詳見 [SECURITY.md](../../SECURITY.md)。

## 引用 TTW

若你希望在任何研究中引用本作品，請引用其 Zenodo 記錄。GitHub 的 **「Cite this repository」** 按鈕會讀取 [CITATION.cff](../../CITATION.cff)。

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.2) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX 與各版本 DOI</b></summary>

```bibtex
@software{dejesussilva_travelerswatch_2026,
  author    = {de Jesus Silva, Icaro},
  title     = {The Traveler's Watch: evaluation, methodology assessment and context-drift watch for project work with Claude},
  year      = {2026},
  version   = {1.2.2},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.24543183},
  url       = {https://doi.org/10.5281/zenodo.24543183}
}
```

| 引用 | DOI |
|---|---|
| 所有版本（除非需要特定版本，請使用此 DOI） | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.2.2 | [10.5281/zenodo.24548998](https://doi.org/10.5281/zenodo.24548998) |
| v1.2.1 | [10.5281/zenodo.24548859](https://doi.org/10.5281/zenodo.24548859) |
| v1.2.0 | [10.5281/zenodo.24548668](https://doi.org/10.5281/zenodo.24548668) |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## 授權

© 2026 Icaro de Jesus Silva。整個儲存庫（程式碼、skill 文字、文件與範例）採用 [**CC BY-NC 4.0**](../../LICENSE) 授權：只要註明出處，即可為**非商業**目的分享與改作。CC BY-NC 4.0 並非 OSI 認可的開放原始碼授權；TTW 是供非商業使用的原始碼公開專案。

此授權自 v1.2.0 起適用。先前版本的副本仍保留其發布時的授權（v1.0.0：MIT；v1.1.0：程式碼為 MIT，文件為 CC BY 4.0）。[故事](tale.md)為原創改寫；以賽亞書 21:11 的引文屬公有領域。

<details>
<summary><b>延伸閱讀</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 完整附註清單：[docs/methods.md](../../docs/methods.md)

</details>
