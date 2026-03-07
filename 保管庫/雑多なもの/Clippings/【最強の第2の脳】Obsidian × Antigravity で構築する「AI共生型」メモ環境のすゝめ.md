---
title: "【最強の第2の脳】Obsidian × Antigravity で構築する「AI共生型」メモ環境のすゝめ"
source: "https://qiita.com/hoge_kawamuro/items/341a8bca794a0ddff0de"
author:
  - "[[hoge_kawamuro]]"
published: 2025-12-18
created: 2026-03-08
description: "「メモを取っても、活用できていない気がする…」 「AIに自分の知識を学習させたいけど、設定が面倒…」 そんな悩みを持つあなたへ。 「書く」ことに特化したObsidianと、「考える」ことを拡張するAntigravity。 この2つを組み合わせることで、爆速で書き、AIと深く..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiitaにログインして、便利な機能を使ってみませんか？

あなたにマッチした記事をお届けします

便利な情報をあとから読み返せます

[ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fhoge_kawamuro%2Fitems%2F341a8bca794a0ddff0de&realm=qiita) [新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fhoge_kawamuro%2Fitems%2F341a8bca794a0ddff0de&realm=qiita)

「メモを取っても、活用できていない気がする…」  
「AIに自分の知識を学習させたいけど、設定が面倒…」

そんな悩みを持つあなたへ。  
**「書く」ことに特化したObsidian** と、 **「考える」ことを拡張するAntigravity** 。  
この2つを組み合わせることで、爆速で書き、AIと深く対話する「 **最強のメモ環境** 」が完成します。

本記事では、その **運用の哲学** から、誰でも今日から始められる **具体的な構築手順** までを完全解説します。

---

## 🚀 なぜこの組み合わせなのか？

この2つは「競合」ではなく「協力者」です。脳みその違う部分を使うイメージで使い分けます。

| **ツール** | **役割のイメージ** | **特徴・得意なこと** |
| --- | --- | --- |
| **Obsidian** | **「高速な右脳」**   (インプット・思考) | ・ **とにかく軽い** 。一瞬で起動して書ける。   ・リンク機能でアイデアをつなげるのが得意。   ・プラグインで見た目や操作を自分好みに改造できる。   ・ **「書くこと」に集中する場所。** |
| **Antigravity** | **「賢い左脳（秘書）」**   (アウトプット・分析) | ・ **AIが強力** 。メモ全体を読んでくれる。   ・「要約して」「整理して」「コード書いて」が得意。   ・VS Codeベースなのでエンジニア的な編集も可能。   ・ **「相談・活用」する場所。** |

---

## ✍️ なぜ「書く」のはObsidianなのか？

Antigravity（VS Codeベース）でも文字は書けますが、あえて\*\*「書き込み」をObsidianに集約すべき理由\*\*があります。

### ① 思考を止めない「圧倒的な軽さ」

Obsidianはローカルアプリであり、起動が一瞬です。「あ、これメモしたい」と思った瞬間に書き始められます。この\*\*「思考のスピードに追いつくレスポンス」\*\*こそが、知的生産において最も重要です。

### ② 知識を編み上げる「リンク機能」

`[[ブラケット]]` で囲むだけで作れる内部リンクが、情報を有機的に繋げます。フォルダ分けに悩む必要はありません。リンクさえしておけば、後でグラフビューで意外な繋がりを発見できます。

### ③ データは「ただのテキストファイル」

Obsidianのデータは、PC上のフォルダにある\*\*ただのMarkdownファイル（.md）\*\*です。  
これがAntigravityとの連携の鍵です。独自のデータベースではないため、Antigravity（VS Code）からもそのまま開いて編集できるのです。

---

## 🔄 具体的なワークフロー

### 🟢 Obsidianを使うシーン（日常の9割）

普段のメモ書きは、これまで通りObsidianで行います。

- **デイリーノート:** 「今日のタスク」や「ふと思ったこと」をサッと書く。
- **会議メモ:** 議事録をバーッと打ち込む。
- **モバイル:** スマホアプリで移動中もメモ。

### 🔵 Antigravityを使うシーン（ここぞという時）

「溜まったメモをどうにかしたい」「新しい知見を得たい」時にAntigravityを起動します。

- **RAG相談（AI壁打ち）:**
	- 「最近『AI』について書いたメモを全部探して、重要なポイントをまとめて」
	- 「過去の議事録から、Aプロジェクトの懸念点をリストアップして」
- **週次レビューの自動化:**
	- 「今週のデイリーノートを読んで、やったこと・わかったことを要約して『週報』を作って」

---

## 🛠️ 導入手順（今日から始められます！）

「便利そうだけど、設定が難しそう…」と思った方も安心してください。  
以下の手順通りに進めれば、 **15分程度** で環境が整います。

### 1\. 事前準備

以下の3つがインストールされていることを確認してください。

- **Obsidian**
- **Google Antigravity**
- **Git** (ターミナルで `git --version` で確認)

### 2\. Obsidian側の設定（Git化）

まず、ローカルのObsidian VaultをGitリポジトリとして初期化します。

1. **プラグインの導入:**
	- Obsidianの `Settings` > `Community plugins` > `Turn on community plugins` を有効化。
	- 「Browse」から **「Obsidian Git」** (by Vinzent) を検索し、インストール → **Enable（有効化）** 。
2. **リポジトリの初期化:**
	- `Cmd + P` (Winは `Ctrl + P`) でコマンドパレットを開く。
	- **`Git: Initialize a new repo`** を実行。
3. **初回のコミット:**
	- コマンドパレットから **`Git: Commit all changes`** を実行。
	- 通知で「Committed X files」と出ればローカル保存完了です。

### 3\. Antigravity側の設定（AI環境整備）

ObsidianのフォルダをAntigravityで開き、AIが読みやすいように整えます。

1. **フォルダを開く:**
	- Antigravityを起動し、 `File` > `Open Folder` から **ObsidianのVaultフォルダ** を選択して開く。
2. **除外設定（.gitignore）の作成:**
	- Antigravityのチャット（Agent）に以下を指示して実行させます。
	> 「ここはObsidianのVaultです。RAGの精度確保のため、システムファイルである `.obsidian` フォルダと `.git` フォルダを除外する `.gitignore` ファイルを作成してください。」

### 4\. GitHub側の設定（バックアップ先作成）

データのバックアップ先となる「箱」を用意します。

1. **リポジトリ作成:**
	- GitHubで `New repository` をクリック。
	- **Repository name:** 任意（例: `obsidian-notes` ）。
	- **Public/Private:****必ず `Private` （非公開）** を選択。
	- その他は何もチェックせず `Create repository` 。
	- 作成後の **HTTPS URL** をコピー。
2. **トークン発行:**
	- GitHub設定の `Developer settings` > `Personal access tokens (classic)` へ移動。
	- `Generate new token (classic)` をクリックし、 **`repo`** にチェックを入れて生成。
	- トークン（ `ghp_...`）をコピーして控えておく。

### 5\. 連携とアップロード（Push）

Antigravityのターミナル機能を使って接続します。

1. **リモートの追加:**
	- Antigravity上で `Terminal` > `New Terminal` を開く。
	- 以下のコマンドを入力（URLは自分のものに書き換え）。
	```bash
	git remote add origin [https://github.com/ユーザー名/リポジトリ名.git](https://github.com/ユーザー名/リポジトリ名.git)
	```
2. **初回アップロード:**
	```bash
	git push -u origin main
	```
	- **Username:** GitHubのユーザー名
	- **Password:** 先ほど発行した **トークン** を貼り付け

---

## 💡 日々の運用ルーティン

これだけで環境構築は完了です！あとは日々使い倒すだけ。

1. **Obsidianで書く:** 思考をどんどん書き出す。
2. **Obsidianで保存:** 作業区切りで `Cmd + P` → `Git: Commit all changes` （自動保存設定もおすすめ）。
3. **Antigravityで対話:** 悩んだらAntigravityを開き、自分のメモを元にAIと壁打ち。

あなたの「第2の脳」が、これまで以上に強力なパートナーになることを約束します。  
ぜひ、今日から試してみてください！

[0](https://qiita.com/hoge_kawamuro/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fhoge_kawamuro%2Fitems%2F341a8bca794a0ddff0de&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fhoge_kawamuro%2Fitems%2F341a8bca794a0ddff0de&realm=qiita)