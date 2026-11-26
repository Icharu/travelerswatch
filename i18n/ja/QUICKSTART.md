<!-- lang-bar -->
[English](../../QUICKSTART.md) · [Português (Brasil)](../pt-BR/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [繁體中文](../zh-Hant/QUICKSTART.md) · [简体中文](../zh-Hans/QUICKSTART.md) · **日本語** · [العربية](../ar/QUICKSTART.md)

> `QUICKSTART.md`（Unreleased、2026-11-25）からの翻訳です。機械支援による翻訳のため、正式な版は英語版です。

# クイックスタート

The Traveler's Watch（TTW）をインストールし、初日にプロジェクトの針路を決め、その後は毎日使います。[README](README.md) に戻る。

**TTW は日々の作業を人が導く（daily-led）ツールです。** 毎日の作業を導くのはあなたです。見張り番はプロンプトのたびに針路を視野に入れ、航海日誌が履歴を残します。そのため毎日が、モデルの記憶ではなく、プロジェクトの実際の状態から始まります。

## 1. インストール

いずれか一つを選びます。

| 方法 | コマンド | 得られるもの |
|---|---|---|
| **Claude Code プラグイン**（推奨） | `/plugin marketplace add Icharu/travelerswatch`<br>`/plugin install travelerswatch@travelerswatch` | スキル + 自動の見張り番。コマンド：`/travelerswatch:checkwatch`、`/travelerswatch:fixwatch`、`/travelerswatch:configwatch` |
| **スキルのみ**（Claude Code、または任意の [Agent Skills](https://agentskills.io/) エージェント） | `git clone https://github.com/Icharu/travelerswatch`<br>`cp -r travelerswatch/skills/checkwatch travelerswatch/skills/fixwatch travelerswatch/skills/configwatch ~/.claude/skills/` | スキルのみ、見張り番なし。コマンド：`/checkwatch`、`/fixwatch`、`/configwatch`。各セッションの開始時に `/checkwatch` を手動で実行します。 |
| **インストールせずに試す** | `claude --plugin-dir ./travelerswatch` | すべての機能（このセッションのみ） |

要件：見張り番には Claude Code が必要です。`bash` と `awk`（macOS と Linux には標準で入っています）。`git` は任意ですが、コミット数のカウントと完全なプロジェクト事後レビューに使います。

## 2. 初日：針路を決める

1. プロジェクトのルートフォルダで Claude Code を開きます。
2. **`/checkwatch`** を実行します。プロジェクトが何か、この針路がどの部分を導くかを一行で答えます。
3. Claude が README、`docs/`、最近の git 履歴を読み、**証拠カード**と各セクションの**下書き**を示します。あなたがそれを直し、Claude は抜け、誤ったセクションに書かれた項目、あなたの回答と証拠が矛盾する箇所について質問します。だいたい五往復ほどです。
4. 針路を確認します。Claude が `.watch/WATCH.md` を書き、`.watch/.state` を `.gitignore` に追加します。
5. **航海日誌をコミットします**：`git add .watch/WATCH.md .gitignore && git commit -m "watch: bearing set"`。

これ以降、あなたの確認なしに針路が変わることはありません。

## 3. 毎日

| タイミング | あなたがすること | TTW がすること |
|---|---|---|
| **一日の始まり** | Claude Code を開き、いつもどおり作業します。 | 最初のプロンプトで見張り番が `.watch/WATCH.md` を読み直すので、昨日確認した変更はすでに反映されています。 |
| **作業中** | コード、レビュー、下書きなど、必要なものを依頼します。 | 反復作業は針路の範囲内で行われます。依頼が針路から外れれば、Claude が**一行**で指摘して作業を続けます。 |
| **ずれの警告が出たとき** | 判断します：一時的な寄り道か、それとも道が本当に変わりつつあるのか。 | 寄り道ならそのまま続けます。本当の変更なら **`/fixwatch`** を実行し、差分と影響を見て、確認するか取り消します。 |
| **「チェックポイントの時期です」** | 手が空いたときに **`/checkwatch`** を実行します。 | *順調／ずれ始めている／針路外／針路に疑義* を根拠とともに報告し、チェックポイント記録に一行追加します。 |
| **一日の終わり** | `.watch/WATCH.md` が変わっていれば、作業と一緒にコミットします。 | ほかには何もしません。TTW はリポジトリの外にデータを保存しません。 |
| **フェーズやプロジェクトの終わり** | Claude に「このフェーズが終わるので、プロジェクト事後レビューをしよう」と伝えます。 | チェックポイント記録、Path log、git 履歴からレビューを下書きします。**レビューして終了**か**レビューのみ**かをあなたが選びます。 |

### TTW が何を、いつ知っているか

TTW は、あなたのファイルを監視するのではなく、航海日誌と git を通じてプロジェクトの日々の変化を把握します。正確には：

| タイミング | 読むもの | 読まない**もの** |
|---|---|---|
| **プロンプトごと**（見張り番） | `.watch/WATCH.md` の針路と Status、前回のチェックポイント以降のコミット数とセッション数。 | あなたのコード、差分、その他のファイル。 |
| **チェックポイント**（`/checkwatch`） | 会話、前回のチェックポイント以降の `git log`、変更されたファイル、*Evidence scanned* に挙げられたドキュメント。 | プロジェクトフォルダの外にあるもの。 |
| **プロジェクト事後レビュー** | 航海日誌全体（チェックポイント記録 + Path log）と `.watch/WATCH.md` の git 履歴。 | プロジェクトフォルダの外にあるもの。 |

## 4. コマンド早見表

| コマンド | 用途 |
|---|---|
| `/checkwatch` | 針路を決める（初回）・チェックポイントを行う・プロジェクト事後レビューを行う |
| `/fixwatch` | 意図して針路を変える・レビューを閉じる・終了したプロジェクトを再開する |
| `/configwatch` | 状態を見る・チェックポイントの頻度を設定する：試運転 `every 3 commits or 2 sessions`（既定）、安定 `every 10 commits or 5 sessions`、カスタム、または `off` |

## 5. TTW があなたの代わりにしないこと

頼まれても、TTW はあなたの代わりに変更を確認したり、矛盾を受け入れたり、プロジェクトを終了したりはしません。差分を下書きし、影響を確かめ、証拠を集めるので、毎回ひと目見るだけで判断できます。これは意図的な設計です。README の「TTW とは何か、何ではないか」（[README](README.md)）を参照してください。

## 6. 止める・一時停止する

- このシェルだけ：`export TRAVELERSWATCH_DISABLE=1`
- 恒久的に：`/plugin` → travelerswatch → disable（スキルは手動で引き続き使えます）。
- チェックポイントの通知を減らす：`/configwatch` → 安定または `off`。

## 次へ

[コンセプト](../../docs/concepts.md) · [完全な例](../../examples/pm-walkthrough.md) ·
[方法](../../docs/methods.md) · [貢献ガイド](CONTRIBUTING.md)
