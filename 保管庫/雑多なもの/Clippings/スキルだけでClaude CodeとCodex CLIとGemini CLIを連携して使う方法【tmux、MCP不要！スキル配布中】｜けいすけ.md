---
title: "スキルだけでClaude CodeとCodex CLIとGemini CLIを連携して使う方法【tmux、MCP不要！スキル配布中】｜けいすけ"
source: "https://note.com/konho/n/nece15d7b08af"
author:
  - "[[けいすけ]]"
published: 2026-02-10
created: 2026-03-09
description: "こんにちは。けいすけです。  動画にもしました。動画が良いよー！という方はどうぞ。    簡単に説明しますと、Claude CodeやCodex CLIなどのエージェントって、コマンドラインで動くので多重起動して並列化やできるんですよね。  で、その方法はいろいろあって多く用いられる手法はtmuxを使うものです。  ですが、どうもtmuxを使う方法だと、自分の使い方だとしっくりこなかったので、skillだけで連携する方法を紹介します。  たとえば、Claude Codeを起動するときは、コマンドラインに  claude  と入力しますよね。  ですが、このように入力すると、単発の質問も"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/250589232/rectangle_large_type_2_a10bad2e7c4cb09acbf1cd7947f5e4d4.jpeg?width=1280)

## スキルだけでClaude CodeとCodex CLIとGemini CLIを連携して使う方法【tmux、MCP不要！スキル配布中】

[けいすけ](https://note.com/konho)

こんにちは。けいすけです。

動画にもしました。動画が良いよー！という方はどうぞ。

簡単に説明しますと、Claude CodeやCodex CLIなどのエージェントって、コマンドラインで動くので多重起動して並列化やできるんですよね。

で、その方法はいろいろあって多く用いられる手法はtmuxを使うものです。

ですが、どうもtmuxを使う方法だと、自分の使い方だとしっくりこなかったので、skillだけで連携する方法を紹介します。

たとえば、Claude Codeを起動するときは、コマンドラインに

```
claude
```

と入力しますよね。

ですが、このように入力すると、単発の質問もできるんです。

```javascript
claude -p "雨はなぜふるの？"
```

このように返ってきます。

![画像](https://assets.st-note.com/img/1770696048-5Ynjm8kNtKXFp3eW671BMwOR.png?width=1200)

これは、Claude Codeの他にも、Codex CLIにもGemini CLIにも同様の事ができます。

つまり！Claude Code（あるいは他のコーディングエージェント）から、コマンドラインで質問をしてあげれば良いんです。

あと、セッションを継続するためのパラメーターもあるので、会話履歴を引き継ぐ事も可能です。（このあたりは動画でも解説しています。）

ちなみに、スキルは以下で配布しています。

けいすけメルマガ（無料だよ）に登録してくださった方に配布していますのでぜひ！

[**スキルだけでClaude CodeとCodexとGeminiを連携させるスキルプレゼント** *kov.jp*](https://kov.jp/p/r/qqnU67Nw)

  

スキルだけでClaude CodeとCodex CLIとGemini CLIを連携して使う方法【tmux、MCP不要！スキル配布中】｜けいすけ