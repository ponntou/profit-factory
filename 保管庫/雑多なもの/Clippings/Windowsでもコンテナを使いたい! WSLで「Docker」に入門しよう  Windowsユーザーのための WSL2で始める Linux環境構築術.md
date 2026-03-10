---
title: "Windowsでもコンテナを使いたい! WSLで「Docker」に入門しよう | Windowsユーザーのための WSL2で始める Linux環境構築術"
source: "https://thinkit.co.jp/article/37985"
author:
  - "[[水野 源]]"
published: 2025-03-04
created: 2026-03-09
description: "【Think IT】第9回の今回は、WSLを利用してWindows上でコンテナの実行環境「Docker」を動かす方法について解説します。"
tags:
  - "clippings"
---
## はじめに

今どきのアプリケーション開発において、避けては通れないトレンドとなっているのが「コンテナ」です。そして、その中でも世界で最も利用されているコンテナ実行環境が「Docker」ではないでしょうか。

Dockerは、自身を「アプリケーションを開発、転送、実行するためのプラットフォーム」と位置づけています。Dockerはアプリケーションの実行環境一式をカプセル化し、ポータビリティを持たせる技術です。これにより、環境に左右されず同じ条件でアプリケーションを動かすことができ、効率の良い開発やデリバリーを実現できるというわけです。

[第4回](https://thinkit.co.jp/article/37770) で少し触れた通り、Dockerとユニバーサルパッケージは非常によく似た設計思想を持っています。コンテナと言えば軽量な仮想環境というイメージを持っている方も多いかもしれませんが、Dockerはむしろパッケージシステムに近い存在だと言えるでしょう。

DockerはLinuxカーネルの機能を利用しているため、Linuxでなければ動かすことはできません。そのためWindows上でDockerを使うには仮想マシンを併用するのが定石でしたが、現在ではより高速に動作するWSL(WSL2)が存在するため、これを利用しない手はないでしょう。

今回はWSLを使って、Windows上でDockerを動かす方法を解説します。

## Docker Desktopとは

WindowsやmacOSでDockerを動かそうと思った際、最初に候補に上がるのが [Docker Desktop](https://docs.docker.com/desktop/) ではないでしょうか。Docker DesktopはDocker Engine、クライアントとなるdockerコマンド、GUIフロントエンド等々のDocker実行環境をオールインワンで提供するプロダクトです。その特徴として内部的に仮想マシンを起動し、Dockerを動かしているという点が挙げられます。

Docker Engineを仮想マシンで提供することより、Windows/macOS/Linuxが混在する環境でも同じバージョンのDocker Desktopをインストールすれば開発環境を同一に揃えることができるのです。これは大規模なチームによる開発プロジェクトにおいて、非常に大きなアドバンテージとなります。

従来のWindows版のDocker DesktopはバックエンドとしてHyper-Vの仮想マシンを利用していましたが、WSLがインストールされている環境であれば、代わりにより軽量で高速なWSLを利用できます。

## Docker Desktopのインストールと起動

それでは、実際にDocker Desktopをインストールしてみましょう。なお、まだWSLをインストールしていない場合は、 [第1回](https://thinkit.co.jp/article/37578) を参考に、事前にWSLのインストールを済ませておいてください。

Docker Desktopの [インストールドキュメント](https://docs.docker.com/desktop/setup/install/windows-install/) を参考にWindows用のインストーラーをダウンロードして実行してください。以下の構成オプション画面が表示されます。バックエンドにWSL2を利用するので「Use WSL2 instead of Hyper-V」にチェックが入っていることを確認してください(現在ではWSLの利用が推奨されているため、デフォルトでチェックが入っているはずです)。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_01.png.avif?itok=nZFnogKC)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_01.png)

Docker Desktopのインストール画面。「WSLの利用」にチェックを入れる

なお、Hyper-Vが使えない環境(具体的にはWindows 11 Home)ではバックエンドを選択できないため、この選択肢は表示されず自動的にWSLが使用されます。

そのまま画面の指示に従ってインストールを進め、完了するまで待ちましょう。以下の画面が表示されたら「Close and restart」をクリックします。Windowsが即座に再起動されるので気をつけてください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_02.png.avif?itok=Pfmbz_Zu)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_02.png)

インストールが完了したらWindowsを再起動される

再起動が完了したら、Docker Desktopを起動しましょう。初回起動時は以下のダイアログが表示され、Docker Subscription Service Agreementへの同意を促されます。内容を確認した後、問題がなければ「Accept」をクリックします。Docker Desktopは一定以上の規模の企業では有償サブスクリプションプランの契約が必要となります。業務で利用する場合はくれぐれも気をつけてください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_03.png.avif?itok=2mTIXykX)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_03.png)

Docker Subscription Service Agreementへの同意

この段階でWSL内に「docker-desktop」という名前のディストリビューションがインストールされており、ここでDockerが起動しています。PowerShellを起動して以下のコマンドを実行すると、その存在を確認できます。

```lua
$ wsl --list
```

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_04.png.avif?itok=JwnjsFqX)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_04.png)

docker-desktopディストリビューションがUbuntuなどと同列にインストールされていることが分かる

後述しますが、CLIで実行するdockerコマンドもWindows上のPowerShellから直接実行可能です。そのため、本連載で使ってきたUbuntuなどとは異なり、ユーザーが直接このディストリビューション内にログインして操作することはありません。あくまで、Docker DesktopのバックエンドとしてDocker Engineを動かすためのものとなります。通常の利用の範疇においては、その存在を意識する必要もないでしょう。

## Dockerコンテナを動かす

ここまでの操作だけで、WSLをバックエンドとしてDockerコンテナを動かせます。試しにnginx Webサーバーをコンテナで動かしてみましょう。

Docker Desktopを起動したら、ウィンドウ上部にある検索ボックスに「nginx」と入力してください。複数のイメージがヒットしますが(おそらく)、一番上に表示されているであろう公式のイメージを選択します。「Run」をクリックしてください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_05.png.avif?itok=GE6mBKnm)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_05.png)

nginxのイメージを取得して実行する

コンテナを起動しようとすると、以下のウィンドウが表示されます。nginxのコンテナは、ホストが待ち受けるポート番号やコンテナ内にマウントするボリュームを起動時に指定できます。これはその設定を行うためのウィンドウです。ここではコンテナに「nginx」という名前を付け、ホストのポートに「8080」を指定しました。設定値を入力したら「Run」をクリックしてください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_06.png.avif?itok=95KtPC5f)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_06.png)

起動前にコンテナの設定を行う

これだけでコンテナが起動します。WindowsでWebブラウザーを起動して「http://localhost:8080」 <sup><strong>*</strong> 1</sup> にアクセスしてみましょう。nginxのサンプルページが表示されたら成功です。

**\*** 1: コンテナの起動時に異なるポートを指定した場合は、ポート番号を適宜変更してください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_07.png.avif?itok=zf9x6xem)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_07.png)

Windowsからコンテナ内で起動しているnginxにアクセスしてみた

たったこれだけで、Windows上でも簡単にDockerを動かせることが理解いただけたのではないでしょうか。Docker Desktop自体のより詳しい使い方は [ドキュメント](https://docs.docker.com/desktop/use-desktop/) を参照してください。

## コマンドラインからDockerを使う

Docker Desktopのメリットの1つはGUIから操作できる点ですが、「普段からコマンドラインを使っているためCLIでも操作したい」「自動化したいのでマウス操作は困る」といった方もいるでしょう。Docker DesktopにはCLIツールであるdockerコマンドも同梱されているため、コマンドラインからの操作も可能です。

PowerShellを起動して、以下のコマンドを実行してみましょう。先ほどpullしたnginxのコンテナイメージや、(コンテナを終了していなければ)起動中のnginxのコンテナが表示されます。

```ruby
$ docker images

$ docker ps
```

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_08.png.avif?itok=J2AruOIo)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_08.png)

WindowsのPowerShellからdockerコマンドを実行してWSL内で実行されているDocker Engineと通信できる

少し内部の仕組みを見てみましょう。以下のコマンドを実行してください。

```ruby
$ docker context inspect
```

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_09.png.avif?itok=9VUHsWl8)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_09.png)

Docker Desktopをインストールした後のコンテキストの状態

dockerコマンドは、Docker Engineとの通信に必要になるエンドポイント情報やセキュリティ情報などを「コンテキスト」という単位で管理しています。dockerコマンドは使用するコンテキストを切り替えることで複数のDocker Engineと通信できるのです。

Docker Desktopをインストールすると「desktop-linux」という名前のコンテキストが作成され、デフォルトでこれを利用するよう設定されていることが分かります。また、そのエンドポイントとしてWindowsの名前つきパイプである「\\\\.\\pipe\\dockerDesktopLinuxEngine」が指定されています。この名前つきパイプを経由して、WSL内のDocker Engineと通信を行っているというわけです。

## WSL内のLinux空間からDocker Desktopを使う

コマンドラインからもDockerを使えることは先に述べた通りですが、普段からLinuxサーバーに慣れている方からすると「PowerShellはちょっと不慣れで…」「やっぱりコマンドはLinuxのBashから操作したい」という方も多いのではないでしょうか(筆者もそうです)。せっかくWSLディストリビューションとしてUbuntuがインストールされているのですから、UbuntuのシェルからDocker Desktopを利用できたら便利ですよね。実はできるのです。

Docker Desktopのウィンドウを開いたら、右上にある歯車のアイコンをクリックして設定を開きます。左ペインから「Resources」→「WSL integration」を選択すると以下の画面が表示されるので、「Enable integration with my default WSL distro」にチェックを入れてください。これでデフォルトのWSLディストリビューション(本連載の通りにインストールしているのであればUbuntu 24.04)において、Docker Desktopとの連携設定が行われます。

もし複数のディストリビューションをインストールしており、個別に連携設定を行いたい場合は「Enable integration with additional distros」を個別にオンにしてください。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_10.png.avif?itok=AIhHvfsu)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_10.png)

WSLディストリビューションにDocker Desktop連携の設定を行う

「Apply & restart」をクリックして設定を適用したら、連携を設定したWSLのLinuxディストリビューションを起動してください。インストール作業を行っていないにもかかわらず、dockerコマンドが使えるようになっていることに気づくでしょう。

/usr/bin/dockerコマンドの実体を調べてみると、/mnt/wsl以下にマウントされたファイルへのシンボリックリンクとなっていることが分かります。このファイルの実体はWindows上にある「C:\\Program Files\\Docker\\Docker\\resources\\wsl\\docker-wsl-cli.iso」というISOイメージ内に含まれています。Windows上にインストールされたISOイメージをループバックマウントすることで、WSLのLinux内から利用可能にしているというわけです。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_11.png.avif?itok=uEr5ttFH)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_11.png)

/usr/bin/dockerコマンドはシンボリックリンク。その実体はWindows側にある

また、Linux内からdocker contextを確認するとエンドポイントが「/var/run/docker.sock」というUnixドメインソケットに向いていることが分かりますが、Docker Desktopがこのソケットをプロキシしているため、docker-desktopディストリビューションのDocker Engineと通信できるようになっています。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_12.png.avif?itok=z5ASr-2P)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_12.png)

WSLのUbuntu内からdockerコマンドを実行した例。先ほどWindows上でpullしたイメージや実行中のコンテナが表示される。つまり同一のDocker Engineと通信できていることが分かる

Docker DesktopのWSL連携を使うことで、クライアント環境としては好みのディストリビューションを使いつつ、Windows/WSL間で共通のDocker Engineを利用できるのです。

## Docker Desktopを使わない方法

このように至れり尽くせりなDocker Desktopですが、企業での利用となると、そのライセンスが問題となることもあります。大規模な企業の業務では無償利用ができないため、現場レベルで気軽に試すといったことができません。

勘違いされる方も多いのですが、こうしたライセンスが課されているのは「Docker Desktop」です。コンテナの実行に必要なDocker Engine自体はApache License 2.0で公開されているオープンソースソフトウェアのため自由に利用できます。つまり、Docker Desktopを使わずにDocker Engineをインストールすれば良いということになります。そしてUbuntuにはDockerのパッケージが用意されており、WSLの中でも動かすことができます。

Ubuntuのシェルを起動したら、以下のコマンドを実行してください。なお、Ubuntu内に直接Dockerをインストールする際は意図しないトラブルを避けるため、Docker DesktopのWSL連携は無効にしておきましょう。あるいはDocker Desktop自体をアンインストールしてしまっても良いでしょう。

```shell
$ sudo apt install -U -y docker.io
```

これだけでDockerが動き出します。前述と同様に、nginxのコンテナを動かすには以下のようにコマンドを実行してください。なおUbuntuのパッケージからDockerをインストールした場合、dockerコマンドの実行にはroot権限(sudoコマンド)が必要になります。

```shell
$ sudo docker run -p 8080:80 -d nginx
```

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_13.png.avif?itok=wsQUbJ4M)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_13.png)

Ubuntu内にインストールしたDockerを使ってコンテナを起動する

先ほどと同様に、WindowsのWebブラウザーから「http://localhost:8080」にアクセスしてみましょう。WSLでは自分(Windows)宛ての通信をWSLが動作している仮想マシンへ転送する仕組みがあるため、これで問題なくコンテナ内と通信できます。

[![](https://thinkit.co.jp/sites/default/files/styles/picturize_mobile_1x/public/article_node/ren_wsl2_vtj_09_14.png.avif?itok=XsiE7vsB)](https://thinkit.co.jp/sites/default/files/article_node/ren_wsl2_vtj_09_14.png)

Ubuntu内で起動したnginxへWindowsからアクセスできる

## おわりに

現在のDocker DesktopはWSLとシームレスに連携できるようになっています。これにより、複雑なインストール手順や設定をせずともWindowsで高速なコンテナ実行環境を整えることができます。また、現在のWSLディストリビューションはsystemdが動作するようになっているため、Docker Desktopを使わず、一般的なLinuxディストリビューションと同様にDockerを動作させることも簡単です。

本連載の開始時にも述べましたが、本番環境はLinuxであるものの「開発用のデスクトップにはWindowsを使いたい」というニーズは多いでしょう。そしてWSLとDockerは、こうしたニーズを満たすために最適だと言えるのではないでしょうか。

次回は、WSL＋Dockerの活用例として、Visual Studio Codeを利用したWindows上でのリモート開発について解説します。

この記事をシェアしてください

- [ポストする](https://twitter.com/intent/tweet?original_referer=&ref_src=&text=Windows%E3%81%A7%E3%82%82%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E4%BD%BF%E3%81%84%E3%81%9F%E3%81%84%21+WSL%E3%81%A7%E3%80%8CDocker%E3%80%8D%E3%81%AB%E5%85%A5%E9%96%80%E3%81%97%E3%82%88%E3%81%86+%7C+Think+IT%EF%BC%88%E3%82%B7%E3%83%B3%E3%82%AF%E3%82%A4%E3%83%83%E3%83%88%EF%BC%89&tw_p=tweetbutton&url=https%3A%2F%2Fthinkit.co.jp%2Farticle%2F37985&lang=ja "この記事をX (Twitter) でポストする")
- [\>ブクマする](http://b.hatena.ne.jp/add?mode=confirm&title=Windows%E3%81%A7%E3%82%82%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E4%BD%BF%E3%81%84%E3%81%9F%E3%81%84%21+WSL%E3%81%A7%E3%80%8CDocker%E3%80%8D%E3%81%AB%E5%85%A5%E9%96%80%E3%81%97%E3%82%88%E3%81%86+%7C+Think+IT%EF%BC%88%E3%82%B7%E3%83%B3%E3%82%AF%E3%82%A4%E3%83%83%E3%83%88%EF%BC%89&url=https%3A%2F%2Fthinkit.co.jp%2Farticle%2F37985 "このエントリーをはてなブックマークに追加")
- [noteで書く](https://note.mu/intent/post?url=https%3A%2F%2Fthinkit.co.jp%2Farticle%2F37985&hashtags=Think%20IT "この記事に関してnoteで書く")

## 人気記事トップ10

[人気記事ランキングをもっと見る](https://thinkit.co.jp/popular)

[【CNDW2025】Grafanaが明かす「オブザーバビリティの哲学」ー最小限の労力で実用的なインサイトを得るには](https://thinkit.co.jp/article/38870) [【CNDW2025】プロダクト急増に備える基盤刷新 ーウェルスナビがECSからEKSへの移行で得た知見とは](https://thinkit.co.jp/article/38848) [【CNDW2025】250環境を5人で運用、構築時間は30分に ーKINTOテクノロジーズが語るインフラ基盤組織の作り方](https://thinkit.co.jp/article/38800) [新たな自動化で熱視線！ AIエージェントの「推論能力」を支える2つのコンポーネントとは？](https://thinkit.co.jp/article/38699) [IoTに生成AIを掛け合わせる「AI-driven IoT」で現場のIoTデータ活用を加速](https://thinkit.co.jp/article/38698) [アイレット、KDDIの属人化問題を生成AIアシスタントの精度を高め解消へ](https://thinkit.co.jp/article/38697) [「Grafana Cloud」の先進的ユーザーであるグリーが10年をかけて到達した「オブザーバービリティ」とは](https://thinkit.co.jp/article/38184) [Grafana Labs CTOのTom Wilkie氏インタビュー。スクラップアンドビルドから産まれた「トラブルシューティングの民主化」とは](https://thinkit.co.jp/article/38129) [API管理をより簡単にする「Kong Konnect」が解決する課題とその主要機能](https://thinkit.co.jp/article/37937) [目指すはプロセス連結によるサイロ化の打破! ガバナンス強化にも寄与する自動化プラットフォームとは](https://thinkit.co.jp/article/37827)