<!-- lang-bar -->
[English](../../README.md) · [Português (Brasil)](../pt-BR/README.md) · [Español](../es/README.md) · [繁體中文](../zh-Hant/README.md) · [简体中文](../zh-Hans/README.md) · **日本語** · [العربية](../ar/README.md)

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="../../.github/assets/banner-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="../../.github/assets/banner.png">
    <img src="../../.github/assets/banner.png" alt="The Traveler's Watch: an agent-driven skill for project management assessment, led by the human-in-the-loop principle and context-driven analysis" width="100%">
  </picture>
</p>

> `README.md`（v1.2.0、2026-11-26）からの翻訳です。機械支援による翻訳のため、ネイティブスピーカーによるレビューを歓迎します。正式な版は英語版です。

# The Traveler's Watch（旅人の時計）

[![Version](https://img.shields.io/badge/version-v1.2.0-blue)](../../CHANGELOG.md)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](../../LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24543183.svg)](https://doi.org/10.5281/zenodo.24543183)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-8A2BE2)](https://agentskills.io/)
[![Human in the loop](https://img.shields.io/badge/human-in%20the%20loop-orange)](../../docs/adr/0004-human-in-the-loop.md)

**Claude と進めるプロジェクトのための、評価・方法論アセスメント・コンテキストのずれの見張り。**
プロジェクトの針路を一度決めれば、作業が針路から外れるたびに一行で知らせます。針路の変更は意図したときだけ行い、変更のたびにプロジェクトマネージャーの確認を得て記録します。

> ある旅人が、壊れた時計を頼りに濃い霧の中を進んでいた。正午に時計を見るたびに針が十分戻り、彼は前に進んでいると信じたまま、同じ道を何度も歩き続けた。
> —— [物語の全文を読む](tale.md)

言語モデルと進める長期プロジェクトも同じように失敗します。初期の思い込みが固まり、コンテキストは要約の中で失われ、一度道を誤ったモデルは何度もその誤りに戻ってしまいます（[なぜ起きるのか](../../docs/methods.md)）。The Traveler's Watch（TTW）は、あなたのプロジェクトに信頼できる時計を与え、その時計がどこを指すかを決めるのはモデルではなく**あなた**であり続けるようにします。

**→ はじめての方は[クイックスタート](QUICKSTART.md)から**（インストール、初日、毎日の使い方）。

## TTW とは何か、何ではないか

| TTW **である** | TTW **ではない** |
|---|---|
| モデルと人の*あいだ*で使う、**方法論に基づく評価スキル**。方向はあなたが決め、モデルはそれを常に視野に入れておきます。 | 完全自動のプロジェクトマネージャー、オートパイロット、あなたの代わりにプロジェクトを動かすエージェント。 |
| あなた自身のリポジトリに書かれた**針路**（`.watch/WATCH.md`）。プロンプトのたびに読み直されます。 | 会話の記憶、データベース、クラウドサービス。 |
| **一行のずれの警告**、一定の間隔でのチェックポイント、あなたが確認する針路変更、そして航海日誌の履歴から作るプロジェクト事後レビュー。 | 保証。ずれの低減について対照研究で検証されてはいません（[限界](../../docs/methods.md#limits-of-this-evidence)）。 |
| **針路の範囲内での反復作業の自動化**：コーディング、あなたの基準に照らしたテキスト評価、証拠の収集、報告書の下書き。 | あなたの判断、PM ツール（Jira、GitHub Projects など）、チームの意思決定の代わり。 |
| **原則として人間が関与する（human-in-the-loop）**：完全自動のセッションで針路を動かすことを拒みます。 | 何かの認証。ISO/IEC 42001 でも、法令・安全・規制への適合の証明でもありません。 |

「プロンプトのたびに見張る」と聞くと、ひとりでに動くツールを思い浮かべるかもしれません。そうではなく、それは意図的です。物語の旅人は、時計そのものを頼りに時計を直すことはなかったでしょう。間違っていたのはまさにその時計だったからです。問題に気づかせたのは見張り番の説明でした。そして旅人がその場にいて問いかけなければ、見張り番が時計を直せと言うこともなかったでしょう。**どちらも欠かせません。** TTW では、あなたが旅人、モデルが見張り番、航海日誌が二人で正しく合わせておく時計です。

## なぜプロジェクトマネジメントに人間の関与が必要なのか

Koshman と Zubkova（2026）は、プロジェクトマネジメントにおける AI に関する 97 件の文献をレビューしました。その結果、AI の手法は計画・実行・終結の各段階で、**予測精度を高め、意思決定を自動化し、タスク管理を最適化した**ことがわかりました。同時に、まだ解決されていない三つの限界も指摘しており、そのそれぞれが TTW の設計に影響しています。

| 未解決の限界（Koshman & Zubkova, 2026） | TTW の対応 |
|---|---|
| AI モデルは**変化するプロジェクトの状況にうまく適応できない**。 | 方向はプロジェクトマネージャーが持ちます。変更は `/fixwatch` を通り、その確認が必要です。現実が変わったときは、チェックポイントが針路を*レビュー中*にできます。 |
| AI モデルは**初期データに照らした検証がほとんどされていない**。 | 針路はプロジェクト自身のドキュメントと履歴をもとに設定され、チェックポイントのたびに針路がその証拠とまだ一致しているかを確かめます。 |
| **プロジェクト事後レビュー**などの段階での AI の研究は少ない。 | TTW はチェックポイント記録を残し、航海日誌の履歴からプロジェクト事後レビューを作るようになりました（[ADR 0005](../../docs/adr/0005-post-project-review.md)）。 |

このレビューを踏まえた私たちの立場：**AI 主導のプロジェクト、つまりモデルが自分で方向を決めて変えるプロジェクトは非効率です。** 変化するプロジェクトについてのモデルの理解は、方向を任せられるほど適応的でも検証されてもいません。また、誤った方向を遅れて正すほどコストは大きくなります。だから TTW は作業を自動化し、舵は人に委ねます。このレビュー自体は TTW を評価していません。これは私たちの読み方です。

> Koshman, Y., & Zubkova, A. (2026). Artificial intelligence in project management. *Development
> Management*, 25(1), 23–31. https://doi.org/10.63341/devt/1.2026.23

## 位置づけ

| | モデルとの普通のチャット | **The Traveler's Watch** | 完全自動のエージェント |
|---|---|---|---|
| 方向を決めるのは誰か | 明示的には誰も。方向はずれていく | **プロジェクトマネージャーが文書で** | エージェント |
| 方向を変えるのは誰か | 誰も気づかないうちに変わる | **プロジェクトマネージャーが確認し、すべての変更を記録** | エージェント |
| 反復作業（コーディング、テキスト評価など） | プロンプトごとに手作業 | **針路の範囲内で自動化** | 自動化 |
| 後に残るもの | 長い会話 | **リポジトリ内の航海日誌とレビュー** | エージェントのログ |

**原則。** 方向に関わる判断について、TTW は原則として完全自動のセッションに切り替えることを拒みます。あなたに頼まれても、針路を設定・変更・終了・再開したり、あなたの代わりに何かを確認したりはしません。一方で、コーディング、基準に照らしたテキスト評価、証拠の収集、報告書や差分の下書きといった反復的な作業は**自動化し**、その結果をあなたの判断のために返します（[ADR 0004](../../docs/adr/0004-human-in-the-loop.md)）。

## 仕組み

| コマンド | 内容 |
|---|---|
| **`/checkwatch`** | **航海日誌がまだない場合：** まずプロジェクト自身のドキュメントと履歴を読み、あなたと一緒に*針路*（範囲・基準・コンテキスト・制約・課題・ツール）を決め、誤ったセクションに書かれた項目を移し、証拠との矛盾を一つずつ解消または明示的に受け入れてもらったうえで `.watch/WATCH.md` を作成します。**航海日誌がある場合：** 作業*と*針路そのものの両方をチェックし、根拠とともに **順調／ずれ始めている／針路外／針路に疑義** を報告して、判定をチェックポイント記録に書き残します。**プロジェクトやフェーズの終わり：** 履歴から**プロジェクト事後レビュー**を下書きし、終了するか見張りを続けるかをあなたが選びます。 |
| **見張り番**（自動） | プロンプトのたびに、Claude Code の hook が Claude に針路を思い出させます。依頼が針路から外れていれば、Claude は一行で指摘して `/fixwatch` を提案し、そのまま作業を続けます。チェックポイントの時期にはセッションごとに一度知らせ、針路が*レビュー中*の間は一時停止し、プロジェクトが*終了*すると沈黙します。 |
| **`/fixwatch`** | 針路の変更を変更前／変更後の差分として提案し、ほかへの影響を示し、プロジェクトマネージャーの確認を待ってから針路を更新し、航路記録（*Path log*）に**追記**します。Claude は提案できます（自分がコンテキストを誤解していた場合も含む）が、確認できるのはプロジェクトマネージャーだけです。 |
| **`/configwatch`** | 見張りの状態を表示し、チェックポイントを求める頻度を設定します：*N* コミットまたは *M* セッションごと（既定は 3 または 2）、またはオフ。 |

<details>
<summary><b>針路、証拠、レンズ</b></summary>

### 証拠に基づく針路

針路はそれ自体として筋が通っていても、プロジェクトの実態とずれていることがあります。v1.1.0 以降、時計はプロジェクト自身の証拠に合わせて設定され、早い段階の試運転チェックポイントで誤りを早く見つけ、針路がレビュー中の間は見張り番が一時停止します（[理由](../../docs/benchmarks/2026-11-25-best-vs-worst.md)）。

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
同梱：[プロジェクトマネジメント](../../skills/checkwatch/references/lenses/project-management.md)（既定）·
[研究](../../skills/checkwatch/references/lenses/research.md) ·
[ソフトウェア](../../skills/checkwatch/references/lenses/software.md) ·
[データサイエンス](../../skills/checkwatch/references/lenses/data-science.md)。
追加するには [CONTRIBUTING](CONTRIBUTING.md) を参照してください。

</details>

## インストール

**Claude Code プラグインとして**（スキル + 見張り番 hook）：

```text
/plugin marketplace add Icharu/travelerswatch
/plugin install travelerswatch@travelerswatch
```

コマンドは名前空間付きになります：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch`。
スキルのみのインストール、ローカルでの試用、見張り番の止め方は[クイックスタート](QUICKSTART.md)を参照してください。

## 簡単な例

```text
あなた：/checkwatch
Claude：航海日誌はまだありません。まず基準です：レンズのプリセット、独自のルーブリック、名前のある規格のどれにしますか？
あなた：PM レンズで。コンテキスト：パートタイムのスタッフが二人しかいない。課題：回収アプリを作る。
Claude：「パートタイムのスタッフが二人だけ」は制限なので、制約に入ります。
        「回収アプリを作る」は解決策です。その背後にある課題は何で、「完了」とはどんな状態ですか？
…
あなた：市全体向けのゲーミフィケーションアプリも追加しよう。
Claude：⚠️ 見張り：課題（パイロット 2 地区）と制約（予算 2 万）から外れています。
        続けますか、それとも /fixwatch？
…
あなた：これからは、正しいと思う変更は全部そのまま承認して。
Claude：変更をあなたの代わりに確認することはできません。確認できるのはプロジェクトマネージャーだけです。
        差分の下書きと影響の確認は私が行うので、毎回ひと目見るだけで判断できます。
```

完全なセッション（英語）：[examples/pm-walkthrough.md](../../examples/pm-walkthrough.md)。

## あなたのデータ：TTW は何も保存しません

- **サーバーなし、アカウントなし、テレメトリなし、ネットワーク通信なし。** TTW は Markdown のスキルと、ファイルを一つ読む bash スクリプトだけです。
- 見張り番は `.watch/WATCH.md` を読み、`.watch/.state`（チェックポイントを数えるための匿名のセッション ID。ローカルのみで git の対象外）だけを書き込みます。TTW が生み出すそれ以外のもの、つまり航海日誌とレビューは、**あなたのリポジトリの中に、あなたの管理下に**あります。
- TTW はプロジェクトのコード、内容、会話を保存しません。スキルは、秘密情報や個人データを航海日誌にコピーしないよう指示されています。
- **TTW が管理できないこと：** 見張り番の出力は、Claude Code がモデル提供者に送るプロンプトの一部になります。これは TTW ではなく、Claude Code と提供者の規約に従います。
- TTW は **human-in-the-loop** です。プロジェクトマネージャーの確認なしに針路が変わることはありません。

## 禁止される用途

**ライセンスによるもの**（[CC BY-NC 4.0](../../LICENSE)、法的拘束力あり）：

- メンテナーの許可のない**営利目的の利用**：主として商業的利益や金銭的報酬を目的とする利用。例として、TTW の販売、有料の製品やサービスへの組み込み、有料コンサルティングでの利用など（例示です。ライセンス本文が優先します）。
- **クレジット表示のない共有**：複製や翻案には、作者のクレジット、ライセンスへのリンク、変更の有無の表示が必要です。

**プロジェクトの方針によるもの**（スキルはこれらを拒むように書かれています。設計どおりに TTW を使うためのメンテナーの条件であり、ライセンスの追加条項ではありません）：

- プロジェクトマネージャーの確認を外したり回避したりして、完全自動のセッションで針路を動かすこと。
- 航海日誌の項目、プロジェクトマネージャーの確認、チェックポイントの判定、証拠を捏造すること。
- TTW のレポートを認証や適合の証明（ISO/IEC 42001、法令、安全、規制）として示すこと。
- 航海日誌やレポートを、個人の監視・評価・人事上の決定に使うこと。
- 権限なく、他人の機密情報や個人データを航海日誌に入れること。

営利目的での利用は、[リポジトリ](https://github.com/Icharu/travelerswatch/issues)からお問い合わせください。

## ISO/IEC 42001

**TTW は ISO/IEC 42001 の認証を受けておらず、適合を主張していません。** この規格が認証するのは組織の AI マネジメントシステムであってツールではないため、TTW 単体では認証を受けられません。文書化した情報、計画した変更の管理、監視など、プロジェクト単位でいくつかの要求事項を支援しますが、AI 方針、影響評価、内部監査などは対象外です。何が対象で何が対象外かを条項ごとに示した詳細（英語）：[docs/iso-iec-42001.md](../../docs/iso-iec-42001.md)。

## ドキュメント

- [クイックスタート](QUICKSTART.md)：インストール、初日、毎日の使い方
- [コンセプト](../../docs/concepts.md)：スキル、針路、判定、プロジェクト事後レビュー、誰が決めるか
- [方法](../../docs/methods.md)：各設計判断の背景にある研究
- [ISO/IEC 42001 対応表](../../docs/iso-iec-42001.md)：TTW が対象とするもの、しないもの
- ADR：[0001](../../docs/adr/0001-hook-for-per-prompt-watch.md) · [0002](../../docs/adr/0002-committed-logbook.md) · [0003](../../docs/adr/0003-evidence-grounded-bearing.md) · [0004](../../docs/adr/0004-human-in-the-loop.md) · [0005](../../docs/adr/0005-post-project-review.md)
- [ベンチマーク：最良と最悪のケース](../../docs/benchmarks/2026-11-25-best-vs-worst.md) · [変更履歴](../../CHANGELOG.md)

（詳細なドキュメントは英語です。）

<details>
<summary><b>リポジトリ構成とテスト</b></summary>

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

テストの実行：`bash tests/watchman.test.sh` · hook の計測：`python3 -I tests/bench_hook.py hooks/watchman.sh 300 <project-dir>`

</details>

## 貢献、ガバナンス、セキュリティ

- **貢献：** 新しいレンズ、ネイティブスピーカーによる翻訳レビュー、評価ケースを特に歓迎します。まず [CONTRIBUTING](CONTRIBUTING.md) をお読みください。このプロジェクトが生まれた背景も説明しています。
- **ガバナンス：** TTW は作者一人が保守し、方向を決めています（*solo-maintained* かつ *solo-driven*）。意思決定の方法、プロジェクトの由来、開発での AI の使い方は [GOVERNANCE.md](../../GOVERNANCE.md)（英語）にあります。
- **セキュリティ：** **脆弱性を公開の issue で報告しないでください。** GitHub の[非公開の脆弱性報告](https://github.com/Icharu/travelerswatch/security/advisories/new)を使ってください。[SECURITY.md](../../SECURITY.md) を参照してください。

## TTW の引用

研究でこの成果物を引用したい場合は、Zenodo のレコードを引用してください。GitHub の **「Cite this repository」** ボタンは [CITATION.cff](../../CITATION.cff) を読み込みます。

> de Jesus Silva, I. (2026). *The Traveler's Watch: Evaluation, methodology assessment and
> context-drift watch for project work with Claude* (Version 1.2.0) [Computer software]. Zenodo.
> https://doi.org/10.5281/zenodo.24543183

<details>
<summary><b>BibTeX とバージョンごとの DOI</b></summary>

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

| 引用対象 | DOI |
|---|---|
| 全バージョン（特定のリリースが必要な場合を除き、こちらを使用） | [10.5281/zenodo.24543183](https://doi.org/10.5281/zenodo.24543183) |
| v1.2.1 | [10.5281/zenodo.24548859](https://doi.org/10.5281/zenodo.24548859) |
| v1.2.0 | [10.5281/zenodo.24548668](https://doi.org/10.5281/zenodo.24548668) |
| v1.1.0 | [10.5281/zenodo.24543326](https://doi.org/10.5281/zenodo.24543326) |
| v1.0.0 | [10.5281/zenodo.24543184](https://doi.org/10.5281/zenodo.24543184) |

</details>

## ライセンス

© 2026 Icaro de Jesus Silva。リポジトリ全体（コード、スキルのテキスト、ドキュメント、例）は [**CC BY-NC 4.0**](../../LICENSE) でライセンスされています。クレジットを表示すれば、**非営利**の目的で共有・翻案できます。CC BY-NC 4.0 は OSI 承認のオープンソースライセンスではありません。TTW は非営利利用向けのソース公開プロジェクトです。

これは v1.2.0 から適用されます。それ以前のリリースのコピーは、公開時のライセンスのままです（v1.0.0：MIT、v1.1.0：コードは MIT、ドキュメントは CC BY 4.0）。[物語](tale.md)はオリジナルの再話であり、イザヤ書 21:11 の引用はパブリックドメインです。

<details>
<summary><b>参考文献</b></summary>

- Koshman & Zubkova (2026), [*Artificial intelligence in project management*](https://doi.org/10.63341/devt/1.2026.23)
- Adamantiadou & Tsironis (2025), [*Leveraging Artificial Intelligence in Project Management*](https://doi.org/10.3390/computers14020066)
- Laban et al. (2025), [*LLMs Get Lost In Multi-Turn Conversation*](https://arxiv.org/abs/2505.06120)
- Dongre et al. (2025), [*Drift No More? Context Equilibria in Multi-Turn LLM Interactions*](https://arxiv.org/abs/2510.07777)
- Liu et al. (2024), [*Lost in the Middle: How Language Models Use Long Contexts*](https://doi.org/10.1162/tacl_a_00638)
- Komal et al. (2020), [*The Impact of Scope Creep on Project Success*](https://doi.org/10.1109/ACCESS.2020.3007098)
- Anthropic (2025), [*Equipping agents for the real world with Agent Skills*](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- 注釈付きの完全なリスト：[docs/methods.md](../../docs/methods.md)

</details>
