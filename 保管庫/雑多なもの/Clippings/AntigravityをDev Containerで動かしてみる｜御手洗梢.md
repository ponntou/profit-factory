---
title: "AntigravityをDev Containerで動かしてみる｜御手洗梢"
source: "https://note.com/witty_roses242/n/n48fd3cddb42d"
author:
  - "[[御手洗梢]]"
published: 2025-12-24
created: 2026-03-08
description: "追記2026/2/7：Antigravityのv1.16.5へのアップデート後にDev Container接続不可の報告が出ています。一旦修正が入るまでアップデートをしないなど、Dev Containerご使用の際はご注意下さい。  皆さんお疲れ様です。Antigravity使っていますか？すごい便利ですよね？ただやっぱり気になるのが安全性。うっかり大事なファイルを消されたりするのは避けたいものです。というわけで今回はどうやらAntigravityには標準で入っているらしいDev Containerで開発してみようと思います。 あ、Windows環境での導入ですので他の環境の人はごめん"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/238427086/rectangle_large_type_2_b035120b015123ab0478330b462d8e84.png?width=1280)

## AntigravityをDev Containerで動かしてみる

[御手洗梢](https://note.com/witty_roses242)

追記2026/2/7：Antigravityのv1.16.5へのアップデート後にDev Container接続不可の報告が出ています。一旦修正が入るまでアップデートをしないなど、Dev Containerご使用の際はご注意下さい。

皆さんお疲れ様です。Antigravity使っていますか？すごい便利ですよね？ただやっぱり気になるのが安全性。うっかり大事なファイルを消されたりするのは避けたいものです。というわけで今回はどうやらAntigravityには標準で入っているらしいDev Containerで開発してみようと思います。  
あ、Windows環境での導入ですので他の環境の人はごめんなさい。

Dev ContainerについてはGoogle NotebookLMでインフォグラフィックを作成したのでこちらをご覧ください。

![画像](https://assets.st-note.com/img/1766499927-bIjeM7DSpNEaXz8Q0w4m3YhB.png?width=1200)

Dev Containerがなぜ安全か

インターネット通信（危ない！）がなぜか二個ありますが「大事なことなので２回言いました」ということにしておきましょうｗ

## 事前準備

### Windows側のセットアップ

というわけでまずは土台作り。以下のインストールと設定をします。  
ちょっとこの辺は今回まとめて導入したわけじゃないので皆さんの環境にあわせて適宜調べてください；

- **WSL2**: Windows上でLinuxを動かす基盤。
- **Docker Desktop**: インストール時に「Use the WSL 2 based engine」にチェック。 Docker Desktopの Settings > Resources > WSL Integration で、使用するディストリビューション（Ubuntuなど）のスイッチを  **ON** にしておきましょう。
![画像](https://assets.st-note.com/img/1766491323-tbIhaPQ6zHELn8fDAloGZsTi.png?width=1200)

なんとかここまでこぎつけてください

Docker Desktopはこのまま起動しておきます。

### Dev Containerの作成と接続

プロジェクトフォルダ（例：E:\\work\\Docker\\test）を作成し、.devcontainer/devcontainer.json を配置します。

![画像](https://assets.st-note.com/img/1766491041-c0iYSzT3C1UDKaF2LWXZp8rn.png?width=1200)

![画像](https://assets.st-note.com/img/1766491059-wXUK5GOhvdmBbyT36Iu29aot.png?width=1200)

ちなみにdevcontainer.jsonの中身は下記のような感じ。

```javascript
{
    "name": "Antigravity Sandbox",
    "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
    "postCreateCommand": "sudo apt-get update && sudo apt-get install -y nodejs npm && pip install playwright && playwright install --with-deps chromium",
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-playwright.playwright",
                "ms-python.python" // Pythonも使うなら入れておくと便利です
            ]
        }
    },
    "remoteUser": "vscode"
}
```

配置が終わったらAntigravityでフォルダを開きます。

![画像](https://assets.st-note.com/img/1766493329-9HGU3gwb12sqIeC5JxalEVkA.png?width=1200)

開いたら左下の青い「><」マークからReopen in Containerを選びます。

![画像](https://assets.st-note.com/img/1766493698-YXkuFMhbvGr4ecwZLamN8zpT.png?width=1200)

![画像](https://assets.st-note.com/img/1766494224-vdgNmoj2qhQ07HrIxW9EDe14.png?width=1200)

するとContainer startedとなりいろいろインストールが入るので結構時間かかります。この状態だとログも見れないみたいなので何なら寝る前にやっといて朝できてるか見る感じでもよさそうです。

### 待ち時間について

…なんか１～２時間くらい放置しても変わらなかったので再起動したらログがでました。まだインストール途中だけどそろそろ終わりそうな雰囲気ですね。ネット環境にもよるんかな？

![画像](https://assets.st-note.com/img/1766497782-X1BeWUG53MJjfxOpmhQPVc0Z.png?width=1200)

そこからさらに５分くらいしたらなんかフォルダの作成者を信頼しますか？のPOP出てきたので「はい、作成者を信頼します」押したらようやく終わった…！

![画像](https://assets.st-note.com/img/1766497962-NbkCdHoRirpUDTvF3IKM1mBz.png?width=1200)

### コンテナ内に入れてるか確認

ターミナル確認してちゃんとvscodeユーザーでworkspace内のtestにはいってるのでコンテナ内に入れたみたいです。

![画像](https://assets.st-note.com/img/1766498705-JVC1MdKhOsAHy9k4iPZpvUo3.png?width=1200)

お疲れ様です。これでとりあえず使う準備が整いました。  
また、今回PlaywrightをインストールしているのはDevContainer環境だとAntigravity標準のブラウザ操作がアクセス拒否されて使えないので代わりに入れています。ブラウザが立ち上がるのは見えませんが「ヘッドレスモード」で動作させて「スクリーンショットを撮って保存して」と指示すれば、コンテナ内のAIが代わりに画面を撮影し、プロジェクトフォルダに画像ファイルとして書き出してくれます。

## 実際に動かしてみる

というわけでやってみましょう。手始めに超絶カッコいいHelloWorldのWEBページをつくってもらい、結果のスクリーンショットを撮ってもらいます。  
せっかくなのでCtrl＋Eでエージェントモードでやってもらいますか。

> 超絶カッコいいHelloWorldのWEBページをhtml,css,javascriptで実装してほしいです。実装後はブラウザを起動しスクリーンショットを格納してください。標準のブラウザ操作は現在の環境では使えませんので、Playwrightを使い、ヘッドレスモードで動作させてスクリーンショットを撮って保存してください。ドキュメントや返答はすべて日本語でお願いいたします。

プロンプト

![画像](https://assets.st-note.com/img/1766499305-yBvwOzXWolMHYqnCcxga7e0f.png?width=1200)

GO！

![画像](https://assets.st-note.com/img/1766501927-JdWORPqu62BVACiIkr1c3jNG.png?width=1200)

が、なんやかんやターミナル使うからEditerに移動

### 再度環境構築フェーズに

ちなみにコンテナ内ということもあって設定を「Always Proceed」にしているので基本ガンガン作業してますが、sudoコマンドとかは止まるっぽいですね。そして、スクリーンショット撮るためになんか足りない分の環境構築しているようです。

![画像](https://assets.st-note.com/img/1766499554-r3cs2lfNa4hqST8VQUydzZeD.png?width=1200)

ここでもめっちゃ時間かかるんご

### 割り込みが可能

今の状況いかがですか？って聞くとちゃんと途中でも返してくれるのが優秀ですね。

![画像](https://assets.st-note.com/img/1766502033-xlIZbza8Dm92F7RM1dPEoCr3.png?width=1200)

### タスク完了！

もうしばらく待つとできたようです！  
スクリーンショットも撮ってくれています。

![画像](https://assets.st-note.com/img/1766501903-eE9HxL6jnytCoPRXdq3Tkubg.png?width=1200)

### 次回以降

うまくいったので次回以降開くときはここで開くか

![画像](https://assets.st-note.com/img/1766502515-0YrQ2HbWhdtjUPMCkmAK5TGs.png?width=1200)

再度同じフォルダを開いて

![画像](https://assets.st-note.com/img/1766503319-dsOWg10TkrnjXJaGBvDbtzw3.png?width=1200)

Reopen in Containerを選択すれば２回目以降はすぐ使えます。  
Colabみたいに毎回インストールしなくていいのはありがたいですね！

![画像](https://assets.st-note.com/img/1766503359-364VONuvfLCZjbiHrXcPdgR7.png?width=1200)

さて、ここで忘れてはいけないのがDocker Desktopの起動です。これが起動してないとコンテナに接続できないのでDev ContainerでAntigravityを使うときはセットでDocker Desktopも起動しておいてください。常時起動でもいいですが、メモリを食うのでその辺は適宜調整ください。

## まとめ

今回はHelloWorldという簡単なタスクでしたが、Dev Containerはいわゆる実験室みたいなものなのでもっといろんなことをやらせてみたいですね。１回作ってしまえば次回からはすぐ使えますし。ブラウザ操作が標準のものが使えないのでブラウザが勝手に動いてるところとかが見れないのはちょっと残念ですが、高度なブラウザ操作のテストとかは自分の監視下で適宜確認しながらローカルのPCでやるとかで使い分けていくのがよさそうですかね。

はい、では今日のところはこの辺しておきましょう。  
皆さん良いAIライフを！

[**Antigravity Browser Control：AIがブラウザを操る未来** *amzn.to*](https://amzn.to/498R0Bh)

[*298 円* (2025年12月24日 01:01時点 詳しくはこちら)](https://amzn.to/498R0Bh)

[

Amazon.co.jpで購入する

](https://amzn.to/498R0Bh)

## いいなと思ったら応援しよう！

AntigravityをDev Containerで動かしてみる｜御手洗梢