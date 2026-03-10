---
title: "AIは速いのに、人間が遅い？ Claude Codeをさらに加速させる私の「推しツール」 - Findy Media"
source: "https://findy-code.io/media/articles/aisaji-tonkotsuboy_com"
author:
  - "[[Findy]]"
published: 2026-02-04
created: 2026-03-09
description: "今回の「AIのさじ加減」は、Ubieの鹿野 壮（@tonkotsuboy）さん。「Claude Codeにタスク丸投げおじさん」を自称する鹿野さんに、AIエージェントを活用した開発速度を最大化するための周辺ツールと工夫をご紹介いただきました。AIに速度で勝てない時代、人間は何を担うべきか。AIと人間の役割についても掘り下げます。"
tags:
  - "clippings"
---
本記事では、エンジニアがつくってきた“自分仕様のAIツール”やAI活用術をご紹介します。エージェントやBot、LLM連携ツールなど、実用的なものから、ちょっと遊び心のあるものまで。プロンプト設計やUIの工夫、うまくいかなかったことや思いがけない発見を通して、AIとの付き合い方をのぞいていきます。AIをどう使うかだけでなく、どんな距離感で付き合っているのか。誰かのAIとの向き合い方が、あなたとAIのちょうどいい“さじ加減”の手がかりに。

---

Ubieの [鹿野](https://x.com/tonkotsuboy_com) です。普段はUbieでプロダクトエンジニアとして働いていて、フロントエンド・バックエンド・モバイルアプリ開発等をしています。2025年5月頃から「Claude Codeにタスク丸投げおじさん」を自称しています。

Claude Codeを始めとするAIエージェントの登場で、コードが生産されるスピードと量は劇的に向上しました。しかし、実際の開発では「コードを書く」以外にも、Git操作、フォルダー移動、パッケージのインストール、PRへのコメント返信など、細かい作業が無数にあります。これらの周辺作業が効率化されていないと、せっかくAIエージェントが爆速でコードを生成してくれても、全体の開発速度は頭打ちになります。

本記事では、AIエージェントを活用した開発速度を最大化させるために、私が活用している周辺ツールを紹介します。

Claude Codeでは、MCP（Model Context Protocol）サーバーを使うことで、AIエージェントに様々な外部ツールへのアクセス能力を与えられます。しかし、従来はセッション開始時にすべてのMCPツール定義を読み込んでいたため、特に複数のMCPサーバーを設定しているユーザーは、大量のコンテキストトークンを消費していました。しかも、タスクによって必要なMCPは異なるので、せっかく設定したMCPの多くはそのタスクでは使われないというジレンマがありました。

最近登場した「Tool Search Tool」を使うと、MCPツールを必要なときだけ遅延読み込みできます。セッション開始時にコンテキストを消費することなく、MCPツールを呼び出し可能な状態に保ちます。また、AIが正しいMCPツールを使う選択の精度も上がります。

設定は簡単で、 ~/.claude/settings.json の env で ENABLE\_TOOL\_SEARCH を true に設定するだけです。

```json
{
  "env": {
    "ENABLE_TOOL_SEARCH": "true"
  }
}
```

キャプチャーは、通常であればMCPだけでコンテキストの50％を占める環境ですが、Tool Search ToolをONにすると起動時のMCPのコンテキスト消費は0%となり、Free space（残りのコンテキスト）の量が増えています。MCPの箇所には「loaded on demand」、つまり呼び出し時に読み込まれることを示すメッセージが表示されます。

![loaded on demand.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTUyLCJwdXIiOiJibG9iX2lkIn19--109fd80d9d7efe26e5ef187c64901f4010e04735%2Floaded%2520on%2520demand.png&w=3840&q=75)

登場後しばらく使っていますが、確かにMCPの選択精度が向上したようで、体感ではほとんど間違わなくなったように感じます。

## セッション間のコンテキストを手軽に維持する（Claude-Mem）

AIエージェントでの作業は複数のセッションにまたがることが常です。しかし、デフォルトではセッションを終了すると、そのセッションで得たコンテキストは基本的には失われてしまいます。セッションが変わるたびに、何度も同じ指示をAIに出すということはよくあります。

Claude Codeの「Claude-Mem」プラグインを使うと、セッション間でコンテキストを自動的に保存・復元してくれます。コーディングセッション中のすべての活動を自動的に記録し、AIで圧縮してから、次回のセッションに関連コンテキストを注入してくれます。

[

GitHub - thedotmack/claude-mem: A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. · GitHub A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. - thedotmack/claude-mem

GitHub

![GitHubのサムネイル画像](https://repository-images.githubusercontent.com/1048065319/c84340b5-674d-4f93-ad06-452718614abb)](https://github.com/thedotmack/claude-mem)

プロジェクトに関する知識を連続的に持つようになり、「以前どうやって解決したっけ？」「今日やった作業ってなんだったっけ？」といった、セッションに跨る質問や解決が可能になります。次の例では、セッション開始直後に以前のセッションに対する質問を行い、解答を得ています。

![以前のセッションに対する質問.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTUwLCJwdXIiOiJibG9iX2lkIn19--62143ad8e7f543acd1568b2b07fb61696fe2c08f%2F%25E4%25BB%25A5%25E5%2589%258D%25E3%2581%25AE%25E3%2582%25BB%25E3%2583%2583%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%25B3%25E3%2581%25AB%25E5%25AF%25BE%25E3%2581%2599%25E3%2582%258B%25E8%25B3%25AA%25E5%2595%258F.png&w=3840&q=75)

また、過去のセッションはhttp://localhost:37777でリアルタイムに表示されるので、セッションの内容を確認できます。

![セッションの内容確認.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTUxLCJwdXIiOiJibG9iX2lkIn19--200ed8ba190384e61688c14c3bf6ee60e1e51386%2F%25E3%2582%25BB%25E3%2583%2583%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%25B3%25E3%2581%25AE%25E5%2586%2585%25E5%25AE%25B9%25E7%25A2%25BA%25E8%25AA%258D.png&w=3840&q=75)

## 過去のセッションに素早くジャンプする（ccresume）

Claude Codeでは、claude --resume（または-r）コマンドで過去のセッションを選んで再開できます。初期に比べて随分見やすくなりましたが、私は「ccresume」というサードパーティツールを気に入っています。

[

GitHub - sasazame/ccresume: A CUI tool for browsing and resuming Claude Code conversations · GitHub A CUI tool for browsing and resuming Claude Code conversations - sasazame/ccresume

GitHub

![GitHubのサムネイル画像](https://opengraph.githubassets.com/8a3c27be30b618b8e19b2c9f6efa29070bba52c9b11161afcf0a996fcb677574/sasazame/ccresume)](https://github.com/sasazame/ccresume)

ccresumeは、Claude Codeのセッション履歴をインタラクティブに閲覧・管理できるCUIツールです。矢印キーやTabキーでのインタラクティブな操作、オートコンプリート機能、Claude CLIオプションの公式ヘルプテキストが表示されるなど、標準のresumeコマンドよりも使いやすくなっています。

実際にccresumeを使って、過去のセッションを確認している様子です。ここからセッションを選択して再開できます。

![ccresume.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTU1LCJwdXIiOiJibG9iX2lkIn19--8f276bd2ac192e72e318f75ead930db1324a90aa%2Fccresume.png&w=3840&q=75)

## AIエージェントにPRコメントを返信させる

リポジトリには、CodeRabbitやCopilot、その他さまざまなAIレビュアが導入されていることが多いです。これらは非常に有用なのですが、PRを作成すると複数のAIから大量のコメントが飛んできます。すべてに返信するのは面倒ですが、無視してマージすると、後からPRを見た人が「このコメントは検討されたのかな？」と困ります。

そこで私は、次のコマンドをClaude Codeに覚えてもらって、自動返信してもらっています。このコマンドは、GitHub CLIのghコマンドを使って、PRの特定のコメントに対してスレッド形式で返信するものです。

```sh
gh api repos/{owner}/{repo}/pulls/{pr_number}/comments -X POST \
  -f body="返信内容" \
  -F in_reply_to={comment_id}
```

実際にClaude Codeでレビューに自動返信してもらっている様子です。「今回のPRの各コメントに返信しておいて」と指示しました。

![レビューへの自動返信.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTU2LCJwdXIiOiJibG9iX2lkIn19--d8d72d7c8275e9469b54865c731c019f7e20b705%2F%25E3%2583%25AC%25E3%2583%2592%25E3%2582%2599%25E3%2583%25A5%25E3%2583%25BC%25E3%2581%25B8%25E3%2581%25AE%25E8%2587%25AA%25E5%258B%2595%25E8%25BF%2594%25E4%25BF%25A1.png&w=3840&q=75)

逆に、こういった形で返信を指定しないと、コメントへの返信ではなく、PRの新規コメントとして投稿されたりします。私はそれが嫌で、ghコマンドをつかう形を指定しています。

## npmやpnpmのパッケージマネージャーを自動判定する（ni）

AIエージェントを活用するようになり、手数が増えたことで、多くのリポジトリを扱うことになりました。複数のプロジェクトを扱っていると、あるプロジェクトはnpm、別のプロジェクトはyarn、さらに別のプロジェクトはpnpmと、パッケージマネージャーが異なるケースもよくあります。各コマンドの使い方は微妙に異なるので、全部覚えたり、その都度調べたりするのは開発速度の低下につながります。

「ni」というツールを使うと、プロジェクトのロックファイルを検出して、自動的に適切なパッケージマネージャーを選択してくれます。

たとえば「ni vite」というコマンドを実行すると、プロジェクトに応じて、npm、yarn、pnpmのいずれかのコマンドが実行されます。

- npmが使われている場合: npm install vite
- yarnが使われている場合: yarn add vite
- pnpmが使われている場合: pnpm add vite
- bunが使われている場合: bun add vite
- denoが使われている場合: deno add vite

たとえば、次のコマンドなどはよく使います。

- ni - 依存関係をインストール
- ni パッケージ名 -D - 開発依存としてインストール
- nr コマンド名 - スクリプトを実行

実際にnr devを使って、npm run devを実行している様子です。

![npm run dev.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTU3LCJwdXIiOiJibG9iX2lkIn19--f85854619ee68aee9a161fbdcf3b4eadc6240bc7%2Fnpm%2520run%2520dev.png&w=3840&q=75)

## リポジトリ間をコマンド一つで移動する（ghq, peco）

私は複数のプロジェクトを並行して作業することが多く、リポジトリ間の移動が頻繁に発生します。しかし、いちいちcd ~/git/github.com/owner/repoのようにcdコマンドを打つのは面倒です。Claude Codeに「このリポジトリに移動して」と指示できますが、「ghq」と「peco」を使うと、コマンド1つでリポジトリ間を移動できます。

### ghqでリポジトリ管理

ghqは、Gitリポジトリを決まったディレクトリ構造で管理するツールです。すべてのリポジトリが~/git/github.com/{owner}/{repo}のように整理されます。

[

GitHub - x-motemen/ghq: Remote repository management made easy · GitHub Remote repository management made easy. Contribute to x-motemen/ghq development by creating an account on GitHub.

GitHub

![GitHubのサムネイル画像](https://opengraph.githubassets.com/4ebd733e6c4bae460ef0fcfb921acbd7fb3414a72c5e14555d2ad1e72ac56bda/x-motemen/ghq)](https://github.com/x-motemen/ghq)

ghqコマンドでGitリポジトリをクローンするには、まず、~/.gitconfigの\[ghq\]の項目に、リポジトリをクローンするディレクトリを設定します。私は ~/git/フォルダに指定しています。

```json
[ghq]
    root = ~/git
```

ghq get コマンドでGitリポジトリをクローンします。

ghq get （リポジトリパス）

すると、~/git/github.com/{owner}/{repo}フォルダーにリポジトリがクローンされます。

![ghq get.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTU4LCJwdXIiOiJibG9iX2lkIn19--1c63a9db4649c23924af5b2a3b7383000eed8b45%2Fghq%2520get.png&w=3840&q=75)

### pecoで絞り込み、g一発で移動

pecoは、標準入力から受け取ったリストをインタラクティブに絞り込むツールです。ghqと組み合わせることで、リポジトリ間を一発で移動できるようになります。

[

GitHub - peco/peco: Simplistic interactive filtering tool · GitHub Simplistic interactive filtering tool. Contribute to peco/peco development by creating an account on GitHub.

GitHub

![GitHubのサムネイル画像](https://opengraph.githubassets.com/64a87fb8e756f810e80d08715546f2c7655ae1a81dd806049620168e0a9959b2/peco/peco)](https://github.com/peco/peco)

私の場合は、gコマンドでGitリポジトリ一覧を表示し、矢印キーかインクリメンタルサーチでリポジトリを選択して移動しています。

gコマンドの設定例は次のとおり。まず、.zshrcに以下のようなエイリアスを設定します。gと入力するだけで、クローンしたすべてのリポジトリ一覧が表示され、リポジトリ名の部分一致か上下キーで選択して移動できます。

```sh
function g (){
  local selected_dir=$(ghq list -p | peco --query "$LBUFFER")
  if [ -n "$selected_dir" ]; then
    cd ${selected_dir}
  fi
}
```

実際の動作は次のとおりです。

① gを押す

![gを押す.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTYwLCJwdXIiOiJibG9iX2lkIn19--7daaf396d2b4325811bb72a35cbb070866c6f346%2Fg%25E3%2582%2592%25E6%258A%25BC%25E3%2581%2599.png&w=3840&q=75)

② Enterキーを押すと、ghqでクローンしたリポジトリ一覧が表示される

![リポジトリ一覧.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTYxLCJwdXIiOiJibG9iX2lkIn19--8c4e0be496e10dbe99f7f5d6fff8de2f032fdc82%2F%25E3%2583%25AA%25E3%2583%259B%25E3%2582%259A%25E3%2582%25B7%25E3%2582%2599%25E3%2583%2588%25E3%2583%25AA%25E4%25B8%2580%25E8%25A6%25A7.png&w=3840&q=75)

③ 矢印キーか、インクリメンタルサーチでリポジトリを選択して移動する

![リポジトリを選択して移動.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTYyLCJwdXIiOiJibG9iX2lkIn19--da3034b1fa5a6cfd8c154f5b6b5622ae4b20d1d3%2F%25E3%2583%25AA%25E3%2583%259B%25E3%2582%259A%25E3%2582%25B7%25E3%2582%2599%25E3%2583%2588%25E3%2583%25AA%25E3%2582%2592%25E9%2581%25B8%25E6%258A%259E%25E3%2581%2597%25E3%2581%25A6%25E7%25A7%25BB%25E5%258B%2595.png&w=3840&q=75)

リポジトリ間の移動にかかる時間が短縮されることで、AIエージェントとのやり取りのテンポが格段に良くなります。

## Raycastでアプリケーション操作を高速化

AIエージェントとの開発では、ターミナル、エディター、ブラウザ、その他のツールを頻繁に切り替えます。マウスでアプリを探してクリックする時間は、積み重なると大きなロスになります。

「Raycast」は、生産性ランチャーで、キーボードショートカット1つでアプリケーションの起動、コマンドの実行、ファイル検索などが可能になります。Windows版もベータ版として提供されています。

[

Raycast - Your shortcut to everything A collection of powerful productivity tools all within an extendable launcher.

www.raycast.com

![nullのサムネイル画像](https://www.raycast.com/opengraph-image-pwu6ef.png?7385e23163a01717)](https://www.raycast.com/)

Raycastでは、任意のアプリケーションにショートカットキーを割り当てられます。たとえば、私はOption + Command + Tでターミナルを起動するように設定しています。毎日何十回も開くターミナルなので、いちいちspotlightを開いたり、アプリケーションをマウスダブルクリックするのは時間のムダです。

![ショートカットキーを割り当て.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTYzLCJwdXIiOiJibG9iX2lkIn19--5bafdb65e6b4d8e57ba4860e64509c856522757a%2F%25E3%2582%25B7%25E3%2583%25A7%25E3%2583%25BC%25E3%2583%2588%25E3%2582%25AB%25E3%2583%2583%25E3%2583%2588%25E3%2582%25AD%25E3%2583%25BC%25E3%2582%2592%25E5%2589%25B2%25E3%2582%258A%25E5%25BD%2593%25E3%2581%25A6.png&w=3840&q=75)

また、Raycastの「Run Command」機能を使うと、任意のシェルスクリプトをショートカットキー1つで実行できます。私は、「同じリポジトリを複数フォルダーに自動採番しながらクローンする」という操作を頻繁に行いますが、それをスクリプト化し、Run Commandで実行するようにしています。複数のAIエージェントに同じタスクを並行実行させるときに便利です。

![Run Command.png](https://findy-code.io/_next/image?url=https%3A%2F%2Fstorage.findy-code.io%2Fstorage%2Fblobs%2Fproxy%2FeyJfcmFpbHMiOnsiZGF0YSI6MTAzMTY0LCJwdXIiOiJibG9iX2lkIn19--47ab4e7b6d65a10c8e465239468df0923971fae4%2FRun%2520Command.png&w=3840&q=75)

他にも、クリップボードヒストリー、スニペットなど日々の操作を便利にする機能が豊富に揃っています。私は長年課金していたAlfredからRaycastに移行しましたが、快適で1操作でも減らせないか日々楽しく改善しています。

## 最後に

AIエージェントの開発速度は、もはや人間が追いつけるものではありません。Claude Codeをはじめとするツールは、私よりも速く、大量にコードを生産できます。「人間が勝てる時代」は、おそらくもう来ないでしょう。私はAIエージェントを「道具」だとは思っていません。自分より圧倒的に速いチームメイトだと捉えています。チームメイトである以上、それぞれに役割がある。では、速度で勝てない人間は何を担うべきか。

1つ目は、AIの速度を落とさせないこと。本記事で紹介したツール群はまさにそのためのものです。セッション間のコンテキスト維持、MCPの遅延読み込み、リポジトリ間の高速移動などははすべて「AIエージェントが本来持っている速度を、人間のボトルネックで殺さない」ための工夫です。

2つ目は、成果物の質をコントロールすること。AIは速い。しかし、何を作るべきか、どの方向に進むべきかの判断は人間がします。レビューし、軌道修正し、品質を担保する。速度はAIに任せ、判断と責任は人間が持つ。それが今の私のスタンスです。

「業務を一操作でも減らせないか？」そんな視点でAIエージェントとの開発フローを日々改善しています。

[新規登録](https://findy-code.io/users/sign_up?r=%2Fmedia%2Farticles%2Faisaji-tonkotsuboy_com) [ログイン](https://findy-code.io/users/sign_in?r=%2Fmedia%2Farticles%2Faisaji-tonkotsuboy_com)

[利用規約](https://findy-code.io/terms) 、 [プライバシーポリシー](https://findy.co.jp/privacy) に同意の上 、 ご利用ください。