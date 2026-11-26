<!-- lang-bar -->
[English](../../CONTRIBUTING.md) · [Português (Brasil)](../pt-BR/CONTRIBUTING.md) · [Español](../es/CONTRIBUTING.md) · [繁體中文](../zh-Hant/CONTRIBUTING.md) · [简体中文](../zh-Hans/CONTRIBUTING.md) · **日本語** · [العربية](../ar/CONTRIBUTING.md)

> `CONTRIBUTING.md`（v1.2.0、2026-11-26）からの翻訳です。機械支援による翻訳のため、正式な版は英語版です。

# The Traveler's Watch への貢献

旅人が道を外れないよう手伝ってくださり、ありがとうございます。規模を問わず、どんな貢献も歓迎します。

## このプロジェクトが生まれた背景

TTW は、利用者と貢献者が変更を加える前に、このプロジェクトがなぜ生まれたのかを理解することを勧めています。設計の土台は、言語モデルが長い作業の中でどのようにずれていくか、そして AI がプロジェクトマネジメントをどう変えつつあるかについての、およそ**五年間の研究（2021〜2026 年）**と、それ以前のスコープクリープ（*scope creep*）に関する一つの研究です。

現代社会における AI の働きと利用に関する研究は、本質的に**学際的**です（Koshman & Zubkova, 2026）。そのため、どの分野からの貢献も歓迎します。二つのレビューが、その研究の中での TTW の位置を示しています。

- **AI がプロジェクトマネジメントですでにうまくできていること。** Adamantiadou と Tsironis（2025）は、機械学習、深層学習、ハイブリッドモデルがプロジェクトマネジメントの可能性を大きく広げ、**コスト見積もり、スケジュール予測、リスク分析**を改善したと報告しています。TTW はこれを真剣に受け止め、針路の範囲内で反復作業を自動化します。
  *透明性に関する注記：この知見は Koshman & Zubkova（2026）での紹介に基づいて引用しています。原論文の書誌情報は DOI で確認しました。*
- **まだ解決されていないこと。** Koshman と Zubkova（2026）は 97 件の文献をレビューし、AI モデルが変化するプロジェクトの状況にうまく適応できないこと、初期データに照らした検証がほとんどされていないこと、プロジェクト事後レビューなどの段階での研究が少ないことを示しました。TTW はこれらの空白を中心に作られています。方向はプロジェクトマネージャーが持ち、針路は証拠と照らし合わされ、航海日誌がプロジェクト事後レビューを支えます。

| 年 | 文献 | ここで重要な理由 |
|---|---|---|
| 2020 | Komal et al., [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098) | 承認のない変更はプロジェクトを損なう → すべての針路変更を確認し記録する |
| 2024 | Liu et al., [*Lost in the Middle*](https://doi.org/10.1162/tacl_a_00638) | モデルは長いコンテキストの両端をよく使う → 各プロンプトのそばに短い針路を置く |
| 2024 | [*A Survey on LLM-as-a-Judge*](https://arxiv.org/abs/2411.15594) | LLM の評価者には明示的な基準が必要 → 判定の前に基準を決める |
| 2025 | Laban et al., [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120) | モデルは道を誤ると立ち直れない → 最初に針路を決める |
| 2025 | Dongre et al., [*Drift No More?*](https://arxiv.org/abs/2510.07777) | リマインダーはずれを減らす → プロンプトごとの見張り番 |
| 2025 | Adamantiadou & Tsironis, [*Leveraging AI in Project Management*](https://doi.org/10.3390/computers14020066) | AI は見積もり・予測・リスク分析を改善する → 反復作業を自動化する |
| 2026 | Koshman & Zubkova, [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23) | 適応性・検証・事後レビューは未解決 → 人間が関与する |

各情報源と設計上の帰結をまとめた注釈付きの完全なリストは [docs/methods.md](../../docs/methods.md)（英語）にあります。プロジェクトの始まりと、誰が決めるかは [GOVERNANCE.md](../../GOVERNANCE.md) にあります。

<details>
<summary><b>参考文献（全文）</b></summary>

- Adamantiadou, D. S., & Tsironis, L. (2025). Leveraging artificial intelligence in project
  management: A systematic review of applications, challenges, and future directions. *Computers*,
  14(2), 66. https://doi.org/10.3390/computers14020066
- Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
  Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23
- その他の情報源：[docs/methods.md](../../docs/methods.md)。

</details>

## 貢献の方法

| 貢献 | 場所 |
|---|---|
| 新しい分野の**レンズ**（例：イベント、建設、非営利プログラム、プロダクトデザイン） | `skills/checkwatch/references/lenses/` |
| ネイティブスピーカーによる**翻訳レビュー** | `i18n/<lang>/`（README、QUICKSTART、CONTRIBUTING） |
| 新しい**評価ケース**（プロンプトと期待する振る舞い） | `skills/<skill>/evals/evals.json` |
| **バグ報告**やアイデア | [Issues](https://github.com/Icharu/travelerswatch/issues)。テンプレートを使ってください。 |
| **セキュリティの問題** | issues には**書かない**でください。[SECURITY.md](../../SECURITY.md) を参照。 |

## レンズの追加

1. 既存のレンズ（例：`project-management.md`）を `lenses/<分野>.md` としてコピーします。
2. スキルがどのレンズも同じように使えるよう、同じ四つの見出しを残します：
   - **How the sections read in this field**：コンテキスト・制約・課題・ツールを言い換える表
   - **Default criteria**：4〜8 個の*観察可能な*基準（`references/standards.md` を参照）
   - **Drift signals**：この分野で道を外れるとはどういうことか
   - **Typical tools**
3. 基準は**自分の言葉で**書いてください。有料または著作権のある規格の文章を貼り付けず、名前とセクションの参照だけにします。
4. レンズを `skills/checkwatch/SKILL.md`（ステップ A1）の一覧と、README の *Lenses* セクションに追加します。
5. そのレンズを使う評価ケースを `skills/checkwatch/evals/evals.json` に少なくとも一つ追加します。

## スキルの変更

- 各 `SKILL.md` は短く、判断を中心に保ち、詳細は `references/` に置きます。
- 中核となるルールを弱めないでください（[GOVERNANCE.md](../../GOVERNANCE.md#how-decisions-are-made)）：針路変更、終了、受け入れた矛盾を**確認できるのはプロジェクトマネージャーだけ**。**Path log とチェックポイント記録は追記のみ**。針路について**完全自動のセッションは行わない**（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）。利用者のリポジトリの外に**データを保存しない**。
- スキルの移植性を保つため、標準の Agent Skills frontmatter（`name`、`description`、`license`、`metadata`）だけを使います。
- 振る舞いの変更が設計判断を変える場合は、`docs/adr/` に ADR として説明します。

## hook の変更

- bash（macOS のため 3.2 以上）と awk のみ。git は任意です。追加のプロセスより bash の組み込み機能を優先し、航海日誌は `awk` の一回のパスで解析します。
- 常に終了コード 0 で終わること、航海日誌がないときや針路が `closed` のときは何も出力しないこと、出力量に上限を設けること、ネットワーク通信をしないこと、`.watch/.state` 以外に何も書き込まないこと。
- **まず失敗するテストを** `tests/watchman.test.sh` に書き、それを通してから、変更前後のプロンプトあたりの時間を測ります：

  ```bash
  bash tests/watchman.test.sh
  python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir> [...]
  ```

## 航海日誌の形式の変更

hook は次のラベルを厳密に解析します：`## Status`、`- **Bearing:**`（`confirmed` / `under review …` / `closed …`）、`- **Checkpoint cadence:**`（`every N commits or M sessions` / `off`）、`- **Last checkpoint:** <date> @ <sha>`、`**Boundary notes:**`、"accepted" を含む Relations の行、そして `## Path log` 見出し。`## Checkpoint log` はスキルだけが読みます。これらを変えるときは、hook、テンプレート（`skills/checkwatch/assets/WATCH.md`）、スキル、テストを必ず一緒に変えてください。

## 翻訳

ルートにある英語のファイル（`README.md`、`QUICKSTART.md`、`CONTRIBUTING.md`）が正式版です。ルートが散らからないよう、翻訳は言語ごとに `i18n/<lang>/` にまとめています。英語のファイルを変更したときは、どの翻訳が古くなったかを pull request に書いてください。翻訳者の方へ：言語バー、リンク（`i18n/<lang>/` からの相対パス。例：`../../docs/tale.md`）、バッジ、コマンド、シェルのコードブロックはそのままにしてください（*簡単な例*の会話は翻訳して構いません）。ファイル冒頭の「翻訳元」の注記を更新してください。アラビア語：本文は `<div dir="rtl">` の中に、コードブロックはその外に置きます。

## Pull request

1. フォークしてブランチを作ります：`feat/<内容>`、`fix/<内容>`、`docs/<内容>`、`lens/<分野>`。
2. 一つの pull request は一つの変更に絞ります。
3. Claude Code があれば `bash tests/watchman.test.sh` と `claude plugin validate .` を実行します。
4. [CHANGELOG.md](../../CHANGELOG.md) の **Unreleased** に項目を追加します。
5. [Conventional Commits](https://www.conventionalcommits.org/) 形式のメッセージ（`feat:`、`fix:`、`docs:`）を使います。

貢献することで、あなたの貢献がリポジトリのほかの部分と同じ条件でライセンスされることに同意したものとみなされます：[CC BY-NC 4.0](../../LICENSE)。
