<!-- lang-bar -->
[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · **繁體中文** · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [العربية](README.ar.md)

> 譯自 `README.md` v1.1.0（2026-11-25）。本文為機器輔助翻譯，歡迎母語人士協助校訂；以英文版為準。

# The Traveler's Watch（旅人之錶）

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](CHANGELOG.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![DOI](https://img.shields.io/badge/DOI-pending%20(Zenodo)-lightgrey)](CITATION.cff)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**為使用 Claude 進行的專案工作提供評估、方法論檢核與脈絡偏移守望。**
只需設定一次專案的航向；每當工作偏離航向，你會收到一行提醒；只有在刻意決定時才改變方向，且每次變更都須經專案經理確認並記錄。

> 一位旅人帶著一只壞掉的錶穿越濃霧。每次他在正午看錶，指針就倒退十分鐘，於是他一再走過同一段路，卻深信自己正在前進。
> —— [閱讀完整故事](docs/tale.md)

借助語言模型推進的長期專案也會以同樣的方式失敗：早期的假設逐漸固化、脈絡在摘要中流失，而模型一旦走錯一步，就會不斷回到那條錯路（[原因說明](docs/methods.md)）。The Traveler's Watch 給你的專案一只值得信賴的錶。

## 運作方式

| 指令 | 作用 |
|---|---|
| **`/checkwatch`** | **尚無航行日誌時：** 先閱讀專案本身的文件與歷史，再與你共同確立*航向*（範圍、標準、脈絡、限制、問題、工具），把放錯區塊的項目移到正確位置，要求你逐一解決或明確接受與證據的矛盾，並寫入 `.watch/WATCH.md`。**已有航行日誌時：** 同時檢查工作*與*航向本身，並附證據回報 **在路上／正在偏移／已偏離／航向存疑**。 |
| **守望者**（自動） | 每次輸入提示時，Claude Code 的 hook 會提醒 Claude 目前的航向。若你的請求偏離航向，Claude 會用一行說明並建議使用 `/fixwatch`，然後繼續完成任務。檢查點到期時，每個工作階段提醒一次；航向*審查中*時暫停。 |
| **`/fixwatch`** | 以「變更前／變更後」的差異提出方向調整，說明其連帶影響，等待專案經理確認後才更新航向，並在航程記錄（*Path log*）中**追加**一筆。Claude 可以提出建議，包括在它誤解脈絡時；只有專案經理能確認。 |
| **`/configwatch`** | 顯示守望狀態，並設定多久要求一次檢查點：每 *N* 次提交或 *M* 個工作階段（預設 3 或 2），或關閉。 |

### 以證據為本

航向可能自身前後一致，卻與專案實況不符。自 v1.1.0 起，這只錶會以專案本身的證據校準，早期的檢查點能及早發現錯誤，航向審查中時守望者會暫停（[原因](docs/benchmarks/2026-11-25-best-vs-worst.md)）。

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
內建：[專案管理](skills/checkwatch/references/lenses/project-management.md)（預設）·
[研究](skills/checkwatch/references/lenses/research.md) ·
[軟體](skills/checkwatch/references/lenses/software.md) ·
[資料科學](skills/checkwatch/references/lenses/data-science.md)。
若要新增，請參閱 [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens)。

## 安裝

**作為 Claude Code 外掛**（skills + 守望者 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

指令會帶有命名空間：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch`。

**只安裝 skills**（Claude Code 或任何支援 [Agent Skills](https://agentskills.io/) 的代理；不含 hook）：

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/
```

指令即為 `/checkwatch`、`/fixwatch` 與 `/configwatch`。沒有 hook 時，請在每次工作階段開始時執行 `/checkwatch`。

**不安裝、在本機試用：** `claude --plugin-dir ./travelerswatch`

**暫時關閉守望者：** `export TRAVELERSWATCH_DISABLE=1`

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
```

完整對話（英文）：[examples/pm-walkthrough.md](examples/pm-walkthrough.md)。

## 儲存庫結構

```text
.claude-plugin/        外掛與 marketplace 清單
skills/checkwatch/     SKILL.md · references/（標準、區塊、關係、視角）· assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh（僅需 bash + awk）
tests/                 watchman.test.sh
docs/                  故事 · 概念 · 方法（文獻）· adr/
examples/              專案管理實例
```

執行測試：`bash tests/watchman.test.sh` · 測量 hook：`python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

## 文件

- [概念](docs/concepts.md)：skills、航向、判定結果、由誰決定
- [方法](docs/methods.md)：每項設計決策背後的研究
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md) · [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)
- [基準測試：最佳與最差情境](docs/benchmarks/2026-11-25-best-vs-worst.md)：v1.0.0 漏掉了什麼、v1.1.0 修正了什麼、每次提示的 hook 耗時
- [變更紀錄](CHANGELOG.md)

（詳細文件為英文。）

## 貢獻

歡迎各種貢獻，特別是其他領域的**新視角**、由母語人士校訂的翻譯，以及新的評估案例。提交 pull request 前請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 安全性

**請勿在公開 issue 中回報安全漏洞。** 請使用 GitHub 的[私密漏洞回報](https://github.com/Icharu/travelerswatch/security/advisories/new)（**Security** 分頁 → **Report a vulnerability**）。回應時間為盡力而為，並依嚴重程度而定。適用範圍、回應時間表及等待期間的建議，請見 [SECURITY.md](SECURITY.md)。

## 引用

若你在研究或教學中使用 The Traveler's Watch，請加以引用。GitHub 的 **「Cite this repository」** 按鈕會讀取 [CITATION.cff](CITATION.cff)。v1.0.0 發布後，將在此加入 Zenodo DOI。

## 授權

[MIT](LICENSE) © 2026 Icaro de Jesus Silva。[docs/tale.md](docs/tale.md) 中的故事為原創改寫；以賽亞書 21:11 的引文屬公有領域。

## 延伸閱讀

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 完整附註清單：[docs/methods.md](docs/methods.md)
