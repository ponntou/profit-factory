---
title: "AIとのバグ修正協同作業ではまず最初に全体図を作ってもらうべき！Unity+Antigravity(アンチグラビティ)｜ギガビット＠ゲームつくるひと"
source: "https://note.com/gigabit_million/n/n5655e7af8025"
author:
  - "[[ギガビット＠ゲームつくるひと]]"
published: 2025-12-11
created: 2026-03-09
description: "まず・・・   AIエージェントを自分の手足と思って使うと99%失敗します。     AIエージェントを使うというのは、１人のエンジニアを雇って一緒に働くような感覚で使うのが正しいと思います。つまり１人の別人と一緒に働くつもりでコミュニケーションコストを負担しないといけない、ということです。   でも、その作業コストを負担してでもやっぱり１人より２人の方が作業は進むよね、一緒に働くその人は世界中のあらゆるプログラミングの書籍を読破しマスターしてるけど現場経験はゼロ。そんな人と一緒に働く感じです。     以前、Unityでのゲーム開発にGoogleのAIエージェントツールのAntigr"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/235624004/rectangle_large_type_2_256f0fdc5313413bb78ece4c9b7175c7.jpeg?width=1280)

## AIとのバグ修正協同作業ではまず最初に全体図を作ってもらうべき！Unity+Antigravity(アンチグラビティ)

まず・・・  

## AIエージェントを自分の手足と思って使うと99%失敗します。

  

AIエージェントを使うというのは、**１人のエンジニアを雇って一緒に働くような感覚**で使うのが正しいと思います。つまり１人の別人と一緒に働くつもりでコミュニケーションコストを負担しないといけない、ということです。

  
でも、その作業コストを負担してでもやっぱり１人より２人の方が作業は進むよね、一緒に働くその人は世界中のあらゆるプログラミングの書籍を読破しマスターしてるけど現場経験はゼロ。そんな人と一緒に働く感じです。

  

以前、Unityでのゲーム開発にGoogleのAIエージェントツールのAntigravity(アンチグラビティ)を使うと作業効率が爆上がりした、という記事を書きました。基本操作などはこちらの記事をご覧ください。

[](https://note.com/gigabit_million/n/nfbaf1e0c9701)

  
僕は非エンジニアですが、もうすっかりAntigravityは手放せなくなってしまいました。今日は僕のスマホゲーム『カードモンスターあつめ！』に寄せられている**バグ修正をAntigravityと一緒に行っていく記事**です。  

  

さっそくAntigravityと協同作業でバグ修正をしていきます。頼むぜ相棒！！  

[![画像](https://assets.st-note.com/img/1765449365-hMB6LvJoUQigaRcC3Izrpw19.png?width=1200)](https://assets.st-note.com/img/1765449365-hMB6LvJoUQigaRcC3Izrpw19.png?width=2000&height=2000&fit=bounds&quality=85)

Antigravityの画面

  
左にUnityのプロジェクトフォルダ、右にAIへの指示プロンプトですが、いきなりバグの内容を言うと、AIはどこに何があるか探すところから始まってしまいますので、まず**「プロジェクトの全体図」を作ってもらいます**。

  

これがとても重要と考えています。AIを１人のエンジニアを雇って働いているとすれば、まずどこにどのファイルがあるか、そのファイルがどんな関係になっているかを渡してあげると親切だと思います。

  

ただ関係図とか準備するのって大変じゃないですか。そこは今回は相手がAIさんであるという大きな強みがあります。その全体図は自分で作る必要はありません。そこからもう**全部AIさんにおまかせで作ってもらいます**。

  

[![画像](https://assets.st-note.com/img/1765449694-htaYOM02wNbzUuI9SfKGJdl3.png?width=1200)](https://assets.st-note.com/img/1765449694-htaYOM02wNbzUuI9SfKGJdl3.png?width=2000&height=2000&fit=bounds&quality=85)

  

プロジェクトを見ればUnityだというのはAIさんは百も承知なのでわざわざ言う必要はないのですが念のため保険でUnityのプロジェクトであることも言っています。スクリプトの関係図と書いてますが、エンジニアの人はこういうのなんで呼ぶんでしょうね。わかる方、ぜひコメントご教授ください。

  

これを指示するとすぐAIさんが作業を始めてくれます。

  

[![画像](https://assets.st-note.com/img/1765449956-ZLNSQJ4jxGc13ndkD8RhBtpu.png)](https://assets.st-note.com/img/1765449956-ZLNSQJ4jxGc13ndkD8RhBtpu.png?width=2000&height=2000&fit=bounds&quality=85)

  
**動き出すまでにわずか6秒**。さすがシゴデキだぜ！

  

[![画像](https://assets.st-note.com/img/1765449894-ndYEfHWyqGNvgXheC2FUxTlo.png?width=1200)](https://assets.st-note.com/img/1765449894-ndYEfHWyqGNvgXheC2FUxTlo.png?width=2000&height=2000&fit=bounds&quality=85)

  

悪かったよ。スクリプトはScriptsフォルダの中にあるのは言ってあげれば良かったね。でもここまでには10秒ぐらいしかかかってないから君なら楽勝だね。

  

[![画像](https://assets.st-note.com/img/1765450046-aZmAEoOxSytRWCuprwbdX5Le.png?width=1200)](https://assets.st-note.com/img/1765450046-aZmAEoOxSytRWCuprwbdX5Le.png?width=2000&height=2000&fit=bounds&quality=85)

  

『証拠は揃った』の一言。頼もしい。

  

[![画像](https://assets.st-note.com/img/1765450116-N58BPd2GAZh4T3aCMfo0K6bu.png?width=1200)](https://assets.st-note.com/img/1765450116-N58BPd2GAZh4T3aCMfo0K6bu.png?width=2000&height=2000&fit=bounds&quality=85)

  
  
**あっという間にできてしました。1分もかかっていません。**  
この記事用に作業過程をスクショ撮ったりしてたのですが撮ってる間に作業終わってました。mdファイルという形式でscript_relationship_diagramといういかにもスクリプトの関係図らしきファイルができましたがどんなものができたかというと、

  

[![画像](https://assets.st-note.com/img/1765450180-fRVDcowjG4m8W2JBFTU7XOgS.png?width=1200)](https://assets.st-note.com/img/1765450180-fRVDcowjG4m8W2JBFTU7XOgS.png?width=2000&height=2000&fit=bounds&quality=85)

  
こんなのとか、

  

[![画像](https://assets.st-note.com/img/1765450295-R7uDm62XVtU4idMev1Qc8AwY.png?width=1200)](https://assets.st-note.com/img/1765450295-R7uDm62XVtU4idMev1Qc8AwY.png?width=2000&height=2000&fit=bounds&quality=85)

  

こんなのとか、いろんな処理におけるスクリプト間の関係、フローを示した多数の図解が作られていました。この図解を示したmdファイルを次の指示に使えるようにフォルダに入れておきます。

  

[![画像](https://assets.st-note.com/img/1765450372-tDVh4LObB3SfyJ2jpePHGl1s.png?width=1200)](https://assets.st-note.com/img/1765450372-tDVh4LObB3SfyJ2jpePHGl1s.png?width=2000&height=2000&fit=bounds&quality=85)

  

すると、フォルダの下にファイルを置いておいてくれます。ファイルの配置や移動、作成や削除もお手の物なのでとっても頼りになりますね。

  

[![画像](https://assets.st-note.com/img/1765450101-ytNK13MocFzOsbfEgTDGQPpA.png)](https://assets.st-note.com/img/1765450101-ytNK13MocFzOsbfEgTDGQPpA.png?width=2000&height=2000&fit=bounds&quality=85)

  

さて、スクリプト関係図ができたところで**本命のバグ修正に入っていきます**。このスクリプト関係図を参照してもらってスムーズにバグの特定にたどりついてもらいます。

  

[![画像](https://assets.st-note.com/img/1765450634-mn8CcIZNFMA6go1ieLWuw5rk.png?width=1200)](https://assets.st-note.com/img/1765450634-mn8CcIZNFMA6go1ieLWuw5rk.png?width=2000&height=2000&fit=bounds&quality=85)

  

関係図ファイルは最初の"@script_relationship_diagram.md"をわざわざ手打ちする必要はなく、ファイルを左から右のAI指示のところにドラッグ＆ドロップすることで入力されます。

そしてプレイヤーさんからバグ報告を頂いた、修正したいバグの現象を入力しています。（プレイヤーさんいつもありがとうございます！！！）僕の場合はいきなりAIエージェントにコーディングまでされちゃうとどこ触られたかわからなくなるので検討までを指示します。これでスタート！

  

[![画像](https://assets.st-note.com/img/1765450838-O6YLWpd9iqeA2mh8lHVNTZ7w.png?width=1200)](https://assets.st-note.com/img/1765450838-O6YLWpd9iqeA2mh8lHVNTZ7w.png?width=2000&height=2000&fit=bounds&quality=85)

[![画像](https://assets.st-note.com/img/1765450857-whHEi7TA8jk2maYLd1lUoRFf.png?width=1200)](https://assets.st-note.com/img/1765450857-whHEi7TA8jk2maYLd1lUoRFf.png?width=2000&height=2000&fit=bounds&quality=85)

  

  
**あっという間にバグを見つけてくれました！わずか30秒ぐらい。  
**30秒なんてもし自分で解析やろうとしたらUnity立ち上げてるだけで終わる時間です。Unityすら立ち上げずにプロジェクトファイル解析でここまで終わる。原因は本当にここだったので修正。

  

この要領で、プロジェクト全体を理解しているAIさんとプレイヤーさんから頂いたバグ報告についてどんどん修正をしてもらいます。

  

複雑なバグとかでなかなか原因特定できないものもありますが、それは自分でしっかり頭を使って解決していくとして、頭を使う必要がなく、どこにどの処理があったかな、と探すのが作業のほとんどを占めるような作業はAIにおまかせした方が速いし正確です。

  

今回はプロジェクト全体の構成図をまず作ってもらって、プロジェクト全体を理解してもらった上でAntigravityと協同でゲーム開発における厄介な作業「バグ修正」をしていく様子を書きました。**構成図をまず参照してもらうことでAIの処理スピードが速くなりますし、AIが使うトークン量も少なく抑えることができます**。

  

構成図に限らず、AIエージェントと共同作業をする上では１人のエンジニアを雇った気持ちで、情報共有のコミュニケーションには気を使って仕事をしてもらった方がうまくいくと思います。

  

このAntigravity…なぜか知りませんが基本**無料**なんですよ。  
一定量を超えると課金を促されますが月1500円でChatGPTの半額ぐらいだし、Google Drive 2TBも、YouTubeプレミアムの割引までついてくる意味わからん安さです。**Google恐るべし**。

  

  
僕たち非エンジニア、ぜひAntigravityと一緒に快適なゲーム制作ライフを送りましょう！！！