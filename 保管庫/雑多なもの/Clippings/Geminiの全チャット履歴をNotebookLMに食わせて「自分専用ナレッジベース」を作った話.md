---
title: "Geminiの全チャット履歴をNotebookLMに食わせて「自分専用ナレッジベース」を作った話"
source: "https://zenn.dev/minipoisson/articles/d8b307f8eedc5f"
author:
  - "[[Zenn]]"
published: 2026-01-14
created: 2026-03-09
description:
tags:
  - "clippings"
---
42

41[tech](https://zenn.dev/tech-or-idea)

## はじめに：Geminiとの対話は「知的資産」だ

日々、プログラミングのデバッグやアイデア出しに Google Gemini を活用している方は多いと思います。しかし、その膨大なチャット履歴、「使い捨て」にしていませんか？

Gemini の履歴は、自分の思考プロセス、ハマったエラー、解決策が詰まった「 **知的ライフログ** 」そのものです。しかし、標準の履歴機能やキーワード検索だけでは、「あの時どうやって解決したっけ？」「最近の自分、どんな技術に触れてた？」といった **俯瞰的な分析** や **文脈検索は困難** です。

そこで、「 **Gemini の全履歴を NotebookLM に読み込ませて、自分専用の最強検索＆分析AIを作る** 」ことを試みました。そのための Python ツールも自作し、OSS として公開しましたので紹介します。

## 課題：JSON は NotebookLM に優しくない

Google Takeout を使えば、Gemini の履歴を JSON 形式（ `MyActivity.json` ）でエクスポートできます。しかし、これをそのまま NotebookLM に投げてもうまくいきません。

1. **データ構造の問題**: JSON はデータ構造重視の形式であり、NotebookLM が得意とする「文脈のある文章」ではない。
2. **ノイズ**: 不要な HTML タグやメタデータが多く、AIのノイズになる。
3. **容量制限**: NotebookLM の1ソースあたりの制限（文字数やファイルサイズ）に引っかかる。

これらを解決するために、専用の変換スクリプトを作成しました。

## 自作ツール: Gemini\_Json2md4NotebookLM

作成したツールは GitHub で公開しています。

### 主な機能

Python 標準ライブラリのみで動作するシンプルなスクリプトです。

1. **HTMLタグ除去 & Markdown 整形**  
	チャットログに含まれる `<div>` や `<br>` などを除去し、可読性の高い Markdown 形式に変換します。これにより NotebookLM が文脈を理解しやすくなります。
2. **自動ファイル分割**  
	NotebookLM の制限を考慮し、指定したサイズ（デフォルト 1.5MB）を超えると自動でファイルを分割して連番（ `Gemini_History-00.md`, `-01.md`...）を出力します。
3. **差分更新への対応**  
	`last_entry_time.txt` に最終処理日時を記録することで、次回以降は「新しく増えた会話分」だけを追記・出力できるようにしています。これで日々の運用が楽になります。

## 使い方

1. Google Takeout で「マイ アクティビティ」のみを選択し、アクティビティの記録の形式として JSON を選択し、サービスとして「Gemini アプリ」のみを選択してエクスポートし、ダウンロード。
2. `MyActivity.json` （日本語では `マイアクティビティ.json` ）をスクリプトと同じ階層に置く。
3. コマンドを実行。

```
python convert_history.py --input_file MyActivity.json --output_file Gemini_History.md --limit 2000000
```

あとは生成された Markdown ファイルを NotebookLM にアップロードするだけです 。  
![](https://storage.googleapis.com/zenn-user-upload/6eae53727d4b-20260114.png)

## 実践：NotebookLM で自分を分析してみた

実際に数年分の履歴を NotebookLM に読み込ませて、いくつか質問をしてみました。これが想像以上に面白い結果になりました。

1. プログラミング履歴の棚卸し
	プロンプト: 「Python, C#, Rust, JavaScript, VBA, PowerShell, Windows Command Prompt で実際に作成・デバッグ・完成したプロジェクトを列挙して」

この質問に対し、NotebookLM は正確にプロジェクトをリストアップしてくれました。面白かったのは Rust に関する回答です。

```
回答: Rust については「具体的なプログラム作成・デバッグの記述は履歴に見当たりません」
```

確かに Rust は記事を読んだ程度で、Gemini とコードを書いたことはありませんでした。ハルシネーション（嘘）を起こさず、「やっていないことはやっていない」と答えてくれる信頼性があります。 ![](https://storage.googleapis.com/zenn-user-upload/e6bccbdb0fbf-20260114.png)

1. 「自分の開発傾向」を客観視する

NotebookLM に自分のエラー傾向や強みを分析させてみました。自分では気づきにくい癖が言語化されます。

- よく遭遇するエラーの傾向
	- 外部 API の認証エラー（Google API 429/403 等）
	- C# の Dispose 忘れによるリソースロック
	- Python の f-string 構文エラーなどの細かいミス
- 解決アプローチの特徴
	- まずは「動く最小構成」を作って検証する傾向がある 。
	- ログやスタックトレースを徹底的に提示して解決を図る 。
- エンジニアとしての強み（AIによる分析）
	- 複数言語・技術の統合力
	- 国際化（I18n）への理解
	- 堅牢性へのこだわり

「国際化への理解」などは、確かに多言語対応のツールを作ったりしていたので、AI は文脈からそこを評価してくれたようです。

## まとめ

Gemini の履歴を Markdown 化して NotebookLM に入れることで、過去の自分が取り組んだ課題や解決策をいつでも引き出せる「 **第二の脳** 」が完成しました 。

自分の開発傾向を客観的に指摘してもらう「AIコードレビュー」のような使い方もできるので、Gemini ヘビーユーザーの方はぜひ試してみてください。

スクリプトは MIT License で公開しています。

42

41

### Discussion

![](https://static.zenn.studio/images/drawing/discussion.png)

ログインするとコメントできます

42

41