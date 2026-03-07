---
title: "【Obsidian×NotebookLM】AI時代のインプット・アウトプット方法 - SAKURUG TECHBLOG"
source: "https://techblog.sakurug.co.jp/article/obsidian_notebooklm_googledrive/"
author:
published: 2025-12-08
created: 2026-03-08
description: "僕の最近の課題として、AIを使用しすぎて考える力が低下してきました。そのため、今回はアウトプットの量と質を効率的にあげる手段としてObsidianとNotebooklmを使用した方法をご紹介します。"
tags:
  - "clippings"
---
## 【Obsidian×NotebookLM】AI時代のインプット・アウトプット方法

Toki

こんにちは、sakurugのtokiです。

最近はAIの進化が目まぐるしく、簡単なコーディングやデザインは知識がなくてもAIが作成してくれる時代になりました。  
しかし、AIを活用する上で重要なことは、AIが出力したアウトプットを理解して運用できているかです。もしも理解せずに運用していると、エラーやバグが起きた時にどのように対処すれば良いかからなくなります。そこで重要となるのが、技術の根本的な理解です。その為に今回はアウトプットの量と質を効率的にあげる手段としてObsidianとNotebooklmを使用した方法をご紹介します。

## このブログで解説しないこと

- Obsidianの具体的な設定方法

## 僕のObsidianの運用方法

**シンプル** かつ **迷わない** 運用を目指しています。

- ログ（アウトプット）とデータ（インプット）のタグを付与した２種類のノートに分ける
- ノート同士のつながりはタグのみで行う（AI、開発、デザイン等）
- タグは階層化させない
- ファイルの階層は分けない

## 1\. ツール選定：なぜこの4つの組み合わせが最適なのか？

本システムは、 **「手間の少ない入力」「確実な管理」「AIによる加速」** の3軸でツールを選定しました。

### 1.1. Obsidian：知識の「ローカルDB」

- **選定理由**: ローカルファーストでプライバシーが守られ、Markdown形式でGit管理が容易なため。また、Claude CodeやGemini CLIを使用することで、ターミナルからノートを編集することが可能になるため
- **本システムでの役割**: 複雑なリンク構造は使わず、 `#ログ` （アウトプット）と `#データ` （インプット）のタグ付けのみを行う「シンプルなインデックス」として利用する

### 1.2. NotebookLM：インプットを「アウトプット」に変える

- **選定理由**: Google Drive内のファイルを直接学習ソースとして取り込め、音声解説、動画解説、フラッシュカード、テスト等の多様な方法でのインプット・アウトプット方法があるため
- **本システムでの役割**: アウトプットにより、今の自分の状態を理解する

### 1.3. Google Drive：データの安全性と履歴の確保

- **Google Drive**: ObsidianのVaultを安全に同期し、NotebookLMとの連携を容易にする

## 2\. 使用イメージ：知識が循環し、基礎が固まるフロー

本システムは、 **「Obsidianへデータを蓄積」→「過去のインプットを知る」→「Notebooklmでアウトプット」→「ログ化（現状把握）」** の3ステップで構成されます。

### 2.1. 知識の入力と分類（Web Clipper → Obsidian）

1. **インプット**: [Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf?hl=ja&pli=1) で収集した技術記事やインプットしたい情報をObsidianに記録。
	試しに、下記URLを要約してObsidianにノートを作成します。
	[https://typescriptbook.jp/overview/features](https://typescriptbook.jp/overview/features)
	![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/5b002b73a49143cdb448e314b6b77af9/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-26%2017.26.03.png)
	10秒ほどすると要約が完了し、下記のようにObsidianにノートが作成されます
	![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/a80afb6f8a3c46e990b935e13e19564b/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-26%2017.27.06.png)
2. **タグ付け**: もしも手入力でノートを作成する場合には、すべてのノートに以下のルールでタグ付けします
	- **Input（今後身につけたい知識）**: `#データ`
	- **その他カテゴリとなるタグ**
	- *（例）* 読んだ技術記事 -> `#データ #Python`

### 2.2. 過去のインプットを知る（Obsidian Dataview）

- **毎日決まった時間にノートを開く**: 毎日、Obsidianの **デイリーノート** を開きます
- **振り返りテーマの自動表示**: デイリーノートに埋め込まれたDataviewクエリが、 **ちょうど「昨日、7日前、1ヶ月前」** に作成された `_データ_` を含むノート（インプットノート）を自動で一覧表示します
	この一覧が、今日NotebookLMでアウトプットを行うべきテーマとなります
![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/1b85db3a98084c83b45df0045a223d75/%E5%90%8D%E7%A7%B0%E6%9C%AA%E8%A8%AD%E5%AE%9A%E3%81%AE%E3%83%86%E3%82%99%E3%82%B5%E3%82%99%E3%82%A4%E3%83%B3.png)

### 2.3. AIによる加速とアウトプット生成（NotebookLM）

- **インプットしたいデータを設定**: DataviewでリストアップされたノートをNotebookLMにアップロードします
- 自分に合ったアウトプット方法で教材を作成し、アウトプットを行います
	右側のStudioからさまざまなインプット・アウトプット方法が選択できます。
![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/5e49fd9e09634e8c832ffaf0eea1ded4/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-26%2017.41.28.png)

### 2.4. アウトプットをログとして記録

**ログとして記録**: このノートに `#ログ` タグを付与します  
ログとして記録することで、自分の学習記録を振り返ることができます

---

## 3\. 設定手順：Dataviewクエリとフローの確立

### 3.1. Obsidian Web Clipper の設定方法

![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/9d6e02611ff6428bb49f6b47def2aa0d/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-26%2017.19.56.png)

![](https://images.microcms-assets.io/assets/730c64335a1744ccbff060ce425d00ac/92c25de402ff447abcbbafeb3dbc6176/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%202025-11-26%2017.22.19.png)

```markdown
#データ

{{"内容を簡潔に要約してください。また要点ごとにマークダウン形式で簡潔にまとめてください。その際、箇条書きや見出しを活用し重要なポイントが一目で分かるようにしてください。また、カテゴリをタグとして「#〇〇」形式で1～3つ付与してください"}}
```

### 3.2. ObsidianのDataviewテンプレート設定

1. コアプラグインから、デイリーノートを有効化
2. コミュニティプラグインから、Dataviewをインストールし有効化。設定から「Enable JavaScript queries」を有効化
3. 下記を記載したテンプレノートを作成し、デイリーノートに設定

以下のクエリをデイリーノートテンプレートに貼り付け、毎日自動で過去のテーマが発掘されるように設定します。

```
## ■ 振り返り

\`\`\`dataview
TABLE without ID file.link as ノート, file.cday as 作成日, file.mday as 最終更新日
FROM ""
WHERE 
    contains(file.name, "_データ_")
    AND (
        (file.cday = date(today) - dur(1 day) OR file.mday = date(today) - dur(1 day)) OR
        (file.cday = date(today) - dur(7 day) OR file.mday = date(today) - dur(7 day)) OR
        (file.cday = date(today) - dur(1 month) OR file.mday = date(today) - dur(1 month))
    )
SORT file.mtime DESC
```

最後までお読みいただき、ありがとうございます。  
Obsidianを使用していることにより、Claude CodeやGemini CLI等のコマンドラインから操作することができます。これにより、アウトプットの整理などにも役立つのでまたの機会にご紹介します

株式会社SAKURUGのAdvent Calendar 2025です。

会社HP： [https://sakurug.co.jp](https://sakurug.co.jp/)

ーーーーーーーーーー  
株式会社SAKURUGは「寄付月間2025」に参画しています。  
12月中のテックブログのpv数に応じて、アフリカの支援団体に寄付をおこないます。  
[https://giving12.jp/](https://giving12.jp/)  
ーーーーーーーーーー

### ▼高校生向けインターン実施中！

弊社では高校生向けにインターンを行っております！  
現役エンジニア指導の下、一緒に働いてみませんか？

[高校生インターン応募フォーム](https://cherista.sakurug.co.jp/)

### ▼カジュアル面談実施中！

カジュアル面談では、会社の雰囲気や仕事内容についてざっくばらんにお話ししています。  
履歴書は不要、服装自由、原則オンラインです。興味を持っていただけた方は、  
ぜひ以下からお申し込みください。

皆さんにお会いできることをサクラグメンバー一同、心より楽しみにしております！

[カジュアル面談応募フォーム](https://sakurug.co.jp/career/casual-interview-entry/?source=techblog)

## ABOUT ME

Toki

2024年新卒入社。フロントエンド開発をメインにNuxt3やTypeScriptのキャッチアップを行っています。