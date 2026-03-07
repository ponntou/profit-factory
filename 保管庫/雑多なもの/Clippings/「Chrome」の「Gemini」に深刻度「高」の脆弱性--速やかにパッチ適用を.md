---
title: "「Chrome」の「Gemini」に深刻度「高」の脆弱性--速やかにパッチ適用を"
source: "https://japan.zdnet.com/article/35244474/"
author:
  - "[[ZDNET Japan]]"
published: 2026-03-03
created: 2026-03-08
description: "「Google Chrome」の「Gemini」によるエージェント型人工知能（AI）機能に影響する新たな脆弱性が公表された。セキュリティ確保のため、速やかにパッチを適用すべきだ。"
tags:
  - "clippings"
---
- 
- [noteで書く](https://note.mu/intent/post?url=https%3A%2F%2Fjapan.zdnet.com%2Farticle%2F35244474%2F&ref=https%3A%2F%2Fjapan.zdnet.com%2Farticle%2F35244474%2F&hashtags=ZDNET)
- - 印刷する
- - メールで送る
	- テキスト
	- HTML
	- 電子書籍
	- PDF
- - ダウンロード
	- テキスト
	- 電子書籍
	- PDF
- - クリップした記事をMyページから読むことができます

　「Google Chrome」の「Gemini」によるエージェント型人工知能（AI）機能に影響する新たな脆弱性が公表された。セキュリティ確保のため、速やかにパッチを適用すべきだ。

　この脆弱性は、Palo Alto NetworksのUnit 42チームでシニア・プリンシパル・セキュリティ・リサーチャーを務めるGal Weizman氏によって開示された。影響を受けるのは、Google Chrome内のAI機能としてのGemini、すなわち、AIエージェント型のブラウザーアシスタント機能だ。

## 脆弱性の詳細

　共通脆弱性識別子「 [CVE-2026-0628](https://nvd.nist.gov/vuln/detail/CVE-2026-0628) 」が割り当てられた今回の脆弱性は、深刻度「高」と評価されており、「Google ChromeにおけるWebViewタグのポリシー適用の不備」と説明されている。この問題により、バージョン「143.0.7499.192」以前のGoogle Chromeは、「悪意ある拡張機能をインストールさせることに成功した攻撃者が、細工したChrome拡張機能を介して特権ページにスクリプトやHTMLを挿入できる」状態にある。

　Palo Alto Networksの研究チームは、「declarativeNetRequests」というAPIを通じて基本的な権限セットにアクセスする拡張機能によって、これを悪用した攻撃者が、新たなGeminiパネルのブラウザーコンポーネントにJavaScriptのコードを挿入することも可能な権限が付与されるおそれがあることを確認した。

　同チームによると、この脆弱性は、Google Chromeユーザーを標的とする [攻撃チェーンに組み込まれ](https://unit42.paloaltonetworks.com/gemini-live-in-chrome-hijacking) 、悪用されるおそれがあるという。

　例えば、攻撃者が標的をだまして、一見無害なブラウザー拡張機能をダウンロードしてインストールさせることに成功したら、その悪意ある拡張機能がポリシーの問題を悪用してGeminiを乗っ取るおそれがある。インストールしてしまうと、AIアシスタントのGeminiが許可なく動作して、サイバー犯罪者にウェブカメラやマイクへのアクセスを許可したり、スクリーンショットを撮影したり、ローカルのファイルやディレクトリにアクセスしたりすることが考えられる。フィッシング目的でGeminiパネルが乗っ取られる可能性もある。

　研究チームは次のように述べている。「Geminiアプリは正当な目的のためにアクションを実行するのが前提になっていることから、Geminiパネルを乗っ取られると、拡張機能には通常なら与えられないシステムリソースへの特権アクセスが許可されてしまう」

　最善の対策はシンプルだ。新しいバージョンのChromeが利用可能になったという通知を見たら（デスクトップ版では通常、アドレスバーの右側に表示される）すぐにアップデートを適用しよう。パフォーマンスの向上と新機能といったメリットが得られるだけでなく、含まれたセキュリティパッチにより、ブラウザーやデータが侵害されるリスクも軽減できる。

![提供：ZDNET](https://japan.zdnet.com/storage/2026/03/03/fd674d987075f711e48ddb25570a1cb1/new-report-finds-chatbots-can-steal-passwords-from-chrome_1280-1.jpg)  
提供：ZDNET

この記事は海外Ziff Davis発の [記事](https://www.zdnet.com/article/gemini-live-chrome-bug-hijacks-ai/) を4Xが日本向けに編集したものです。

ZDNET Japan 記事を毎朝メールでまとめ読み（登録無料）

[メールマガジン登録のお申し込み](https://japan.zdnet.com/newsletter/)

- 
- [noteで書く](https://note.mu/intent/post?url=https%3A%2F%2Fjapan.zdnet.com%2Farticle%2F35244474%2F&ref=https%3A%2F%2Fjapan.zdnet.com%2Farticle%2F35244474%2F&hashtags=ZDNET)

### ホワイトペーパー

#### 新着

- 開発
	[
	IT運用の複雑化にどう向き合うべきか、全社自動化へのアプローチ
	](https://japan.zdnet.com/paper/30001814/30008552/)
- 仮想化
	[
	既存環境の継続か、全面的なクラウド移行か。その二者択一を排した「ハイブリッド」の現実解
	](https://japan.zdnet.com/paper/30001815/30008554/)
- 経営
	[
	生成AIプロジェクトが進まない本当の理由とは？　AI時代に備えるデータ戦略の5つの重要ステップを解説
	](https://japan.zdnet.com/paper/30001462/30008547/)
- 開発
	[
	はじめての「テスト外注」、発注者の不安を減らす“失敗しない事前準備”の進め方
	](https://japan.zdnet.com/paper/30001773/30008545/)
- 運用管理
	[
	AI×ハイブリッドクラウド活用の「最適解」とは？ビジネス成果につながるインフラ実装と事例
	](https://japan.zdnet.com/paper/30001812/30008539/)

#### ランキング

1. 経営
	[
	ガートナーが示す「2026年の戦略的テクノロジ・トレンド」トップ10
	](https://japan.zdnet.com/paper/30001462/30008546/)
2. ビジネスアプリケーション
	[
	「生成 AI 活用」国内企業・自治体の事例集―― ユースケースから見る実践方法
	](https://japan.zdnet.com/paper/30001001/30008533/)
3. コミュニケーション
	[
	生成AIでナレッジ活用はどう変わる？組織の情報資産を最大化するための実践知を徹底解説
	](https://japan.zdnet.com/paper/30001799/30008428/)
4. 経営
	[
	調査レポート：生成AI・AIエージェントの企業導入実態と、浮き彫りになった課題構造
	](https://japan.zdnet.com/paper/20029481/30008521/)
5. 経営
	[
	生成AIプロジェクトが進まない本当の理由とは？　AI時代に備えるデータ戦略の5つの重要ステップを解説
	](https://japan.zdnet.com/paper/30001462/30008547/)

[ホワイトペーパーライブラリー](https://japan.zdnet.com/paper/)

ZDNET Japanは、CIOとITマネージャーを対象に、ビジネス課題の解決とITを活用した新たな価値創造を支援します。  
ITビジネス全般については、 [CNET Japan](https://japan.cnet.com/) をご覧ください。