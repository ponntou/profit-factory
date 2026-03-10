---
title: "AntigravityとUnity MCPを使ってバイブコーディングをしてみた"
source: "https://zenn.dev/91works/articles/1c2e59799a1b3e"
author:
  - "[[Zenn]]"
published: 2026-02-02
created: 2026-03-09
description:
tags:
  - "clippings"
---
2

2[tech](https://zenn.dev/tech-or-idea)

## 概要

MCPとやらがどんなものかを確認したかった＋最近話題のAntigravityを触ってみたかったので  
普段使ってるUnityと組み合わせてどういった事ができるかを勉強がてら使ってみる

## 環境

- Unity 6000.0.63f1
- MCP for Unity 8.7.1
- Antigravity 1.13.3

## 導入

- Antigravityのインストール
	- [ココ](https://antigravity.google/) からダウンロード
- Unityのインストール
	- [ココ](https://unity.com/ja/releases/editor/archive) からダウンロード
- MCP for Unityのインストール
	- Unity内のPackageManagerからインストール
- MCPの繋ぎこみ
	- 大体 [こちらの記事](https://zenn.dev/ail/scraps/c5ed8d5f67a160) に書いてある通りなのでこちらを参考に繋げる

## バイブコーディング

唐突にテトリスがしたくなったのでAntigravity上のプロンプトでお願いする  
使うモデルは `Gemini 3 Pro(High)` を選択

```
Unity上でテトリスを作ってください
```

ガリガリ作り始めてくれた  
![](https://storage.googleapis.com/zenn-user-upload/e754eb2c5f2f-20260106.png)

完了したら説明と、ご丁寧に操作方法まで用意してくれてて軽く感動  
![](https://storage.googleapis.com/zenn-user-upload/6bf757df8cdc-20260106.png)

---

いざ起動！

![](https://storage.googleapis.com/zenn-user-upload/fb38ec295d88-20260106.gif)

(どこいくねーん)

直してほしいので、再度プロンプトにお願いする

```
画面外にミノが行ってしまうので、画面内に収まるように直してください
```

![](https://storage.googleapis.com/zenn-user-upload/6d0af8643c63-20260106.png)

収まってた  
![](https://storage.googleapis.com/zenn-user-upload/e0635ab96060-20260106.gif)

---

テトリスは色が付いてこそなので、ブロック線も合わせてプロンプトにお願いする

```
各ミノに色とブロック線を付けてください
```

![](https://storage.googleapis.com/zenn-user-upload/2622ccdb28eb-20260106.png)

良さそう  
![](https://storage.googleapis.com/zenn-user-upload/91e0daac1f5b-20260106.png)

---

謎の空間でテトリスをしてるので、ミノを置く周りに視覚的に壁を用意してもらう

```
謎の空間にミノを置いている状態なので、ミノを置く所に視覚的にわかる壁を用意してください
```

![](https://storage.googleapis.com/zenn-user-upload/e49415cd432f-20260106.png)

良い感じ  
![](https://storage.googleapis.com/zenn-user-upload/54ba19b481b1-20260106.png)

---

なんのために消してるかわからなかったので、スコア機能を実装してもらう

```
スコア機能を実装してください、またスコアボードは画面下に配置してください
```

![](https://storage.googleapis.com/zenn-user-upload/770ad83547e1-20260106.png)

ここで問題発生、プレイしてもミノが落ちてこなくなったので文句を言う

```
ミノが落ちてこなくなりました、直してください
```

![](https://storage.googleapis.com/zenn-user-upload/8dbf8d285cd3-20260106.png)

![](https://storage.googleapis.com/zenn-user-upload/52dab51d2ab4-20260106.png)

落ちてくるようになったが、前述のスコア表示が左下に切れて表示されていた

---

修正をお願いする

```
スコア表示が左下に切れて表示されているので、画面内に収まるように修正してください
```

![](https://storage.googleapis.com/zenn-user-upload/7a70231d6aee-20260106.png)  
左下にちょこんと表示されるようになった、見えん  
![](https://storage.googleapis.com/zenn-user-upload/be5b4d02c61f-20260106.png)

---

更にここでまた問題が発生、またミノが落ちなくなってたので直してもらう

```
またミノが落ちなくなりました、修正してください
```

```
やはりミノが落ちてきません、修正してください
```

```
ゲーム開始時にミノが落ちてきません、修正してください
```

```
やはりゲーム開始時にミノが落ちてきません、不具合を探して修正してください
```

何回かお願いしたが、結局降ってこず・・・

---

## モデルチェンジ

AIが直してくれないなら自分でなんとかするしかないので、AIが作ってくれたコードを覗き見しつつ気になる所を聞いていたらリミットが来る  
![](https://storage.googleapis.com/zenn-user-upload/f337575346f8-20260106.png)

しょうがないので、モデルを `Claude sonnet 4.5` にしてもっかい修正をお願いしてみる  
![](https://storage.googleapis.com/zenn-user-upload/e6f94d66d95b-20260106.png)

一発で直った＋スコア表示も完璧だった(最初からこのモデルで良かったじゃん・・・)  
![](https://storage.googleapis.com/zenn-user-upload/01e328edca44-20260106.png)

## 感想

- Unity MCPを使えば最低限のクオリティのゲームを作るのがすごい時短となりそう
	- ちなみにこのテトリスを作った時間は最初のプロンプトを投げてから２時間ほどで出来た
- ただし、自分で手直しする場合、AIが作ったコードを１から調べていかなきゃいけないので辛い
- AIでどこまでディープな部分を修正していけるかは今後試してみても良さそう
- AntigravityがVSCodeとそっくりだったので使いやすかった

## 備考

- せっかく作ったのでWebに上げた  
	[https://play.unity.com/en/games/be78f3c0-3b5f-4363-8501-4986c6a12671/webgl-builds](https://play.unity.com/en/games/be78f3c0-3b5f-4363-8501-4986c6a12671/webgl-builds)

## 91works AIラボについて

91works AIラボは、エンジニア6名が参加する3ヶ月間のAI学習を目的とした社内プロジェクトです。

詳しくは、こちらの記事をご覧ください👇  
▶ [社内AIラボを3ヶ月やってみた - エンジニア6人の挑戦と成果](https://note.com/91works/n/nd6b13c3fd94d)

2

2

### Discussion

![](https://static.zenn.studio/images/drawing/discussion.png)

ログインするとコメントできます

2

2