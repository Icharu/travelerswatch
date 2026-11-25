<!-- lang-bar -->
[English](README.md) · [Português (Brasil)](README.pt-BR.md) · [Español](README.es.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · **日本語** · [العربية](README.ar.md)

> `README.md` v1.1.0（2026-11-25）からの翻訳です。機械支援による翻訳のため、ネイティブスピーカーによるレビューを歓迎します。正式な版は英語版です。

# The Traveler's Watch（旅人の時計）

[![Version](https://img.shields.io/badge/version-v1.1.0-blue)](CHANGELOG.md)
[![License: MIT (code) + CC BY 4.0 (docs)](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE-docs)
[![DOI](https://img.shields.io/badge/DOI-pending%20(Zenodo)-lightgrey)](CITATION.cff)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)

**Claude と進めるプロジェクトのための、評価・方法論アセスメント・コンテキストのずれの見張り。**
プロジェクトの針路を一度決めれば、作業が針路から外れるたびに一行で知らせます。針路の変更は意図したときだけ行い、変更のたびにプロジェクトマネージャーの確認を得て記録します。

> ある旅人が、壊れた時計を頼りに濃い霧の中を進んでいた。正午に時計を見るたびに針が十分戻り、彼は前に進んでいると信じたまま、同じ道を何度も歩き続けた。
> —— [物語の全文を読む](docs/tale.md)

言語モデルと進める長期プロジェクトも同じように失敗します。初期の思い込みが固まり、コンテキストは要約の中で失われ、一度道を誤ったモデルは何度もその誤りに戻ってしまいます（[なぜ起きるのか](docs/methods.md)）。The Traveler's Watch は、あなたのプロジェクトに信頼できる時計を与えます。

## 仕組み

| コマンド | 内容 |
|---|---|
| **`/checkwatch`** | **航海日誌がまだない場合：** まずプロジェクト自身のドキュメントと履歴を読み、あなたと一緒に*針路*（範囲・基準・コンテキスト・制約・課題・ツール）を決め、誤ったセクションに書かれた項目を移し、証拠との矛盾を一つずつ解消または明示的に受け入れてもらったうえで `.watch/WATCH.md` を作成します。**航海日誌がある場合：** 作業*と*針路そのものの両方をチェックし、根拠とともに **順調／ずれ始めている／針路外／針路に疑義** を報告します。 |
| **見張り番**（自動） | プロンプトのたびに、Claude Code の hook が Claude に針路を思い出させます。依頼が針路から外れていれば、Claude は一行で指摘して `/fixwatch` を提案し、そのまま作業を続けます。チェックポイントの時期にはセッションごとに一度知らせ、針路が*レビュー中*の間は一時停止します。 |
| **`/fixwatch`** | 針路の変更を変更前／変更後の差分として提案し、ほかへの影響を示し、プロジェクトマネージャーの確認を待ってから針路を更新し、航路記録（*Path log*）に**追記**します。Claude は提案できます（自分がコンテキストを誤解していた場合も含む）が、確認できるのはプロジェクトマネージャーだけです。 |
| **`/configwatch`** | 見張りの状態を表示し、チェックポイントを求める頻度を設定します：*N* コミットまたは *M* セッションごと（既定は 3 または 2）、またはオフ。 |

### 証拠に基づく針路

針路は、それ自体では筋が通っていても、プロジェクトの実態とずれていることがあります。v1.1.0 からは、時計をプロジェクト自身の証拠に合わせ、早めのチェックポイントで誤りを早期に見つけ、針路がレビュー中の間は見張り番が一時停止します（[理由](docs/benchmarks/2026-11-25-best-vs-worst.md)）。

### 針路

| セクション | 答える問い |
|---|---|
| **範囲**（*Scope*） | この針路はプロジェクトのどの部分を導き、どの部分は対象外か？ |
| **基準**（*Standard*） | 作業を何に照らして評価するか？**レンズのプリセット**、**自由記述のルーブリック**、または**名前のある外部規格**。適合性・評価可能性・一貫性・範囲・権利・倫理を必ず確認します。 |
| **コンテキスト**（*Context*） | この作業はどこに属するか？分野、ステークホルダー、現状、**参考文献・先行事例**。 |
| **制約**（*Constraints*） | 何に縛られているか？期間、予算、人員、指定された技術、規制。 |
| **課題**（*Problem*） | 今何が問題か（**元の課題**）、そして「完了」とはどんな状態か（**最終目標**）。 |
| **ツール**（*Tools*） | 何を使うか、そしてそれぞれがコンテキストと制約に合う理由は何か。 |

### レンズ

レンズは、質問の仕方と既定の評価基準を分野に合わせて調整します。
同梱：[プロジェクトマネジメント](skills/checkwatch/references/lenses/project-management.md)（既定）·
[研究](skills/checkwatch/references/lenses/research.md) ·
[ソフトウェア](skills/checkwatch/references/lenses/software.md) ·
[データサイエンス](skills/checkwatch/references/lenses/data-science.md)。
追加するには [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-lens) を参照してください。

## インストール

**Claude Code プラグインとして**（スキル + 見張り番 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

コマンドは名前空間付きになります：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch`。

**スキルのみ**（Claude Code、または [Agent Skills](https://agentskills.io/) を読める任意のエージェント。hook なし）：

```bash
git clone https://github.com/Icharu/travelerswatch
cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/
```

コマンドは `/checkwatch`、`/fixwatch`、`/configwatch` になります。hook がない場合は、作業セッションの開始時に `/checkwatch` を実行してください。

**インストールせずにローカルで試す：** `claude --plugin-dir ./travelerswatch`

**見張り番を一時的に止める：** `export TRAVELERSWATCH_DISABLE=1`

## 簡単な例

```text
あなた：/checkwatch
Claude：まだ航海日誌がありません。まず基準です。レンズのプリセット、独自のルーブリック、名前のある規格のどれにしますか？
あなた：PM レンズで。コンテキスト：非常勤スタッフが2人しかいない。課題：回収アプリを作る。
Claude：「非常勤スタッフが2人しかいない」は制限なので「制約」に入ります。
        「回収アプリを作る」は解決策です。その背後にある課題は何で、「完了」とはどんな状態ですか？
…
あなた：市全体向けのゲーミフィケーションアプリも追加しよう。
Claude：⚠️ 見張り：「課題」（2つのパイロット地区）と「制約」（予算2万）から外れています。
        続けますか、それとも /fixwatch しますか？
```

セッション全体（英語）：[examples/pm-walkthrough.md](examples/pm-walkthrough.md)。

## リポジトリ構成

```text
.claude-plugin/        プラグインとマーケットプレイスのマニフェスト
skills/checkwatch/     SKILL.md · references/（基準、セクション、関係、レンズ）· assets/WATCH.md · evals/
skills/fixwatch/       SKILL.md · evals/
skills/configwatch/    SKILL.md · evals/
hooks/                 hooks.json · watchman.sh（bash + awk のみ）
tests/                 watchman.test.sh
docs/                  物語 · 概念 · 方法（文献）· adr/
examples/              PM セッションの実例
```

テストの実行：`bash tests/watchman.test.sh` · hook の計測：`python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

## ドキュメント

- [概念](docs/concepts.md)：スキル、針路、判定、誰が決めるか
- [方法](docs/methods.md)：各設計判断の背景にある研究
- [ADR 0001](docs/adr/0001-hook-for-per-prompt-watch.md) · [ADR 0002](docs/adr/0002-committed-logbook.md) · [ADR 0003](docs/adr/0003-evidence-grounded-bearing.md)
- [ベンチマーク：最良と最悪のケース](docs/benchmarks/2026-11-25-best-vs-worst.md)：v1.0.0 が見逃したもの、v1.1.0 で直したもの、プロンプトごとの hook の所要時間
- [変更履歴](CHANGELOG.md)

（詳細なドキュメントは英語です。）

## コントリビュート

貢献を歓迎します。特に、他分野向けの**新しいレンズ**、ネイティブスピーカーによる翻訳レビュー、新しい評価ケースを歓迎します。プルリクエストを送る前に [CONTRIBUTING.md](CONTRIBUTING.md) をお読みください。

## セキュリティ

**脆弱性を公開 issue で報告しないでください。** GitHub の[非公開の脆弱性報告](https://github.com/Icharu/travelerswatch/security/advisories/new)（**Security** タブ → **Report a vulnerability**）を使ってください。対応時間はベストエフォートで、深刻度によって異なります。対象範囲、対応時間の表、待っている間にできることは [SECURITY.md](SECURITY.md) を参照してください。

## 引用

研究や教育で The Traveler's Watch を使う場合は、引用をお願いします。GitHub の **「Cite this repository」** ボタンは [CITATION.cff](CITATION.cff) を読み込みます。v1.0.0 のリリース後、ここに Zenodo の DOI を追加します。

## ライセンス

© 2026 Icaro de Jesus Silva。**コード**（`hooks/`、`tests/`、およびすべての `.sh`・`.py`・`.json`・`.yml`・`.cff` ファイル）は [MIT](LICENSE) ライセンス、**ドキュメントとスキルの本文**（`skills/**/*.md`、`docs/`、`examples/`、各 README を含むすべての Markdown ファイル）は [CC BY 4.0](LICENSE-docs) ライセンスです。クレジットを表示すれば、自由に再利用・改変できます。v1.0.0 は引き続き全体が MIT ライセンスです。[docs/tale.md](docs/tale.md) の物語はオリジナルの再話です。イザヤ書 21:11 の引用はパブリックドメインです。

## 参考文献

- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 注釈付きの全リスト：[docs/methods.md](docs/methods.md)
