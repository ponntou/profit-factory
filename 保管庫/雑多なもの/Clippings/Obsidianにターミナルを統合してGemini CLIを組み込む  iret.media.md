---
title: "Obsidianにターミナルを統合してGemini CLIを組み込む | iret.media"
source: "https://iret.media/160129"
author:
  - "[[中地 悠斗]]"
published: 2025-07-22
created: 2026-03-08
description: "Obsidianを使い始めましたが、プラグインなどを含めて機能も多く、カスタマイズ性もかなりあると言うことで、まだまだ使い方に慣れておりません。またフレームワークであるZettelkastenなどもち..."
tags:
  - "clippings"
---
## Obsidianにターミナルを統合してGemini CLIを組み込む

[エンジニアブログ](https://iret.media/tech) 2025.07.22
- [x](https://twitter.com/intent/tweet?url=https%3A%2F%2Firet.media%2F160129&text=Obsidian%E3%81%AB%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%82%92%E7%B5%B1%E5%90%88%E3%81%97%E3%81%A6Gemini%20CLI%E3%82%92%E7%B5%84%E3%81%BF%E8%BE%BC%E3%82%80)
- [facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Firet.media%2F160129)
- [はてなブックマーク](http://b.hatena.ne.jp/entry/https%3A%2F%2Firet.media%2F160129)
- [pocket](http://getpocket.com/edit?url=https%3A%2F%2Firet.media%2F160129)

![](https://iret.media/wp-content/uploads/2025/07/the-new-obsidian-icon-v0-fuyAdF_1WhOuYm-zaQugUpVB5ZQr2JZw3LH-yGUsKpE.webp)

Obsidianを使い始めましたが、プラグインなどを含めて機能も多く、カスタマイズ性もかなりあると言うことで、まだまだ使い方に慣れておりません。

またフレームワークであるZettelkastenなどもちゃんとよくわからない。。。

と思ってましたが、これこそAIの出番です。

メモの書き方や整理も全てAIにしてもらって人間はただ思考を垂れ流すだけになれればいいなと言うことで、今回はweb searchも持っているGemini CLIを統合します。（Claude Codeでも同じですが）

ObsidianとCursorの組み合わせも流行ってましたが、まぁObsidianのかっこいいUI使いたいしObsidianの画面からAIが呼べるならそれに越したことはないだろうという考えでCursorは択から外しました。

## Terminalプラグインをインストール

Gemini CLIを統合できたらなぁと言う考えで検索したらありました。

こいつをインストールして有効化してください。

![](https://iret.media/if(this.srcset==this.src)%7Bthis.src=this.srcset='/wp-content/themes/clp_media/img/common/offline.png';this.onerror=false;%7Delse%7Bthis.srcset=this.src%7D)

左のメニューバーから「open terminal」が押せるようになっているので、そちらを押下して下記のモーダルにて「darwinIntegratedDefault」を選択します。

![](https://iret.media/if(this.srcset==this.src)%7Bthis.src=this.srcset='/wp-content/themes/clp_media/img/common/offline.png';this.onerror=false;%7Delse%7Bthis.srcset=this.src%7D)

するとこのように普段のzshが開きました。

![](https://iret.media/if(this.srcset==this.src)%7Bthis.src=this.srcset='/wp-content/themes/clp_media/img/common/offline.png';this.onerror=false;%7Delse%7Bthis.srcset=this.src%7D)

## パスの追加

あとはGemini CLI入れておわりかと思ったら、統合したはずなのにHomebrewが読み込まれておらずnpmなどが通らないんですよね。

Homebrewのパスを追加します。

`export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"`

次に.zshrcに設定追加します。

`echo 'export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:$PATH"' >> ~/.zshrc`

最後に設定反映して完了です。

`source ~/.zshrc`

## Gemini CLI統合

ダウンロードはお好きな方法でしていただくか、すでに自身のPCでインストールされている方は統合しているので追加でのインストールは不要だったりします。

私はClaude Codeはそのまますぐに呼び出せました。

こんな感じで無事にObsidianのUIからGeminiも呼び出せました。

業務中に垂れ流したメモなど、業務後などにタグなど含めて整理してもらうのに重宝していて結構いい感じです。

フォルダ構成やフレームワークについてもアドバイスもらえるので、助かります！

![](https://iret.media/if(this.srcset==this.src)%7Bthis.src=this.srcset='/wp-content/themes/clp_media/img/common/offline.png';this.onerror=false;%7Delse%7Bthis.srcset=this.src%7D)

[エンジニアブログ](https://iret.media/tech)

この記事を書いた人

中地 悠斗 DX開発事業部所属。

- [x](https://twitter.com/intent/tweet?url=https%3A%2F%2Firet.media%2F160129&text=Obsidian%E3%81%AB%E3%82%BF%E3%83%BC%E3%83%9F%E3%83%8A%E3%83%AB%E3%82%92%E7%B5%B1%E5%90%88%E3%81%97%E3%81%A6Gemini%20CLI%E3%82%92%E7%B5%84%E3%81%BF%E8%BE%BC%E3%82%80)
- [facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Firet.media%2F160129)
- [はてなブックマーク](http://b.hatena.ne.jp/entry/https%3A%2F%2Firet.media%2F160129)
- [pocket](http://getpocket.com/edit?url=https%3A%2F%2Firet.media%2F160129)