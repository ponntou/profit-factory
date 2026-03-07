---
title: "ObsidianをAndroidスマホから無料で使い続ける方法｜おがくずにゃんこ"
source: "https://note.com/mikenerian/n/nad630c73950e"
author:
  - "[[おがくずにゃんこ]]"
published: 2025-07-18
created: 2026-03-08
description: "こんにちは、おがくずにゃんこです。  最近は猫も杓子もObsidianという状況で盛り上がっていますが、個人的にはずっとあることがネックで使っていませんでした。  それは、無料版ではAndroid端末でマルチデバイス同期できないことです。  iOSであればデフォルトでiCloudを選べるのに、なぜGoogle Driveは選べないのでしょうか。Google Pixelを愛用している私にとってこれは不便すぎるぞということで足踏みしていたのですが、この弱点を克服し、さらにはスマホで見ている記事をObsidianに保存する機能も安定的に運用する方法を確立したため、今回ご紹介したいと思います。"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/196807201/rectangle_large_type_2_6882ce7c114ce4fd025861a6ecfa54b8.png?width=1280)

## ObsidianをAndroidスマホから無料で使い続ける方法

[おがくずにゃんこ](https://note.com/mikenerian)

こんにちは、おがくずにゃんこです。

最近は猫も杓子もObsidianという状況で盛り上がっていますが、個人的にはずっとあることがネックで使っていませんでした。

それは、 **無料版ではAndroid端末でマルチデバイス同期できない** ことです。

iOSであればデフォルトでiCloudを選べるのに、なぜGoogle Driveは選べないのでしょうか。Google Pixelを愛用している私にとってこれは不便すぎるぞということで足踏みしていたのですが、この弱点を克服し、さらには **スマホで見ている記事をObsidianに保存する機能** も安定的に運用する方法を確立したため、今回ご紹介したいと思います。

  

## Android端末でクラウドと同期させる方法

Obsidianの使い方は色々な記事で紹介されているので、早速AndroidとGoogle Driveを同期する方法を紹介します。色々なアプリがありますが、以下のアプリが動作も安定していてオススメです。

[**Autosync for Google Drive - Google Play のアプリ** *AndroidとGoogle Driveクラウドストレージ間の自動同期ファイル* *play.google.com*](https://play.google.com/store/apps/details?id=com.ttxapps.drivesync&hl=ja)

  

使い方としては、まずObsidianの初期設定画面から、「Create new vault」を選択します。Obsidianアプリはこの場合、 **あくまでも内部ストレージのフォルダを参照しているため、同期する機能はありません** 。先程のアプリで、内部ストレージとGoogle Driveを定期的に同期させ、マルチデバイス対応を実現するイメージです。

![画像](https://assets.st-note.com/img/1750212928-HwTxz2PeW4dMIX9pYkoqCnUF.png?width=1200)

続いて任意のフォルダを選択し、「このフォルダを使用」を選択します。私の場合は「Documents」配下に「Obsidian」というフォルダを新規作成しています。

![画像](https://assets.st-note.com/img/1750212989-bdk0gitTMjFoVC21Z3PwREWn.png?width=1200)

同様に、Google Driveにも同じ名前のフォルダを作成してください。

続いてAutosyncアプリの設定です。同期するフォルダにて、先程作成した内部ストレージのフォルダと、Google Driveのフォルダを選択します。  

![画像](https://assets.st-note.com/img/1750213300-LfnGMzmecdTO0XRWpkUvY2BI.png?width=1200)

これだけで自動同期してくれます。このアプリは無料版で1つのフォルダを同期できるため、Obsidianのためだけに使うのであれば、無料で十分です。  
同期間隔も設定画面から変更することができます。

![画像](https://assets.st-note.com/img/1750213390-G7dASIXN4gqZtb5ULCskQnP6.png?width=1200)

これで、「Obsidianが参照するAndroidスマホの内部ストレージ」と、「Google Driveの特定のフォルダ」が定期的に同期されるようになりました。後はPC等で使用する場合は、「Google Driveの特定のフォルダ」をObsidianのvaultとして設定すれば、 **マルチデバイス間で同期しているかのように作業することができます** 。

  

## Android端末で特定の記事をクリップする方法

これで最大の問題は解決しましたが、スマホで記事をクリップ（コピー）してObsidianに蓄積させたいがために、そもそもこのような工夫をしていたのでした。

クリッピングに使用するのは、Firefoxの拡張機能である、「Obsidian Web Clipper」です。スマホ版Firefoxから、こちらの拡張機能をインストールしてください。

[**Obsidian Web Clipper – Get this Extension for 🦊 Firefox (en-US)** *Download Obsidian Web Clipper for Firefox. Save and highlight* *addons.mozilla.org*](https://addons.mozilla.org/en-US/firefox/addon/web-clipper-obsidian/)

  

ただし、ほとんどの方はwebサイトを閲覧する際、Google Chromeを使用していると思います。Googleアカウントでブックマークを同期させているため、私も普段はChromeを使用しています。

そこで、 **Google Chrome→Firefox→Obsidianと二段階で共有する** というのが、少し手間ですが最適解です。Googleさん、早くスマホ版拡張機能を解禁してください…

  

やり方は、まずスマホのGoogle Chromeでクリップしたい記事を表示させ、「共有…」でFirefoxを選択します。

![画像](https://assets.st-note.com/img/1750214114-hKj1iP3VL7XasFl5wIJbGA8g.png?width=1200)

すると同じ記事がFirefoxで表示されます。次は「拡張機能」を選択します。

![画像](https://assets.st-note.com/img/1750214281-GLjuABUN6ocsHpTWaYlPCqeQ.png?width=1200)

拡張機能の中に、インストールした「Obsidian Web Clipper」が出てくると思うので、こちらを選択します。

![画像](https://assets.st-note.com/img/1750214346-qKF7sdaC8VRcXzPZwpnm6t1k.png?width=1200)

すると自動的にObsidianのノートが作成されるので、「Obsidianに追加」を選択するとObsidianに追加されます。

![画像](https://assets.st-note.com/img/1750214396-84576kBIJqa2fTHSAREmOte3.png?width=1200)

  

## おわりに

ここで紹介した方法はAndroid端末に特化した方法で、iPhoneであれば何も気にせずもっと快適に使用できると思います。Safariで拡張機能を使用することもできるため、記事のクリップも簡単なはずです。

私のようにAndroid端末にこだわっている方は、紹介した方法を試してみてください。そして、快適なObsidianライフを実現しましょう。

最後まで見ていただいきありがとうございました。それではまた、別の記事でお会いしましょう。

## いいなと思ったら応援しよう！

ObsidianをAndroidスマホから無料で使い続ける方法｜おがくずにゃんこ