---
title: "GitHub Agentic Workflowsが登場した"
source: "https://zenn.dev/tonkotsuboy_com/scraps/ca0ab69d34b312"
author:
  - "[[Zenn]]"
published: 19日前にコメント追加
created: 2026-03-08
description: "鹿野 壮さんのスクラップ"
tags:
  - "clippings"
---
GitHub Agentic Workflowsが面白そうなのでClaude Code君に解説してもらった。  
MarkdownでGitHub actionのworkflow書けるの、すごくいいね。

以下、 Claude Codeによる要約。

---

## GitHub Agentic Workflowsとは

GitHub Actionsの上でAIコーディングエージェントを動かして、リポジトリまわりの雑務を自動化する仕組みです。Copilot CLI、Claude Code、OpenAI Codexといったエージェントに対応しています。2026年2月にテクニカルプレビューとして公開されました。

## 何が新しいのか

従来のGitHub ActionsではYAMLでビルドやテスト、デプロイを定義していました。Agentic Workflowsでは、やってほしいことをMarkdownに自然言語で書くだけでAIエージェントが動いてくれます。GitHubはこれをContinuous AIと呼んでいて、CI/CDを置き換えるのではなく補完する位置づけです。

## どんなことが自動化できるのか

記事では6つのユースケースが紹介されています。

Issueの自動トリアージでは、新しいIssueを要約してラベル付けやルーティングまでやってくれます。ドキュメントの自動更新は、コード変更に合わせてREADMEなどを書き換えます。コードの簡素化では、リファクタリングの改善点を見つけてPRを作成します。

テスト改善はカバレッジを評価して価値の高いテストを追加し、CI失敗の調査ではビルドが落ちた原因を調べて修正案を提案します。定期レポートは、リポジトリの活動状況や健康状態をまとめて自動生成します。

## ワークフローの書き方

日次レポートの具体例です。.github/workflows/daily-repo-status.md というファイルを作り、以下のように書きます。

```
---
on:
  schedule: daily

permissions:
  contents: read
  issues: read
  pull-requests: read

safe-outputs:
  create-issue:
    title-prefix: "[repo status] "
    labels: [report]

tools:
  github:
---

# Daily Repo Status Report

Create a daily status report for maintainers.

Include
- Recent repository activity (issues, PRs, discussions, releases, code changes)
- Progress tracking, goal reminders and highlights
- Project status and recommendations
- Actionable next steps for maintainers

Keep it concise and link to the relevant issues/PRs.
```

ヘッダー部分のYAMLでトリガーや権限、許可する出力を定義して、本文にやってほしいことを自然言語で書きます。これだけで毎日Issueにレポートが作られます。

## セキュリティまわり

デフォルトでは読み取り専用で動きます。PRの作成やコメントの追加といった書き込み操作はsafe outputsとして明示的に許可しないと実行されません。サンドボックスで実行され、使えるツールはホワイトリスト制、ネットワークも分離されています。

PRが自動マージされることは絶対になく、人間のレビューと承認が必須です。プロンプトインジェクション対策も組み込まれています。

## チームで使うなら

まずはコメントやドラフト、レポートといった低リスクな出力から始めるのがよさそうです。コーディング系のタスクも、新機能開発ではなくリファクタリングやテスト追加のような定型的な改善から入るのが推奨されています。ワークフローのMarkdownもコードと同様にレビュー対象として扱うべきとのこと。

実行ごとにCopilotの場合はプレミアムリクエスト約2回分の課金が発生します。

## フロントエンドエンジニア的に

PRが出たらREADMEの該当セクションを自動更新する、Storybookのドキュメントとコンポーネントの乖離をチェックする、テストカバレッジが下がったら自動でテスト追加のPRを出す、といった使い方が考えられます。YAMLで複雑なスクリプトを書く必要がなく、Markdownで意図を書くだけなので、インフラに詳しくなくても手を出しやすいです。

ログインするとコメントできます