---
title: "AIに「ユーザーペルソナ」を与えるだけで、UIデザインはここまで化ける"
source: "https://qiita.com/natume_nat/items/c3d904ff5f898ad243f3"
author:
  - "[[natume_nat]]"
published: 2026-02-18
created: 2026-03-09
description: "はじめに AIにUIデザインや要件定義を頼むとき、「機能」ばかり指示していませんか？ 実は、誰が使うか（ペルソナ）を1行足すだけで、出力されるデザインの解像度が劇的に変わります。 同じ「タスク管理アプリ」という指示で、ペルソナの有無によってどれだけ差が出るか実験しました。..."
tags:
  - "clippings"
---
![](https://relay-dsp.ad-m.asia/dmp/sync/bizmatrix?pid=c3ed207b574cf11376&d=x18o8hduaj&uid=)

## Qiita Careers powered by IndeedPR

求人サイト「Qiita Careers powered by Indeed」では、エンジニアのあなたにマッチした求人が見つかります。

[求人を探す](https://careers.qiita.com/)

## はじめに

AIにUIデザインや要件定義を頼むとき、「機能」ばかり指示していませんか？  
実は、誰が使うか（ペルソナ）を1行足すだけで、出力されるデザインの解像度が劇的に変わります。  
同じ「タスク管理アプリ」という指示で、ペルソナの有無によってどれだけ差が出るか実験しました。

## 検証： 3つのアウトプット比較

### 1\. ペルソナなし

**▼ 実際に入力したプロンプト**  
タスク管理アプリを作ってください

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/95edc7a3-71b5-44a7-a376-795ac2ba53f2.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2F95edc7a3-71b5-44a7-a376-795ac2ba53f2.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c3611323d1beb2b3092db63f588a0cce)  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/79206519-b48c-46fe-9f05-6ad85e2a4cd7.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2F79206519-b48c-46fe-9f05-6ad85e2a4cd7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5045fc5bce3e1bf32de4947bdf472b06)

**結果：ザ・無難**

- 誰でも使えるが、誰の心にも刺さらない「田中太郎」仕様
- よくあるBootstrap的な青基調のデザイン
- 機能は揃っているが、面白みや特徴はない

### 2\. ペルソナあり：アオイ

**▼ 実際に入力したプロンプト**  
以下のペルソナに向けた「タスク管理アプリ」を作ってください

- **名前:** アオイ（24歳・女性・カフェ店員/イラストレーター志望）
- **性格:** 感覚派。細かい文字や複雑な設定を見ると、やる気がなくなる。
- **現状の悩み:** 「やらなきゃいけないこと」に追われて気が滅入っている。手帳は最初だけ凝るが、すぐに続かなくなる。
- **アプリを使う目的:** 効率化よりも、「今日も私、意外とがんばったじゃん」という自己肯定感を得たい。精神的な負担を減らしたい。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/4d2a9360-cb62-4f74-948d-adb2ab444b59.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2F4d2a9360-cb62-4f74-948d-adb2ab444b59.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=87a9a785f6506ceb8bd20dc588b36b2b)  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/bee2b955-b8d4-4394-a95e-e994f0f574af.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2Fbee2b955-b8d4-4394-a95e-e994f0f574af.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3df2c43ec95d1016154e5f7cad257e33)

**結果：AIが「癒やし」を提案**

- **世界観:** 「タスク」という言葉を排除し、「やることバブル」「今のキブン」といった柔らかい表現に変換
- **機能:** タスクを消化すると「植物が育つ」というゲーミフィケーション要素をAIが独自に追加
- **デザイン:** 曲線とパステルカラー。「開きたくなる画面」への転換

### 3\. ペルソナあり： ケンジ

**▼ 実際に入力したプロンプト**  
以下のペルソナに向けた「タスク管理アプリ」を作ってください

- **名前:** ケンジ（36歳・男性・IT企業のプロジェクトマネージャー）
- **性格:** 超合理的。1秒の無駄も許せない。
- **現状の悩み:** 同時に10以上のプロジェクトが動いており、タスクの抜け漏れが致命的なミスにつながる状況。
- **アプリを使う目的:** 脳のリソースを使わずに、機械的にタスクを処理したい。情報の全体像を一瞬で把握したい。

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/f729a7e0-32d3-47e7-afa4-c953692751ba.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2Ff729a7e0-32d3-47e7-afa4-c953692751ba.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c926c9b15622b6f780346e51becdb7e1)  
[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/488226/f937a079-0c5f-431a-af6e-e0feac9e6c2a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F488226%2Ff937a079-0c5f-431a-af6e-e0feac9e6c2a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d9b03320dcfaeed4199ba0c33b20e6de)

**結果：AIが「コックピット」を提案**

- **世界観:** 「健全性」「阻害要因」といった専門的な管理用語を使用
- **機能:** 「クリティカルパス」やコマンド検索など、プロ向け機能をAIが独自に追加
- **デザイン:** 長時間作業に耐えるダークモード＆高密度グリッド

## なぜここまで変わるのか？（考察）

おそらく、LLM（大規模言語モデル）の特性として、 **ペルソナに含まれるキーワードが、特定のデザインパターンを強く「連想」させた** と考えられます。

|  | アオイ（感覚派） | ケンジ（合理派） |
| --- | --- | --- |
| **入力テキスト** | 「細かい文字を見るとやる気がなくなる」   「自己肯定感を得たい」 | 「1秒の無駄も許せない」   「全体像を一瞬で把握したい」 |
| **学習データ上の   「連想」** | 女性らしいSNS・ゲーミフィケーションの文脈に近い   → 「柔らかいUI」「報酬体験」 | 開発ツール・業務管理の文脈に近い   → 「ダッシュボード」「ダークモード」 |

こちらから「植物を表示して」や「ガントチャートを入れて」とは一言も指示していません。  
しかし、ペルソナの詳細なテキストが強力な文脈となり、そこから確率的に高い精度で「そのユーザー層に適した機能やデザイン」が引っ張り出された結果と言えそうです。

## まとめ： ペルソナ定義は最強の時短

「ボタンは右上で…色は黒で…」のように細かく指示するよりも、「こういうユーザーのために作って」とユーザー像から伝えた方が、圧倒的に早く、高品質なアウトプットにつながります。  
AIを使って要件定義やプロトタイピングをする際は、機能リストを渡すだけでなく「 **どんな性格の人が、何の目的で使うのか？** 」を整理して渡してみてください。  
きっと、これだけで出力の質がぐっと上がりますよ！

[3](https://qiita.com/natume_nat/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fnatume_nat%2Fitems%2Fc3d904ff5f898ad243f3&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fnatume_nat%2Fitems%2Fc3d904ff5f898ad243f3&realm=qiita)