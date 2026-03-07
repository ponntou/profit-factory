---
title: "Antigravity + Gemini 3 Pro のデザイン再現率をさらに引き上げるコツ"
source: "https://izanami.dev/post/525d3b7b-d2c5-40c8-bd99-1d5bcb29e548"
author:
  - "[[コムテ]]"
published: 2025-12-07
created: 2026-03-08
description: "Antigravity と Gemini 3 Pro でデザイン再現率を上げるには、全画面ではなくセクション単位で画像を切り出してアップロードし、既存コードを読み込ませた状態で生成させ、角丸や余白などの微調整を反復して指示するのが最速で 120 点のクオリティに到達する方法"
tags:
  - "clippings"
---
11

要約

Antigravity と Gemini 3 Pro でデザイン再現率を上げるには、全画面ではなくセクション単位で画像を切り出してアップロードし、既存コードを読み込ませた状態で生成させ、角丸や余白などの微調整を反復して指示するのが最速で 120 点のクオリティに到達する方法

[2件の意見があります](https://izanami.dev/post/525d3b7b-d2c5-40c8-bd99-1d5bcb29e548#insights)

まだ、フィードバックはありません

有料プラン契約して、ガンガン回した結果、Antigravity + Gemini 3 Pro のデザイン再現率をさらに引き上げるコツを掴んだぜぃ

ポイントはこれ

- セクション単位で狭く切り出して画像を見せる
- 既存のコードとクラス設計を読み込ませた状態で生成させる
- 細かい修正指示を反復で伝える
- 80 点を生成させた後に、細かいフィードバックを出す

だいたい、これやればデザインの精度がバク上がりする

でも、無料やと、すぐにレートリミットや！

なんで、個人アカウントに切り替えて、Google AI Pro（月額 2,900 円） を契約するといい

[Google AI のプラン（クラウド ストレージ付き） - Google One No Description https://one.google.com/intl/ja\_jp/about/google-ai-plans/](https://one.google.com/intl/ja_jp/about/google-ai-plans/)

![Google AI のプラン（クラウド ストレージ付き） - Google One](https://izanami.dev/_next/image?url=%2Fapi%2Fproxy-image%3Furl%3Dhttps%253A%252F%252Flh3.googleusercontent.com%252FqX38lptBs3zaLX8glwYOJHEGvZ5tDeuvkG5bRB75YBQ7BCUnjVnlFCiVcWKoM34PS0RFxtuKDI5iYxnnjVDi4x_JTpXxpielrN4G%253De365-pa-nu-w1200&w=256&q=75&dpl=dpl_FKTSZtrSdhmyGY8UFWDqH2hgsx2K)

Google AI のプラン（クラウド ストレージ付き） - Google One

Workspace アカウントは、Google AI Pro の契約ができないからね

Antigravity だけ使うなら Pro で十分。エージェントモデルのレート制限も引き上がるからね

### 結論から言うと、セクション単位で切り出すのが最強

再現したい UI を「全画面で渡す」のではなく、セクション単位で狭く切り出してアップロードすると精度が跳ね上がる

なんでかというと、余計な情報に引っ張られなくなるぶん、余白の取り方、フォントの太さ、階層構造、要素の重なりなどをピクセル感覚で読み取ってくれるから

「ここを見て!」と切り出すことで、モデルの視覚的な解像度が上がり、余白のピクセル感、フォントのウエイト、微細なシャドウや角丸の R（半径）まで正確に認識できるようになるんよ

Gemini 3 Pro のマルチモーダル読み取りはかなり優秀で、明示的に指定してなくても余白やヒエラルキーを尊重してくれる。旧世代のモデルより「見る」能力が格段に上がってるんよね

### Antigravity ってそもそも何なん?

Antigravity は Google が作ったエージェント主導の開発プラットフォーム。ベースには世界で最も使われている VS Code が採用されていて、そこに Google の最新 AI モデル Gemini 3 が組み込まれてる

[Google Antigravity を分かりやすく解説する - izanami Google が 2025 年 11 月 18 日に発表した次世代 AI IDE。Agent-first アーキテクチャでエディタ、ターミナル、ブラウザを横断制御し、Gemini 3、Claude Sonnet 4.5、GPT-OSS を無料で使える破壊的なプラットフォーム http://izanami.dev/post/a803b898-b8d8-4fc3-93c1-9d9c336658b5](http://izanami.dev/post/a803b898-b8d8-4fc3-93c1-9d9c336658b5)

![Google Antigravity を分かりやすく解説する - izanami](https://izanami.dev/_next/image?url=%2Fapi%2Fproxy-image%3Furl%3Dhttps%253A%252F%252Fizanami.dev%252Fpost%252Fa803b898-b8d8-4fc3-93c1-9d9c336658b5%252Fopengraph-image-1umokf%253F5589478d64c13f8a&w=256&q=75&dpl=dpl_FKTSZtrSdhmyGY8UFWDqH2hgsx2K)

Google Antigravity を分かりやすく解説する - izanami

特徴的なのは、AI エージェントがエディタ、ターミナル、ブラウザに直接アクセスできる点。エージェントが自律的に計画を立てて、複雑なエンドツーエンドのソフトウェアタスクを同時に実行しながら、自分自身でコードを検証してくれるんよ

VS Code での初期テストでは、Gemini 3 Pro は Gemini 2.5 Pro と比較してソフトウェアエンジニアリングの課題解決精度が 35% 向上したらしい

Antigravity は現在パブリックプレビュー中で、MacOS、Windows、Linux で無料で使える。5 時間ごとにリフレッシュされるレート制限はあるけど、Gemini 3 Pro だけでなく、Anthropic の Claude Opus 4.5 や OpenAI の GPT-OSS も使えるようになってる

### 既存のコードを読み込ませると精度が爆上がりする

既存のコードとクラス設計を読み込ませた状態で生成させると、サイト全体のトーン & マナーを壊さずに実装してくれる

Tailwind や CSS を整理しておくほど、それを吸収して一貫性のあるコードを出力してくれるんよね

具体的には「既存の Tailwind config を使って」とか「Button.tsx の props を再利用して」みたいな制約を追加すると、新しいコンポーネントを発明するんじゃなくて、既存のコードベースにきちんと馴染んでくれる

### 微調整を諦めないのが最強のアプローチ

角丸の数値、間隔、配置位置などの細かい修正指示を反復で伝えるほど、理想形に収束していく

一発で 100 点を目指すよりも、「80 点の構造」を出した後に、「角丸をもっと小さく」「左寄せに」といった具体的なフィードバックを出す方が、結果的に最速で 120 点のクオリティ（理想以上）に到達するんよ

Antigravity の特徴として、実装計画にコメントを追加できて、AI エージェントがそのフィードバックを認識して計画を更新する機能がある。この反復的なアプローチにより、開発初期段階での仕様調整がめっちゃ容易になってる

### Antigravity に聞いてみたら正解やった

上記の方法が正しいか Antigravity 自身に聞いてみたところ、完全に合ってるとのこと

これは経験則だけじゃなくて、ツールの設計思想ともマッチしてるってことやね

### 具体的なワークフロー

#### 画面の切り替えを覚えよう

Antigravity では主に「Agent Manager」と「Editor」の 2 つの画面を `⌘E` で切り替えて作業する

- Agent Manager: エージェントの実行状況、タスク、権限確認などの管理画面
- Editor: コードを書いたり、ファイルを編集したりする開発画面

#### Planning モードと Fast モードを使い分ける

Conversation Mode では 2 つのモードを切り替えられる

- Planning: 複雑なタスクや調査、共同作業向け。実行前に計画を立ててくれる
- Fast: シンプルなタスク向け。直接タスクを実行して素早く完了させる

デザイン再現のように精度が求められる作業は Planning モードで計画を立ててからやると、失敗が少なくなるよ

#### ブラウザ連携で視覚的フィードバックを得る

専用の Antigravity Browser Extension を Chrome にインストールすると、エージェントによる視覚的フィードバックや UI 修正が可能になる

Chrome 上でアプリが起動して、修正していく様子をリアルタイムで確認できるんよ。View をクリックすると AI が実施した実際の動作確認のキャプチャを見ることができて、このキャプチャは Artifact として保存されてる

### 日本語設定のやり方

Agent パネル右上の「...」から「Customizations → Rules → +Global」で「日本語で回答してください」と設定すると、日本語でやり取りできるようになる

プロンプトも日本語で OK。「シンプルな ToDo リストアプリを作って。デザインはモダンでおしゃれにして。完成したらブラウザで動作確認までして。」みたいな指示で、必要なファイル（HTML/CSS/JS）を作成してくれる

### 画像生成機能も使える

Antigravity には NanoBanana（Gemini 3 Pro Image）による画像生成機能も統合されてる

UI モックアップ生成はデザイン段階でのフィードバックやコード生成前の確認にめっちゃ有効。ウェブサイト向けの画像アセット生成では、ストック画像を探す代わりに直接適した素材を生成できるんよ

他の AI IDE だと、こういう画像生成は MCP への接続みたいなワークアラウンドが必要やけど、Antigravity は直接使えるのが強み

### Figma との連携も進んでる

Figma Make では Gemini 3.0 をモデルとして選択できるようになってる

フロントエンド開発者は Figma のワイヤーフレームをクリーンな HTML/CSS に変換できる。Rube がデザインをフェッチして、Antigravity が UI コードを生成するワークフローが可能やねん

Gemini 3 Pro は Figma Make において、デザインを精密に変換して、幅広いスタイル、レイアウト、インタラクションを生成する強力な基盤として機能してる

### 効果的な使い方のまとめ

- **セクション単位で切り出す**: 全画面じゃなくて、再現したい部分だけを狭く切り出してアップロード
- **既存コードを読み込ませる**: Tailwind config や既存コンポーネントの props を参照させて一貫性を保つ
- **制約を明示する**: 「既存の Tailwind config を使って」「Button.tsx の props を再利用して」みたいに具体的に指示
- **反復で微調整する**: 一発で完璧を目指すより、80 点の構造を出してから具体的なフィードバックで詰める
- **Planning モードを活用**: 精度が求められる作業は計画を立ててから実行
- **ブラウザ連携を使う**: リアルタイムで視覚的なフィードバックを得て修正

### 他の AI IDE との違い

Cursor や Windsurf みたいな AI IDE と比較して、Antigravity の特徴的な点は

- **エージェントが主役**: AI が補助ツールじゃなくて、開発プロセス全体を主導する
- **ブラウザ直接操作**: エージェントがブラウザを操作して動作確認まで自動化
- **画像生成統合**: NanoBanana による画像生成が直接使える
- **計画へのフィードバック**: 実装計画にコメントを追加して、AI が認識・更新してくれる

Google AI Studio、Vertex AI、Gemini CLI でも Gemini 3 を使えるし、Cursor、GitHub、JetBrains、Manus、Replit といったサードパーティプラットフォームでも利用可能になってる

### プロンプトのコツ

Google が公式に推奨してるデザイン関連のプロンプト設計のポイント

> Make a design that feels premium and state of the art. Avoid creating simple minimum viable products. Don't use placeholders. If you need an image, use your generate\_image tool to create a working demonstration.

つまり「プレミアム感のあるデザインを作って。シンプルな MVP は避けて。プレースホルダーは使わないで。画像が必要なら generate\_image ツールで実際の素材を作って」という感じ

システマチックなアプローチとしては

- **Plan and Understand**: ユーザー要件を完全に理解して、モダンなデザインからインスピレーションを得る
- **Build the Foundation**: CSS の作成・修正から始めて、コアデザインシステムを実装
- **Create Components**: デザインシステムを使って、フォーカスされた再利用可能なコンポーネントを構築
- **Assemble Pages**: 適切なルーティングとレスポンシブレイアウトでデザインを組み込む
- **Polish and Optimize**: 仕上げと最適化

この流れで進めると、構造化されたアプローチでデザイン再現の精度が上がるよ

### Rules で一貫性を保つ

Antigravity では Rules という機能でエージェントの行動指針を設定できる

コードスタイルを統一したい、常にメソッドをドキュメント化したい、みたいなガイドラインを追加しておくと、エージェントがそれを考慮してコードを生成・テストしてくれる

デザイン再現においても、「角丸は常に 8px」「余白は 4 の倍数」みたいなルールを設定しておくと、毎回指示しなくても一貫性のある出力が得られるようになるんよ

### まとめ

Antigravity + Gemini 3 Pro でデザイン再現率を上げるポイントは

- 全画面じゃなくてセクション単位で切り出す
- 既存のコードとクラス設計を読み込ませる
- 微調整を諦めずに反復で指示する
- 一発で 100 点より、80 点から詰める方が速い

AI IDE の使い方って、「どうやって効率よく指示を出すか」がめっちゃ重要。Antigravity は特にその辺の設計がうまくできてて、反復的なフィードバックを前提としたワークフローになってる

有料プランで制限なくガンガン回せる環境があると、この「反復」の部分が圧倒的に楽になるから、本気でデザイン再現に取り組むなら投資する価値はあると思うよ