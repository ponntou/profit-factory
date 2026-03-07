---
title: "Claude Code の会話を全自動で Obsidian に記録する、または、車輪の再発明について"
source: "https://qiita.com/delphinus/items/9325c8dd750c85bac944"
author:
  - "[[delphinus]]"
published: 2026-02-28
created: 2026-03-08
description: "はじめに 僕は普段から Mac を複数台使って開発しています。フルリモートワークの仕事ですが、その日の気分や家庭の事情によってオフィスや自宅の Mac を使い分けています。 Claude Code には claude -r でセッションを再開できる機能がありますが、これは..."
tags:
  - "clippings"
---

## はじめに

僕は普段から Mac を複数台使って開発しています。フルリモートワークの仕事ですが、その日の気分や家庭の事情によってオフィスや自宅の Mac を使い分けています。

Claude Code には `claude -r` でセッションを再開できる機能がありますが、これは同じ端末でしか使えません [^1] 。そのため、ある端末で始めた作業を別の端末に引き継ぐのが億劫でした。途中のコードや修正方針を Markdown にまとめてレポジトリーにプッシュし、次の端末で `git pull` してから Claude Code に読ませる、そんな運用をしていたのです。これでちゃんと仕事はできるんですが、なかなかの手間です。

## きっかけ

そんな時「 [Claude Code チャットを Obsidian に保存](https://zenn.dev/togo_asai/articles/0b5bbd51f2a7cc) 」という記事を見かけました。

この記事で紹介されている方法は非常にシンプルです。コマンド定義ファイルを置き、セッション中に `/obsidian` と打つと会話内容が Obsidian の Vault に Markdown として保存される、というものでした。

Obsidian に置くなら端末間で簡単に同期できますから、僕の「端末を跨いで文脈を共有したい」という課題にぴったりです。ただ、毎回手動で `/obsidian` を叩くのはどうにも性に合いません。保存するかどうかを選択的に判断する意味は（少なくとも僕にとっては）無いと思ったのです。全部記録してくれればいい。後から検索すればいいんですから。

## 既存のソリューション

実はこの記事を書くにあたり初めて調べたのですが（後述します）、GitHub には Claude Code + Obsidian 連携のプロジェクトが既にいくつか存在していました。

### セッション記録系

| プロジェクト | 方式 | 特徴 |
| --- | --- | --- |
| [pulua/claude-code-obsidian](https://github.com/pulua/claude-code-obsidian) | シェルスクリプト | `/bye` 時に自動保存。日本語プロジェクト。 |
| [zulerne/claude-code-obsidian](https://github.com/zulerne/claude-code-obsidian) | Claude Code Skill | `/note` コマンドで手動保存。学習ノートとセッションログを自動分類。 |
| [aplaceforallmystuff/daily-patterns-pack](https://github.com/aplaceforallmystuff/daily-patterns-pack) | Claude Code Skill | `/log-to-daily` で要約をデイリーノートに追記。蓄積データからパターン分析する機能が面白い。 |

### モニタリング系

| プロジェクト | 方式 | 特徴 |
| --- | --- | --- |
| [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) | Web ダッシュボード | Hook イベントをリアルタイムで可視化（★1,200 超）。 |
| [williamkapke/MadameClaude](https://github.com/williamkapke/MadameClaude) | Web UI | 同様のリアルタイム監視。Node.js ベース。 |
| [welshofer/code-diary-hook](https://github.com/welshofer/code-diary-hook) | Apple Reminders | git commit と PR を Apple Reminders に日記として記録。 |

また [huytieu/COG-second-brain](https://github.com/huytieu/COG-second-brain) （★179）は Claude Code + Obsidian + Git で「自己進化するセカンドブレイン」を構築するテンプレートで、方向性が少し異なります。

セッション記録系はどれも「手動トリガー」が前提です。 `/obsidian` だったり `/note` だったり `/bye` だったり、何らかのアクションをユーザーが起こす必要があります。モニタリング系は Hook を使ったリアルタイム記録ができるのですが、記録先が Web UI であるのは動作の監視用途でしょうか。

僕が欲しかったのは、 **何も操作しなくても全てのやり取りがどこかに記録され、端末を跨いだ時にそのノートを読めば前回の文脈が分かる** 、というものでした。既存のソリューションの中にはこれを満たすものが見当たらなかったので、自分で作ることにしました。

……と書くと格好いいのですが、実際にはこの調査を行ったのは開発が終わった後です。この点については後ほど触れます。

## 作ったもの

[delphinus/homebrew-claude-code-hooks](https://github.com/delphinus/homebrew-claude-code-hooks) という Go 製の CLI ツールを作りました。Homebrew でインストールできます。

```bash
brew install delphinus/claude-code-hooks/claude-code-hooks
claude-code-hooks setup
```

デフォルトでは僕の設定を反映して、iCloud Drive 上の Obsidian Vault（ `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Notes/Claude Code` ）に記録します。変更したい場合は環境変数 `CLAUDE_OBSIDIAN_VAULT` を使います。Hook から呼ばれる際に参照されるため、`.zshrc` 等で設定すると良いでしょう。

```bash
# ~/.zshrc に追記
export CLAUDE_OBSIDIAN_VAULT=~/Documents/MyVault/Claude\ Code
```

Claude Code の [Hook 機能](https://docs.anthropic.com/en/docs/claude-code/hooks) を使い、以下のイベントを捕捉して指定されたフォルダに Markdown ファイルを生成します。

| イベント | 記録内容 |
| --- | --- |
| `UserPromptSubmit` | ユーザーの入力 |
| `Stop` | アシスタントの応答 |
| `PostToolUse` | ツール操作（Bash コマンド、ファイル編集など） |
| `SessionEnd` | AI による要約生成 + ノートのリネーム |

[![スクリーンショット 2026-02-28 14.17.57.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/8880/80d7cd93-cec7-4680-931d-524a49e0a257.jpeg)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F8880%2F80d7cd93-cec7-4680-931d-524a49e0a257.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=6bc50e63d1ff88f3c0ce900709ebf601)

記録されたノートはこのような構造になります。

ユーザーの発言は `## User` セクションに、アシスタントの応答は `## Assistant` セクションに記録されます。Bash コマンドやファイル編集は Obsidian の [Callout](https://help.obsidian.md/callouts) として折り畳み可能な形式で記録されます。

[![スクリーンショット 2026-02-28 14.18.37.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/8880/c405313e-4bc7-4bcb-8ceb-9f3e92b934b4.jpeg)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F8880%2Fc405313e-4bc7-4bcb-8ceb-9f3e92b934b4.jpeg?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e99caec03288f6b9712dfd4d74d17121)

ファイルの書式が準拠しているというだけで、特に Obsidian 固有の機能を使っている訳ではありません。Markdown をサポートするエディタであれば何でも読めますし、フォルダを何らかの方法で共有すれば、Obsidian を使っていない端末からもアクセスできます。

### ツール操作のフィルタリング

全てのツール操作を記録してしまうとノートがノイズだらけになります。Claude Code は作業中に大量の `ls` や `cat` や `grep` を実行しますが、こういった探索的なコマンドを逐一記録しても意味がありません。そこで、60 以上のコマンドをブロックリストに入れてスキップしています。 `git status` や `git diff` のような読み取り専用の git コマンドも同様です。

一方、パイプラインで繋がれたコマンドについては、一つでも記録対象のコマンドが含まれていれば全体を記録します。 `cat foo.txt | wc -l` は記録しませんが、 `go test ./... | tee result.log` は記録する、という具合です（この場合は `cat`, `wc`, `tee` が無視対象です）。

### セッション間リンク

`claude -r` でレジュームしたセッションや、作業ディレクトリが変わった場合は新しいノートが作成されます。その際、以前のノートへの Wiki リンクが自動的に挿入されます。別の端末で作業を再開する時は、Obsidian でそのプロジェクトの最新ノートを開けば、前回どこまで何をやっていたかが分かるようになっています。

### AI 要約

セッション終了時には Claude Code が会話内容の要約を生成し、ノートの冒頭に挿入します。ノートのタイトルが分かりにくいものになっている場合は、より内容を表すタイトルへの自動リネームも行います。

## 開発の経緯

### Bash で始めて Bash で死ぬ

最初は Hook から Bash スクリプトを叩けば済むと思っていました……が、これが思ったより大変でした。

問題は Claude Code における「セッション」という概念の扱いでした。

1. **基本ケース**: 1 セッション = 1 ノート。これは簡単。
2. **`claude -r` でレジューム**: セッション ID は同じだが、時間が空いているのでノートは分けたい。しかし以前のノートに飛べるリンクは欲しい。
3. **作業ディレクトリの変更**: 同じセッション内で `cd` すると、プロジェクトが変わるのでノートを分けたい。
4. **プランモード**: `EnterPlanMode` するとサブエージェントが起動し、セッション ID が変わる。しかしプランの内容は変更先セッションの Hook には流れてこない。プランの内容を取得するためにキャッシュファイルを介した受け渡しが必要になった。
5. **プランの引き継ぎ**: プランモード中にセッションが終了し、新しいセッションで作業を再開した場合、前回のプランを新しいノートにも載せたい。しかしセッション ID が異なるため単純な紐付けができない。2 分以内のキャッシュなら再掲する、という余りスマートでないロジックを入れた。

これらのエッジケースに一つずつ対処していった結果、Bash スクリプトは **800 行を超えました** 。 `jq` と `sed` と `awk` を駆使して [フロントマター](https://publish.obsidian.md/help-ja/%E9%AB%98%E5%BA%A6%E3%81%AA%E3%83%88%E3%83%94%E3%83%83%E3%82%AF/YAML%E3%83%95%E3%83%AD%E3%83%B3%E3%83%88%E3%83%9E%E3%82%BF%E3%83%BC) をパースし、連想配列でセッションキャッシュを管理し、ヒアドキュメントで Markdown を生成する……。AI だからできる芸当ですがソースはとても読めません。

### Go への移行

「これは Bash でやるべきことじゃない」と Claude Code に相談した所、Go への書き直しを提案されました。ファイル I/O が多く、JSON パースが必要で、文字列処理が複雑……確かに Go が適しています [^2] 。

移行自体は Claude Code に丸投げです。「この Bash スクリプトを Go に書き直して。機能は全て維持して」と伝えただけで、ディレクトリ構造の設計から `go.mod` の初期化、テストの作成まで全部やってくれました。この辺のリファクタリングや技術選択を全てお任せできるのは Claude Code の強みだと感じます。自分一人なら「Bash でもうちょっと頑張ればいけるかも……」と粘ってしまいそうです。

## 車輪の再発明について

さて、ここからが本題です（前置きが長い）。

今回個人的に画期的だと感じたのが、 **このスクリプトを作り始める時に一切既存のソリューションについて調べなかった** ということです。

普段の僕なら、何かツールを作ろうと思ったらまず「同じことをやっている人がいないか」を調べます。車輪の再発明は避けるべきですし、そもそも作る手間が掛かります。しかし今回はそうしませんでした。その理由は二つあります。

1. 作る内容が完全に個人的な問題に寄り添う形になることが分かっていた。
	- iCloud Drive で同期した Obsidian に、自分好みの Callout 形式で、自分の使っているターミナル（WezTerm）と連携する通知付きで記録する……こんなニッチな要件を満たす汎用ツールが存在するとは思えませんでした。
2. もっと簡単な方法があったとしたら Claude Code が提案してくれるだろう、という安心感があった。
	- 実際に Go への書き直しは Claude Code にお任せで問題ありませんでした。

結果として、作ったツールはカスタマイズがほとんどできない作りになっています。一応 Vault のパスは環境変数で変えられますが、それだけです。 `notify` サブコマンドは WezTerm 前提でハードコードされていますし、ノートの書式も僕好みの Callout 形式で固定です。ドキュメントもコミットメッセージも全て日本語で書いています。

### これは OSS としてはアンチパターンだらけである

普段 OSS を開発している身からすると、上記は全てアンチパターンです。

OSS として公開するプロダクトは一般的な課題を良く解決し、ニッチな課題にもプラグインやオプションで対応できるのが望ましいです。多くのコントリビューターが集まるほど品質や機能は改善されますし、そのためにはドキュメントは英語で書き、ヘルプや Web サイトもあった方がいいでしょう。

しかし今回は違います。たとえ要望が来ても、僕のワークフローを壊す形では実装しないでしょうし、使っている環境（macOS + WezTerm + iCloud Drive）以外のサポートは限定的になります。気に入らない部分は各人がクローンして AI で修正すればいいのです。

### Fork の時代

大規模なソフトウェアはともかく、今回のような小さなツールに今後、Issue や PR を送る人は少なくなるのではないでしょうか。

例えば、修正したい部分がある、しかし自分ではコード（あるいは英語）が読めない……このような場合、従来であれば Issue を立てて相談するか、諦めるかのどちらかでした。

Claude Code なら何も問題になりません。ドキュメントが何語で書かれていようが読めますし、あなたの知らない言語のコードでも理解して修正できます。問題点を自然言語で伝えれば、解決したバージョンを fork して作ってくれるのです。

その後本家にコントリビュートすることもできますが、取り込まれるかどうか分からないし、メンテナーとのコミュニケーションコストも甚大です。コーディング規約を調べ、テストを書き、CI を通し、レビューに対応し……それに時間を使うくらいなら、自分のアイデアを次々 fork して実装した方が効率的です。

OSS の文化は「みんなで一つのものを良くしていく」という精神で成り立ってきました。しかし AI がコードを書ける時代には、「自分用に fork する」コストが限りなくゼロに近づきます [^3] 。コントリビュートの動機が薄れ、本家のプロジェクトが放置される、そんな未来が来るかも知れません。

もっとも、この心配は杞憂かもしれません。fork が容易になるということは、優れたアイデアの伝播も速くなるということです。本家に PR を送る代わりに、fork 先で試した改善が本家に逆輸入されることもあるでしょう。OSS の形は変わるかもしれませんが、コードを共有するという文化自体は残るのではないかと思います。

## まとめ

Claude Code の会話を Obsidian に全自動で記録するツール [claude-code-hooks](https://github.com/delphinus/homebrew-claude-code-hooks) を作った話を書きました。色々ありましたが、結果として自分のワークフローにぴったりのツールができました。

一番気に入っている点は、このツールの存在を意識しなくていいことです。Claude Code を使っている限り、全てのやり取りが勝手に Obsidian に記録されています。端末を移動しても Obsidian を開けば、前回の作業内容がそこにある。それだけで十分です。

車輪の再発明は悪いことだと教わってきました。でも AI がコードを書いてくれる時代には、必ずしもそうとは限らないのかもしれません。自分のニーズに完全に合ったツールを作るために、あえて既存のソリューションを調べないという選択肢もあると思いました。

[0](https://qiita.com/delphinus/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fdelphinus%2Fitems%2F9325c8dd750c85bac944&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fdelphinus%2Fitems%2F9325c8dd750c85bac944&realm=qiita)

[^1]: 2026 年 2 月現在の話です。先日発表された [Claude Code Remote Control](https://x.com/noahzweben/status/2026371260805271615) を使えば、ローカルで動いているセッションにスマートフォンやブラウザから接続して操作を継続できます。しかしこれは、まだ発表されたばかりなので詳しく調べられていませんが、業務上のコードを扱う環境ではセキュリティポリシー上利用が難しいのではないでしょうか。

[^2]: 本当はここで Python や TypeScript（deno, bun）も提案されました。しかしなるべく依存するコンポーネントを減らしコンパイル済みのバイナリ一つで完結させたかったので Go にしました。

[^3]: もちろんお金は掛かります。