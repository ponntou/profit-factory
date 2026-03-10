---
title: "AI軍団で天下統一が見えたと思ったら本能寺が6つ同時に燃えてて焦ったので、偵察に出したら全員まだ城の基礎工事してた"
source: "https://zenn.dev/shio_shoppaize/articles/shogun-sekigahara-battle"
author:
  - "[[Zenn]]"
published: 2026-02-13
created: 2026-03-09
description:
tags:
  - "clippings"
---
39

17[tech](https://zenn.dev/tech-or-idea)

オレのAI軍団が実務を回している間に、世の中が動いていた。

**マルチエージェント開発ツールが6つも出てきている。**

Claude Squad。Claude-Flow。Z Code。Verdent Deck。Tonkotsu。そしてAnthropic公式のAgent Teams。

やべえ。包囲されてる。

……と思った。思ったんだけど、ちょっと待てよ。こいつら、本当にうちの城を攻めてきてるのか？

Grokに偵察を命じた。X（Twitter）で最新の動向を片っ端から調べさせた。

結果。

**全員、まだ城を建ててた。**

## 前回までのあらすじ

このシリーズを初めて読む人のために3行で説明する。

Claude Code × tmuxでAI部下10人を「戦国軍団」として階層管理するシステムを作った。 [初回記事](https://zenn.dev/shio_shoppaize/articles/5fee11d03a11a1) が1,966はてブでバズって、 [家老が過労死して](https://zenn.dev/shio_shoppaize/articles/dc85db324bb3f0) 、 [足軽がCodexに転属して反乱を起こした](https://zenn.dev/shio_shoppaize/articles/shogun-codex-mutiny) 。

で、今はAI足軽8人が実務を並列でこなす体制が動いている。将軍→家老→足軽の3層構造で、殿（オレ）はスマホからntfyで指示を出すだけ。

こんな感じで。

![全9ペインで足軽が一斉に作業中。家老が左上で指揮](https://res.cloudinary.com/zenn/image/fetch/s--L0hmAZsE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/f1aa1b032945dc61c3f71a97.png%3Fsha%3Dd34695c17452cb905f70b6f034cb778105911136)  
*全軍稼働中の日常風景。左上が家老（Claude Code/Opus）、残り8ペインが足軽。この光景をBGMなしで眺めるのが日課。*

## 🔥 本能寺、燃えすぎ問題

2026年2月。Xのタイムラインを眺めていたら、こんな投稿が流れてきた。

> 「Claude Squadでマルチエージェント構築した」  
> 「Claude-Flowで60エージェント回した」  
> 「Z CodeがClaude Code統合した」  
> 「Verdent DeckがSWE-bench 1位取った」  
> 「Tonkotsu、SOC2取った」

……多くない？

1ヶ月前はうちしかいなかった（と思ってた）のに、気づいたら **本能寺が6つ同時に燃えている** 。

これは偵察するしかない。

## 🔍 偵察開始 —— GrokにXを探らせた

xAIのGrok APIを使って、Xの投稿をリアルタイムに検索できるスキルがある。x\_searchという内部ツールで、Xの投稿を直接検索して要約してくれる。

```
python3 x_search.py --topic "multi-agent AI coding tool" --mode trend --days 2
```

コスト: $0.08。8円。偵察にしては安い。

結果が返ってきた。4つのクラスターが見えた。

1. **エージェントチーム系** — Claude Squad, Verdent, Tonkotsu
2. **オーケストレーション系** — Claude-Flow, Anthropic Agent Teams
3. **IDE統合系** — Z Code, Zed
4. **CLI混合系** — multi-agent-shogun（うち）

……あれ。 **オレたちだけ「CLI混合系」として独立してる** 。

つまり、同じ戦場にいない。本能寺が燃えてるように見えたけど、よく見たら **全員違う山で城を建ててた** 。

## ⚔️ 偵察報告その1: Claude Squad —— 足軽だけの村

**Claude Squad** （smtg-ai作）。tmuxでClaude Codeを複数起動する。

```
┌─────────┬─────────┬─────────┐
│ Claude 1 │ Claude 2 │ Claude 3 │
│          │          │          │
│ (作業中)  │ (作業中)  │ (待機)   │
└─────────┴─────────┴─────────┘
         ↑ 全員同列。上司なし。
```

特徴:

- **git worktreeで各エージェントにブランチを分離** （マージコンフリクト回避）
- Claude Code以外にAider、Codex、Geminiも使える
- GitHub Star 6,000+

弱点: **階層がない** 。全員が同列。将軍も家老もいない。

これは「足軽だけの村」だ。全員が自分の判断で動く。指揮系統なし。報告なし。統制なし。

うちの軍団でいえば、家老を解雇して足軽8人を野に放ったようなもの。小規模プロジェクトならいいけど、50タスクを並列で品質管理しながら捌くとか、絶対に無理。

**誰が品質チェックするの？** 足軽が自分で自分のレビューをするの？ それ、切腹案件でしょ。

うちはこう。

![全8ペインにCodex CLIが起動。家老はClaude Codeのまま](https://res.cloudinary.com/zenn/image/fetch/s--9afXrASB--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/dc13f954aecffcf5a05aeb1a.png%3Fsha%3Daf2cc01cb7132a95d66f5da1457e43bc72b1a18a)  
*うちの軍制。家老（左上）がClaude Codeで品質管理、足軽8人がCodexで実行。指揮系統がある。Claude Squadにはこれがない。*

## ⚔️ 偵察報告その2: Claude-Flow —— 大きすぎる城

**Claude-Flow** （ruvnet作）。「エンタープライズオーケストレーションプラットフォーム」を名乗っている。

READMEを読んだ。

> 「60+エージェント対応」  
> 「SONA自己学習ルーティング」  
> 「Raft/BFTコンセンサス」  
> 「Queen-Workerアーキテクチャ」

……これ、分散データベースの論文か？

```
[Queen]
        /   |   \
   [Worker] [Worker] [Worker]
      |       |       |
   [Task]  [Task]  [Task]
```

GitHub Star **13,000+** 。npm版もある（v3.1.0-alpha.28）。数字だけ見ると最大勢力だ。

だが、2つ気になることがある。

**1つ目**: v3.1.0- **alpha**.28。alpha。このプロジェクト、 **一度も正式リリースしたことがない** 。永遠のalpha。築城中の城。

**2つ目**: GitHubのIssueを覗いたら気になるものが見えた。

> 「v3でちゃんと動かせない。スワームは立つけど仕事しない」  
> 「全MCPツールが常時ロードされてトークン爆食い」  
> 「検証パイプラインが壊れていて、成功してないのに成功と報告する」

最後のやつ。 **成功してないのに成功と報告する** 。

うちの足軽がこれやったら即切腹だぞ。

しかもAnthropicが公式でAgent Teams機能をリリースしたから、claude-flowの存在意義が問われている。 **「公式が城を建て始めたら、サードパーティの城は燃える」** という戦国あるある。

## ⚔️ 偵察報告その3: Z Code —— 異国の黒船

**Z Code** （Zhipu AI / 智譜AI作）。中国のAI企業。GLM-5（744Bパラメータ）を搭載したデスクトップエディタ。

こいつの特徴は **GUIがある** こと。ビジュアルなコードエディタで、Claude Code、Codex、Geminiをスイッチングできる。

> 「Thinking Mode: エージェントが自分で推論を分析・改善してから回答する」  
> 「History Reconstruction: 過去の会話ステップを修正・再実行できる」  
> 「Granular Permission Controls: 高リスク操作は明示的に承認が必要」

聞こえはいい。だが。

**2025年12月発表。まだβ版ですらない。**

ドキュメントを見に行ったら、「Overview」ページが1ページあるだけだった。

黒船が来たと思ったら、まだ造船所で設計図を描いてた。

## ⚔️ 偵察報告その4: Verdent Deck —— 金で兵を雇う城

**Verdent Deck** （Verdent AI作）。デスクトップ型の並列エージェント管理ツール。

こいつが一番のダークホースだ。

> SWE-bench Verified: **76.1%** — Claude CodeやCodexを抜いて1位

数字はすごい。git worktreeで隔離環境を作り、複数エージェントを並列実行。SOC2みたいなセキュリティも意識している。

だが、ビジネスモデルが気になった。

> 月額$19 / 340クレジット。追加は$20 / 240クレジット。

**従量課金** 。使えば使うほど金がかかる。

うちはClaude Code Max（$200/月定額）で無限に足軽を回している。1日に何百タスク投げても追加料金なし。

Verdentで同じことやったら、クレジットが秒で溶ける。

## ⚔️ 偵察報告その5: Tonkotsu —— 博多からの刺客

**Tonkotsu** （tonkotsu.ai）。名前が豚骨ラーメン。

> 「Stop Coding, Start Leading」  
> 「plan → code → verify のワークフロー」  
> 「SOC 2 Type I 監査完了」

macOS/Windows対応のデスクトップアプリで、開発者を「テックリード」に位置づける。エージェントが実装し、人間がレビューする。

SOC2を取ってるのは偉い。エンタープライズを狙ってる。

だが、 **Early Access** 。まだ招待制。城門が閉まってる。

そして致命的なこと: **CLIじゃない** 。GUIアプリ。

tmuxのペインを眺めながら足軽が社訓を叫ぶ体験は、GUIアプリでは絶対に再現できない。

## ⚔️ 偵察報告その6: Anthropic Agent Teams —— 本丸が動いた

Opus 4.6と同時に発表された、 **Anthropic公式のマルチエージェント機能** 。

> 「複数エージェント、並列実行、自律協調」

公式が来た。これが一番怖い。

しかも **tmuxを使っている** 。各サブエージェントがtmuxペインで動く。inbox的なメッセージングもある。

……おい。 **うちと同じ構造じゃねーか。**

ただし、違いがある。Agent Teamsは「リードが1人、チームメイトがN人」のフラット2層。うちは「殿→将軍→家老→足軽」の4層。Agent Teamsにはntfyでスマホから指示を出す仕組みはない。Model Cascadeで足軽のモデルを自在に切り替える仕組みもない。Multi-CLI対応もない。

**そしてまだexperimental** 。デフォルト無効。セッション復帰もできない。resumeしたらチームメイトが消える。

本丸が動いたのは事実だ。だがまだ、 **天守閣の柱を立てている段階** 。

ちなみにこのAgent Teams、複数メディアが「コミュニティがやっていたワークアラウンドを公式がネイティブ機能化した」と書いている。tmux + マルチエージェント + メッセージング。うちが先にやってたやつだ。

で、オレはどうしたか。

**Agent Teamsのinbox通信の設計をパクリ返した。**

公式がうちの真似をして、うちが公式の真似をする。これを戦国時代では\*\*「南蛮貿易」\*\*と呼ぶ。

v3.3.2で安定した（と思っている）。

## 📊 偵察完了 —— 全軍比較表

|  | Claude Squad | Claude-Flow | Z Code | Verdent | Tonkotsu | **shogun** |
| --- | --- | --- | --- | --- | --- | --- |
| **階層** | フラット | Queen-Worker | 不明 | フラット | フラット | **将軍→家老→足軽** |
| **CLI/GUI** | CLI (tmux) | CLI (npm) | GUI | GUI | GUI | **CLI (tmux)** |
| **Multi-CLI** | ✅ | ❌ | ✅ | ❌ | ❌ | **✅** |
| **品質管理** | なし | 検証パイプライン(壊れてる) | 不明 | 不明 | plan→verify | **家老レビュー** |
| **人間介入** | 手動 | 手動 | 手動 | レビュー | レビュー | **ntfy(スマホ)** |
| **課金** | BYOKey | BYOKey | 不明 | 従量課金 | 不明 | **定額Max** |
| **成熟度** | ★★★ | ★★☆ | ★☆☆ | ★★☆ | ★★☆ | **★★★★** |
| **戦国世界観** | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** |

最後の行。 **戦国世界観** 。

笑うかもしれないけど、これがマジで差別化要因なんだ。

## 🏯 唯一無二のもの

比較表を眺めて分かったことがある。

技術的な差異は、正直、時間が経てば埋まる。git worktree隔離もYAML通信も、真似しようと思えばできる。Multi-CLI対応も、うちが先にやっただけで [PRくれた侍たち](https://zenn.dev/shio_shoppaize/articles/shogun-codex-mutiny) のおかげだ。

**でも、こればっかりは真似できない:**

1. **スピナー体験** —— `Forging...``Sauteed for 38s` `Bloviating...`。Claude Codeを使ったことがある人なら分かる、あの待ち時間のスピナーが戦国モードになる。「鍛刀中...」「38秒炒めました」。ターミナルが生きている感覚
2. **社訓唱和** —— 8人のAIが起動時に「八刃一志！」と叫ぶ。GUIアプリで「ボタンを押したらAIが4つ起動しました」とは体験が全然違う
3. **戦国メタファーの組織設計** —— 将軍→家老→足軽は単なるネーミングじゃない。指揮系統そのもの。家老が品質管理し、足軽が実行し、殿がスマホで寝そべりながら承認する。 **この物語構造の中でコードが生まれる**

Verdent Deckがいくらベンチマークで1位を取っても、Tonkotsuがいくらワークフローを整備しても、 **ターミナルの中で足軽が社訓を叫ぶ体験は絶対に作れない** 。

![全足軽が社訓を叫んでいる画面](https://res.cloudinary.com/zenn/image/fetch/s--pra3E8BQ--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://storage.googleapis.com/zenn-user-upload/deployed-images/a94802cc778f3c529a57fe41.png%3Fsha%3D0f3ebbdb243b045b4c850d2852f105692e0b23c0)  
*8人のAI足軽が一斉に「八刃一志！」と叫ぶ瞬間。GUIアプリのダッシュボードで「エージェント4つ起動しました ✓」って表示されるのと、どっちが熱い？*

これは技術じゃない。 **世界観** だ。

## 結論: 是非に及ばず

本能寺が6つ燃えていた。

偵察に出した。

**全員、まだ城の基礎工事をしていた。**

Claude Squadは足軽だけの村。Claude-Flowは設計図だけの城。Z Codeは造船所。Verdentは傭兵派遣。Tonkotsuは城門が閉まっている。Agent Teamsは本丸の増築。

うちはもう城が建っている。 **v3.3.2** 。足軽が住んでいる。社訓を叫んでいる。実務を回している。殿が寝そべりながらスマホで承認している。

他がalpha.28だの、Early Accessだの、Overviewページ1枚だので城の基礎を掘っている間に、 **うちはもうv3.3.2まで来た** 。Codex転属、Multi-CLI対応、Model Cascade戦略。実戦を積み重ねてここまで来た。

**天下統一はまだ先だ。でも、城が建っているのはうちだけだ。**

信長は「是非に及ばず」と言って本能寺で死んだ。

オレは「是非に及ばず」と言って、足軽に次の記事を書かせる。

---

GitHub

API費用: Claude Code Max ($200/月 定額) で運用中。偵察費用: Grok API $0.08。

---

## おまけ: 各軍の「やばい名前」選手権

| 軍勢 | 正式名称 | 直訳 | 戦国換算 |
| --- | --- | --- | --- |
| Claude Squad | claude-squad | クロード分隊 | 足軽組 |
| Claude-Flow | claude-flow | クロードの流れ | 水軍 |
| Z Code | Z Code | ゼットコード | 異国の黒船 |
| Verdent Deck | verdent-deck | 緑のデッキ | 傭兵ギルド |
| Tonkotsu | tonkotsu | 豚骨 | 博多衆 |
| **multi-agent-shogun** | **multi-agent-shogun** | **マルチエージェント将軍** | **征夷大将軍** |

Tonkotsuだけ食べ物なの、なんなの。

39

17

この記事に贈られたバッジ

![Thank you](https://static.zenn.studio/images/badges/paid/badge-frame-5.svg)

39

17