---
title: "実装はClaude、レビューはCodex ─ tmuxで繋ぐ開発フロー"
source: "https://zenn.dev/tokium_dev/articles/0ef3f807d67e7c"
author:
  - "[[Zenn]]"
published: 2026-01-30
created: 2026-03-09
description:
tags:
  - "clippings"
---
[TOKIUMプロダクトチーム テックブログ](https://zenn.dev/p/tokium_dev)

158

72[tech](https://zenn.dev/tech-or-idea)

この記事では、複数のAIエージェントを組み合わせた開発フローと、それを支える環境構築のTipsを紹介します。

私はClaude CodeやCodexといったAIエージェントを毎日使っています。ただ単体で使っているとどうしても「このAIの判断、本当に正しいのかな？」と不安になることがあります。

そんな課題を解決するために試している「Claude CodeからCodexを呼び出してクロスチェックする」というフローを紹介します。

Claude Codeは非常に優秀で、実装からレビューまでこなしてくれます。ただ同じセッションで繰り返し確認を求めても、同じ視点からの回答になることはありませんか。

ここに課題があります。

- 毎回、何回聞いても同じ視点からの回答になる
- 局所解に落ちても気づけない
- 違う視点が欲しくなる

人間の開発でも、自分で書いたコードを自分でレビューするより、別の人にレビューしてもらったほうが見落としを発見できますよね。  
別のAIにセカンドオピニオンを求めることで、仕様面や実装面の見落としを検出できるのではないか、という仮説を立てました。

## 開発フローの全体像

前提として私の開発環境を紹介すると、ターミナルエミュレータはiTerm2、ターミナルマルチプレクサはtmuxです。 [^1]  
（この構成になって5年ほど経ちます。Claude Codeが流行り始めてtmuxが注目を浴びるようになって喜ばしい限りです）

私の現在の開発フローは以下のようになっています。

```
Jira（任意のチケット管理ツール）
    ↓ Atlassian MCP Server
Claude Code（実装・セルフレビュー）
    ↓ tmux-sender
Codex（クロスチェック）
    ↓
フィードバック反映・Pull Request作成
    ↓
GitHub Copilotが自動レビュー
    ↓
人間がレビュー
```

今回はClaude CodeとCodexの連携部分のステップに関して詳しく説明します。

## MCPサーバでチケット情報を取り込む

開発の起点はJiraのチケットです。Atlassian MCP Serverを使うと、Claude Codeから直接チケット情報を取得できます。

具体的には、以下のような操作が可能です。

- チケット番号を指定して要件を取得
- 担当者で絞り込んで自分のタスクを一覧表示
- ステータスで絞り込み（TODOのチケットから実装計画を立てる、レビュー中のチケットをレビューするなど）

```
「PROJ-123の要件を確認し、実装して」
「自分がアサインされているTODOのチケットを見せて」
「ステータスがレビュー中のチケットをレビューして」
```

Atlassian MCP Serverの活用に関しては、同僚が紹介していますのでぜひご覧ください。

## "tmux-sender"で別ペインにコマンドを送る

ここからが本題です。Claude Codeには「Skills」という機能があり、カスタムコマンドを定義できます。

グローバルに設定したい場合は `~/.claude/skills/` 配下にMarkdownファイルを置いて使えます。プロジェクトごとの設定も可能です。

私が作成した"tmux-sender"は、tmuxの別ペインにコマンドを送信するためのSkillです。

```
# ~/.claude/skills/tmux-sender/SKILL.md
---
name: tmux-sender
description: tmux の別ペインにコマンドを送信する。「ペインで実行して」「tmuxで送信」などのリクエストで使用。
allowed-tools: Bash(tmux:*)
---

# tmux コマンド送信スキル

## 使い方

tmux のペインにコマンドを送信して実行する場合：

tmux send-keys -t <ペイン番号> '<コマンド>' Enter

## 手順

1. tmux list-panes でペイン一覧を確認
2. tmux send-keys -t <ペイン番号> '<コマンド>' Enter で送信・実行
```

`allowed-tools: Bash(tmux:*)` で、このSkillがtmuxコマンドのみを実行できるように制限しています。これを定義しないと「ペイン1でnpm run devを実行して」のような指示がそのまま通ります。

## レビュー観点をSkillで定義する

別ペインのCodexにレビューを依頼する前に、まずClaude Code自身でセルフレビューを行います。その際、ただ闇雲に「レビューして」と指示しているわけではありません。レビューの観点もSkillとして定義しています。

```
# ~/.claude/skills/review/SKILL.md
---
name: review
description: コードレビューを行う。「レビューして」「コードレビュー」などのリクエストで使用。
allowed-tools: Read, Grep, Glob, Bash(git diff:*), Bash(git log:*), Bash(git show:*)
---

## レビュー観点

以下の観点でコードを確認する

1. 可読性
   - 変数名・関数名はわかりやすいか
   - コードの意図が伝わるか

2. バグの可能性
   - エッジケースの考慮漏れがないか
   - nullやundefinedの扱いは大丈夫か

3. パフォーマンス
   - 明らかに非効率な処理がないか
   - 不要な再計算・再レンダリングがないか

4. セキュリティ
   - 入力値の検証は適切か
   - 機密情報の扱いは問題ないか

5. テスト
   - テストは書かれているか
   - テストのカバレッジは十分か
```

これはあくまで一例ですが、あらかじめ何かしらの評価基準・観点を明示しておくことで、レビューの品質が安定します。

## Claude CodeからCodexを呼び出す

tmux-senderの真価は、別のAIエージェントを呼び出せることです。

例えば、以下のようなtmuxのペイン構成があるとします。

```
+------------------+------------------+
|                  |                  |
|   Claude Code    |     Codex        |
|    (ペイン0)      |    (ペイン1)      |
|                  |                  |
+------------------+------------------+
```

Claude Codeで実装とセルフレビューを終えたら、以下のように指示します。

```
「ペイン1で、今の変更内容をCodexでレビューして」
```

Claude Codeが `tmux send-keys` でCodexにプロンプトを送信し、Codexがレビューを開始します。

![](https://storage.googleapis.com/zenn-user-upload/8e50e3139775-20260120.gif)

## Codex側にもSkillを設定する

CodexにもSkills機能があります。

`~/.codex/skills/` 配下にMarkdownファイルを置くことで、Claude Codeと同様にカスタムコマンドを定義できます。

Codex側にもtmux-senderとreview Skillを設定することで、双方向のやり取りが可能になります。

```
# ~/.codex/skills/tmux-sender/SKILL.md
---
name: tmux-sender
description: tmux の別ペインにコマンドを送信する。「ペインで実行して」「tmuxで送信」「Claude Codeに依頼して」などのリクエストで使用。
metadata:
  short-description: tmuxペイン間コマンド送信
---

# tmux コマンド送信スキル

## 使い方

tmux のペインにコマンドを送信して実行する場合：

tmux send-keys -t <ペイン番号> '<コマンド>' Enter

## 手順

1. tmux list-panes でペイン一覧を確認
2. tmux send-keys -t <ペイン番号> '<コマンド>' Enter で送信・実行
```

```
# ~/.codex/skills/review/SKILL.md
---
name: review
description: コードレビューを行う。「レビューして」「コードレビュー」などのリクエストで使用。
metadata:
  short-description: コードレビュー用スキル
---

## レビュー観点

以下の観点でコードを確認する

1. 可読性
2. バグの可能性
3. パフォーマンス
4. セキュリティ
5. テスト
```

これにより、Codexからの指摘を受けてClaude Codeに追加の修正を依頼する、といった往復のやり取りも可能になります。

```
Claude Code → Codex「このコードをレビューして」
    ↓
Codex → Claude Code「エラーハンドリングが不足している。修正して」
    ↓
Claude Code → Codex「修正した。再レビューして」
```

### 現時点での制限

`Codex → Claude Code` に対するリクエストの場合、 `tmux send-keys` でプロンプトを送信しても、自動的に実行されません。Claude CodeはインタラクティブなTUIで独自のキー入力処理をしているため、テキストは入力バッファに届きますが、実行は手動で行う必要があります。プロンプトを手打ちする手間は省けますが、送信後は受け取り側のペインで確認・実行する運用になります。

`Claude Code → Codex` の場合は自動的に実行してくれます。

（2026年1月時点での筆者の検証結果を踏まえた見解）

## 実際に得られた効果

これらのフローを導入してから、以下のような効果がありました。

- 仕様の考慮漏れを検出：Claude Codeが見落としていたエッジケースをCodexが指摘してくれることがある
- 実装方針の妥当性確認：「この設計で本当に良いのか」という不安が軽減された
- 異なる視点からのフィードバック：同じAIに聞き直すより、別のAIに聞いたほうが多角的な指摘が得られる

もちろん、両方のAIが同じ見落としをする可能性もあります。

複雑なビジネスロジックの誤りなどを見抜けないことがあるので、最終的には人間が責任を持ってレビューをしないといけません。

## まとめ

本記事では、Claude CodeとCodexを組み合わせたクロスチェック開発フローを紹介しました。tmux-senderスキルを使って別ペインのAIエージェントにレビューを依頼することで、単一AIの視点に偏らない開発が可能になります。

脚注

158

72

この記事に贈られたバッジ

![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-5.svg) ![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-3.svg)

158

72

[^1]: 最近WezTermとかGhosttyが流行っていますね。気になる。なおコードエディタはNeovimとVSCodeを使っています。