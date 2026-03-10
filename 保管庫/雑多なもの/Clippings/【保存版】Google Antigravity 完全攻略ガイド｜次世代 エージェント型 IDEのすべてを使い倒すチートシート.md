---
title: "【保存版】Google Antigravity 完全攻略ガイド｜次世代 \"エージェント型\" IDEのすべてを使い倒すチートシート"
source: "https://qiita.com/akira_papa_AI/items/0acf2679e4ce9f7fb153"
author:
  - "[[akira_papa_AI]]"
published: 2025-11-20
created: 2026-03-09
description: "はじめに Google Antigravityがリリースされました。 「Cursor, Windsurf...またAI搭載エディタか」って思いませんでした？ 僕も最初そう思ってたんです。 でもね、ドキュメント読み込んでいくうちに、ちょっと考えが変わりました。 Googl..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiita Careers powered by IndeedPR

求人サイト「Qiita Careers powered by Indeed」では、エンジニアのあなたにマッチした求人が見つかります。

[求人を探す](https://careers.qiita.com/)

[![sitecard-default.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/868ac99c-5cd1-4333-8d4a-e0d3d6e7bde9.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F868ac99c-5cd1-4333-8d4a-e0d3d6e7bde9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=57150fb5c7e3c97005730513deb5ee27)

## はじめに

Google Antigravityがリリースされました。

「Cursor, Windsurf...またAI搭載エディタか」って思いませんでした？  
僕も最初そう思ってたんです。

でもね、ドキュメント読み込んでいくうちに、ちょっと考えが変わりました。

Google Antigravityって、単なる「AI補完付きエディタ」じゃないんです。  
**「エージェント（自律思考AI）」が主役の開発環境** なんですよね。

ブラウザ操作から複数リポジトリの同時開発まで、未来の機能がてんこ盛り。

この記事を読めば、Antigravityの全体像がつかめるようになってます。  
少し長くなりますが、コーヒー片手にお付き合いください。

---

## 目次

1. Antigravityとは何か？
2. インストールと準備（ここ超重要）
3. 基本画面とナビゲーション
4. 最強の相棒「Agent」を理解する
5. エディタ機能：TabとCommand
6. 成果物「Artifacts」とタスク管理
7. 革命的機能：Browser Agent
8. Agent Manager：全知全能の管理画面
9. 拡張機能：MCPとKnowledge
10. 設定・制限・FAQ

---

## 1\. Antigravityとは何か？

**Google Antigravity** は、従来のIDE（統合開発環境）を「エージェントファースト」の時代へと進化させるプラットフォームです。

VS Codeベースの親しみやすいUIを持ちながら、その核となるのは **「Agent（エージェント）」** 。

エージェントは単にコードを書くだけじゃなくて、ターミナル操作、ブラウザでの検証、そしてプランニングまでを自律的に行います。

これ、すごくないですか？

今までのAIエディタって「ここ直して」って頼む感じでしたけど、Antigravityは「この機能実装しておいて」って頼んだら、計画立てて、コード書いて、ブラウザで動作確認までしてくれるイメージ。

まさに「グラビティ（重力）」から解き放たれるような身軽さ。  
そういう思想がネーミングに込められてるのかなと。

### 主なコア機能

- **Editor:** AI搭載のVS Codeベースエディタ
- **Agent Manager:** 複数のワークスペースやエージェントを一元管理する司令塔
- **Browser Agent:** エージェントが自らブラウザを操作してタスクを実行
- **MCP (Model Context Protocol):** 外部ツールやDBと接続する標準プロトコル

---

## 2\. インストールと準備（ここ超重要）

まずはここから。  
使い始めるための要件がいくつかあるんですけど、ここでつまずく人けっこういそうなので、しっかり確認しておきましょう。

### ダウンロード

・Google Antigravity Download  
　URL: [https://antigravity.google/download](https://antigravity.google/download)

から入手可能です。

### システム要件

自分のPCが対応しているかチェックしましょう。

**macOS:**

- Appleのセキュリティアップデートがサポートされているバージョン（通常は現行+過去2バージョン）
- 最低要件: macOS 12 (Monterey)
- **注意：X86 (Intel Mac) はサポートされていません。Apple Silicon (M1/M2/M3/M4等) 必須です**

ここ、めっちゃ大事なポイント。  
Macユーザーの方、Intel Macだと動かないみたいです。M1以降のマシンのみ対応。

**Windows:**

- Windows 10 (64 bit)

**Linux:**

- glibc >= 2.28, glibcxx >= 3.4.25 (Ubuntu 20, Debian 10, Fedora 36, RHEL 8など)

Linuxユーザーの方もglibcのバージョンには注意してくださいね。

### 認証と利用可能地域

**アカウント:**  
現在は **個人のGoogleアカウント（@gmail.com）のみ** 対応。  
Workspaceアカウント（企業用など）は、たとえ個人利用でもNGです。

会社のメールアドレスでログインしようとして「あれ？」ってなる人、続出の予感。  
今はパブリックプレビューなので、個人のGmailを使いましょう。

**地域:**  
日本（Japan）を含む多くの国で利用可能ですが、リストにない国では使えません。  
日本は対象国に入ってるので安心。

---

## 3\. 基本画面とナビゲーション

Antigravityには大きく分けて2つの「顔」があります。

1. **Editor (エディタ):** コードを書くいつもの画面
2. **Agent Manager (エージェントマネージャー):** エージェントを指揮する管理画面

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/61bda177-e38b-42b9-ac20-1e994411731f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F61bda177-e38b-42b9-ac20-1e994411731f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d1c7319e234a0893714125738fb99850)

### 画面の切り替え

このショートカットだけは覚えて帰ってください。

**`Cmd + E` (Mac) / `Ctrl + E` (Windows)**

エディタとマネージャーを一瞬で切り替えます。

`Cmd + E` でサクサク切り替えるのがAntigravity流の基本動作になりそう。  
エディタの左上にあるボタンからも切り替えられますよ。

---

## 4\. 最強の相棒「Agent」を理解する

Antigravityの心臓部、それが「Agent」です。

### 使用モデル (Models)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/d37704df-834c-4bb2-b955-2de0f1756bae.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fd37704df-834c-4bb2-b955-2de0f1756bae.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=061c749815703b06982845804a6d1486)

なんと、Googleのモデルだけでなく、他社のモデルも選択可能です（ドキュメント記載ベース）。  
会話のプロンプトボックス下のドロップダウンで選択します。

- **Gemini 3 Pro** (High / Low) - Googleの最新フラッグシップ
- **Claude Sonnet 4.5** (通常版 / Thinking版)
- **GPT-OSS**

ユーザーのターンごとにモデルを切り替えられるので、「推論はClaudeで、実装はGeminiで」みたいな使い分けもできそう。

### エージェントモード (Agent Modes)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/b71d3078-c429-4afe-94ab-8d82b6aff19e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fb71d3078-c429-4afe-94ab-8d82b6aff19e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=50c0daabf8be72a34752e2fe5065fac4)

タスクの重さに応じてモードを選べます。

**1\. Planning Mode (計画モード)**

- **用途:** 複雑なタスク、深いリサーチ、共同作業
- **挙動:** いきなりコードを書かず、まずは「Task Groups」や「Artifacts（計画書）」を作成して、じっくり考えます

**2\. Fast Mode (高速モード)**

- **用途:** 変数名の変更、簡単なバッシュコマンド実行など
- **挙動:** 計画を飛ばして、即座にタスクを実行します

基本は「Planning」で良さそうですね。  
エージェントが暴走しないように、ちゃんと計画を立ててくれるのは安心感があります。  
「Fast」は従来のチャットAIっぽい使い心地かなと。

### ファイルアクセス権限

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/b842abb5-8d85-4725-b2f3-0c9fa6dd7064.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fb842abb5-8d85-4725-b2f3-0c9fa6dd7064.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=800eb68c92e851046f6611f74d105cc0)

デフォルトでは、エージェントは「現在のワークスペース」と「 `~/.antigravity/` （設定ファイル等）」しか触れません。

**設定:**`Agent > Non-Workspace File Access` で外部ファイルへのアクセスを許可できますが、 **セキュリティ的に要注意** です。

---

## 5\. エディタ機能：TabとCommand

エージェントだけでなく、コードを書く際のアシスト機能も強力です。

### Tab (Supercomplete)

単なるオートコンプリートを超えた「スーパーコンプリート」。

- **Supercomplete:** カーソル位置だけでなく、ファイル全体を見て、変数名の変更などを同時に提案してくれます
- **Tab-to-Jump:** 次に編集すべき場所へカーソルをジャンプさせます
- **Tab-to-Import:** 未定義のクラスなどを使うと、自動でimport文を提案・追加してくれます

Tabキーを押すだけで、import文の追加から次の編集箇所の移動までやってくれるなんて...。  
「Tabキー連打してたら仕事終わってた」みたいな未来が来るかも？

### Command

自然言語でコードを生成・編集する機能です。

**ショートカット:**`Cmd + I` (Mac) / `Ctrl + I` (Win)

**使い方:**

- エディタ上で: 「ログインフォームのReactコンポーネントを作って」
- ターミナル上で: 「ポート3000を使ってるプロセスをキルして」

---

## 6\. 成果物「Artifacts」とタスク管理

エージェントは仕事の結果を **「Artifacts（アーティファクト）」** という形で提出します。  
これがAntigravityの最大の特徴の一つ。

### 主なArtifactsの種類

**1\. Implementation Plan (実装計画書)**  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/0cc7d455-84b1-4067-869a-2000410cc265.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F0cc7d455-84b1-4067-869a-2000410cc265.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3fd220f697702230063e2e04ddc2dac4)

- エージェントがコードを変更する前に作る計画書
- **重要:** ユーザーはこれを「Review (レビュー)」して、コメントで修正指示を出せます。OKなら「Proceed」で実行

**2\. Task List** [![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/718db6c4-dab8-4ea7-9593-e4dd7ce43bdd.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F718db6c4-dab8-4ea7-9593-e4dd7ce43bdd.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=db607b62c3b32d09e6a05d61c1d984ad)

- リサーチ、実装、検証などのToDoリスト。進捗状況がリアルタイムで見れます

**3\. Walkthrough**  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/d66caf39-450c-4c3a-9c22-fb8bc73f3a43.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fd66caf39-450c-4c3a-9c22-fb8bc73f3a43.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=dd9b950474f7c375d315b882b194a59b)

- 作業完了後の「まとめ」。変更内容の要約や、スクリーンショットなどが含まれます

**4\. Screenshots / Browser Recordings**  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/39709742-a7ff-483d-a951-cd122ce92d72.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F39709742-a7ff-483d-a951-cd122ce92d72.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ed0f41ec58d1fcba3bb2473c31c3a865)

- ブラウザ操作の証拠画像や動画
- 「ブラウザで見て確認して」とプロンプトを打つと実際にブラウザを確認してれます。

### ちなみに、私のmacでは最初動かず、、、以下実施でうまく動きましたメモシェアです。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/db1097d4-92af-49a7-9bec-08a97f537c6d.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fdb1097d4-92af-49a7-9bec-08a97f537c6d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=99efcdfe1d4111ca4425d9368f071d3a)  
Antigravityインストール後に手作業で

・アクセシビリティをON  
・Antigravityユーザー認証をGoogle Workspaceユーザーではなく個人ユーザーに切り替え  
・Mac自体を再起動してAntigravityを開く  
・「ブラウザで見て確認して」とプロンプトを打つと承認ボタン出る  
・Antigravity Browser Extensionを開いたブラウザで拡張機能インストール( [https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd](https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd) )

でBrawser機能使えるようになりました🙌  
うまく動かない方ぜひお試しください。

### レビューポリシー設定

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/b630525a-7954-46ba-91f3-283aabd95063.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fb630525a-7954-46ba-91f3-283aabd95063.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=251957a355593d76fdd821af6a4bc0bc)

エージェントがいちいち許可を求めてくるのが面倒な場合、設定で変更できます。

- **Request Review:** 常に人間がレビューする（デフォルト推奨）
- **Agent Decides:** エージェントが自信があるときは勝手に進める
- **Always Proceed:** ノーチェックで突き進む（勇者向け）

最初は「Request Review」にしておきましょう。  
エージェントの提案が意図と違うことはよくあるので、実装前にコメントで軌道修正できるのはめちゃくちゃ便利です。

---

## 7\. 革命的機能：Browser Agent

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/6b46bc14-b02d-4fc0-8c5c-cdae7d53dd19.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F6b46bc14-b02d-4fc0-8c5c-cdae7d53dd19.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b742aea768bea6d8ed0b2322c5925098)

Antigravityの真骨頂、ブラウザ操作機能です。

### 何ができるの？

- **操作:** クリック、スクロール、入力、コンソールログの読み取り
- **視覚:** スクリーンショット、DOMのキャプチャ、動画撮影
- **独立性:** 「Separate Chrome Profile」で動作します。つまり、普段使いのChromeのクッキーやログイン状態とは隔離されます

「ローカルサーバー(localhost:3000)で立ち上げたアプリの動作確認をして」みたいなタスクを丸投げできるわけです。

しかも別プロファイルだから、自分のGmailセッションが切れたりする心配もなし。  
考えられてるな〜。

### Browser Subagent

メインのエージェントとは別に、ブラウザ操作に特化したモデル（Gemini 2.5 Pro UI Checkpointなど）が裏で動きます。

操作中は、ブラウザ上に青い枠とアクション内容が表示され、人間が邪魔しないようにロックされます。

### セキュリティ（Allowlist / Denylist）

勝手に怪しいサイトに行かないよう、2段階の保護があります。

**1\. Denylist:** Googleが管理する「危険なURLリスト」。アクセス不可  
**2\. Allowlist:** ユーザーが許可したURLリスト

- リストにないサイトに行こうとすると、「許可しますか？」とポップアップが出ます

### Chrome Extension

Antigravityがブラウザを制御するために必須の拡張機能です。  
初回起動時にインストールを求められます。

🔗Antigravity Browser Extension - Chrome ウェブストア  
　　URL: [https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd](https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd)

---

## 8\. Agent Manager：全知全能の管理画面

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/bf995e07-8384-47a1-abd7-faa452643850.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fbf995e07-8384-47a1-abd7-faa452643850.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=980bdd59135cb00aff543046508a1650)

`Cmd + E` で開く、もう一つの画面です。

### Workspaces (ワークスペース)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/054e4a22-6701-4d44-8e7a-59baf9e24d71.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F054e4a22-6701-4d44-8e7a-59baf9e24d71.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4cdd39770454684ecc8527ce3a8d848c)

複数のプロジェクト（フォルダ）を同時に管理できます。  
サイドバーからフォルダを選んで、それぞれのワークスペースで別のエージェントを走らせることが可能。

複数のリポジトリを行き来するシニアエンジニアには最高の機能。  
Aのプロジェクトでビルド待ちの間に、Bのプロジェクトのバグ修正をエージェントに指示する...なんてマルチタスクが可能になります。

### Inbox (インボックス)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/302076d7-1d75-4064-a69b-301ed57b7bbd.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F302076d7-1d75-4064-a69b-301ed57b7bbd.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=80e146daec14c138b795a769919e495c)

全てのスレッドの通知センター。  
「ターミナルコマンドの実行許可待ち」「ブラウザ操作の許可待ち」などのタスクがここに集約されます。

### Playground (プレイグラウンド)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/0dd57512-26f4-4ce1-bf49-6525405fd1d1.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F0dd57512-26f4-4ce1-bf49-6525405fd1d1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=617c90bf25c51f4b0e22a86a130f708c)

特定のフォルダに紐付かない、一時的な実験場。  
「ちょっとこのコード試したい」という時に使い、気に入ったら後でワークスペースに保存（Move）できます。

---

## 9\. 拡張機能：MCPとKnowledge

Antigravityをさらに賢くする機能たちです。

### MCP (Model Context Protocol)

エディタと外部ツールを繋ぐ規格です。

**何ができる？**

- Postgresのスキーマを読み込んでSQLを書かせる
- Linearのチケットを作成する
- Notionのドキュメントを検索する

**導入方法:** エディタ上部の「...」メニュー > MCP Store からインストール

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/5f9c1ded-ab18-4c10-a06e-9e160a322a89.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F5f9c1ded-ab18-4c10-a06e-9e160a322a89.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f2db2e86f89c0c56068995f78022d59d)

これ、今話題のMCPです。  
コンテキスト（文脈）として外部ツールの情報をAIに渡せるので、「Linearのチケット #123 の内容に基づいて修正して」みたいな指示が通るようになります。

### Knowledge (ナレッジ)

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/e19e0329-86dd-4378-8bef-490e7d474d3e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fe19e0329-86dd-4378-8bef-490e7d474d3e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=af203ecd5f595b4dfd33812ef8fa3366)

Antigravityの「記憶」です。

会話の中で得た重要な洞察、パターン、解決策を自動的に「Knowledge Item」として保存します。  
次回以降、エージェントはこの記憶を参照して、より賢く振る舞います。

---

## 10\. 設定・制限・FAQ

最後に、知っておくべき細かい仕様です。

### 料金プラン

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/ae2855cc-230d-49ef-9cbe-57417a63eabc.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2Fae2855cc-230d-49ef-9cbe-57417a63eabc.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=1aa1d8f8345fc25465e3b9565f500d24)

2025/11/20現在は **No-cost Public Preview（無料プレビュー）** です。

**Rate Limits (制限):**

- 5時間ごとにクォータ（利用枠）がリセットされます
- 一般的な使用なら上限には達しない設計ですが、使いすぎには注意

### 便利な設定 (Settings)

`Cmd + ,` で設定を開けます。

**Terminal Command Auto Execution:**  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/12d5b78a-d0e0-434f-9b62-28623a759eba.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F12d5b78a-d0e0-434f-9b62-28623a759eba.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=482c0e41122d93c0603706dd0faa22ad)

- **Off:** 常に許可を求める
- **Auto:** エージェントが判断
- **Turbo:** リスクのあるコマンド以外はガンガン実行（上級者向け）

### Theme

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/435233/3e80e301-5c8c-429c-bc0a-d4ee0af1efdc.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F435233%2F3e80e301-5c8c-429c-bc0a-d4ee0af1efdc.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=cbb63dc28e5446177dda34c6a8e52e05)

VS Codeベースなので、お好みのテーマが使えます。

### よくある質問 (FAQ)

**Q: PCがスリープしたらどうなる？**  
A: エージェント稼働中は、AntigravityがPCのスリープを阻止してくれます。

**Q: 拡張機能は使える？**  
A: Open VSX marketplaceからVS Code互換の拡張機能をインストール可能です。

**Q: サポートは？**  
A: プレビュー期間中は `antigravity-support@google.com` へ（英語推奨）。

---

## まとめ

Google Antigravityは、単なるコード補完ツールではなく、 **「一緒に働いてくれるAI同僚」** をPCの中に住まわせるような感覚のツールです。

### ここがすごい

1. **Agent** が計画・実装・ブラウザ確認まで自律的にやってくれる
2. **Artifacts** で成果物をレビューしながら進めるので、AI任せでも安心
3. **Browser Agent** でWebアプリの動作確認まで自動化できる

今はまだプレビュー版ですが、これからの開発スタイルのスタンダードになる可能性を秘めています。

Mac (Apple Silicon) ユーザーの方は、ぜひ今すぐダウンロードして、未来の開発体験を味わってみてください。

最後まで読んでくれてありがとうございます。長かったですよね。  
でも、これだけの機能が詰まってるんです。

ぜひ実際に触ってみて、エージェントがブラウザを勝手に動かし始めた時の「おぉ...」という感動を味わってください。

それでは、良いコーディングライフを。

### 参考

・Google Antigravity  
　　URL: [https://antigravity.google/](https://antigravity.google/)

・Google Antigravity Documentation  
　　URL: [https://antigravity.google/docs/browser](https://antigravity.google/docs/browser)

[3](https://qiita.com/akira_papa_AI/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fakira_papa_AI%2Fitems%2F0acf2679e4ce9f7fb153&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fakira_papa_AI%2Fitems%2F0acf2679e4ce9f7fb153&realm=qiita)