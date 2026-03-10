---
title: "【入門】Docker Hubとは？概要と仕組み、基本的な使い方を解説"
source: "https://www.kagoya.jp/howto/cloud/container/dockerhub/?_fsi=las7kSbo"
author:
  - "[[小泉 健太郎]]"
published: 2023-01-20
created: 2026-03-09
description: "Docker Hubは、コンテナ型仮想化サービス「Docker」を使う上で非常に便利なサービスです。Docker Docker Hubは、コンテナ型仮想化サービス「Docker」を使う上で非常に便利なサービスです。Docker Hubを使うことによって、非常に高機能なアプリケーションをDocker上で簡単に実行できます。Dockerについて学ぶ上で、Docker Hubを避けて通ることはできません。この記事では、Docker Hubの概要や仕組み、基本的な使い方について解説します。なお、使い方については、Docker環境を構築済の方を対象としておりますので注意して下さい。"
tags:
  - "clippings"
---
![DockerHubのメリット](https://kagoya.jp/howto/wp-content/uploads/dockerhub.jpg)

DockerHubのメリット

Docker Hubは、コンテナ型仮想化サービス「Docker」を使う上で非常に便利なサービスです。Docker Hubを使うことによって、非常に高機能なアプリケーションをDocker上で簡単に実行できます。Dockerについて学ぶ上で、Docker Hubを避けて通ることはできません。

この記事では、Docker Hubの概要や仕組み、基本的な使い方について解説します。なお、使い方については、Docker環境を構築済の方を対象としておりますので注意して下さい。

Docker環境の構築方法を知りたい方は、以下記事が参考になります。興味があれば、あわせてご覧ください。

![Docker を使って コンテナ仮想化を体験する](https://www.kagoya.jp/howto/wp-content/uploads/202103d_main.jpg)

Docker を使って コンテナ仮想化を体験する

[Docker を使って コンテナ仮想化を体験する](https://www.kagoya.jp/howto/cloud/container/docker-template/)

カゴヤのVPSでは CentOS や Ubuntu、Windows などのOSに加え、必要なパッケージがインストール済みのテンプレートも用意されています。テンプレートを使うことで、面倒で複雑な環境構築作業を大幅に削減することが可能です。利用目的に合わせた環境を簡単に素早く構築できるため、学習や開発・テストなど、やりたいことをすぐに始められます。また日額料金で使い始めることができるので、少しだけ環境…

![Windows＋WSL2でDocker環境を用意しよう](https://www.kagoya.jp/howto/wp-content/uploads/202203b_catch-1.jpg.webp)

Windows＋WSL2でDocker環境を用意しよう

[Windows＋WSL2でDocker環境を用意しよう](https://www.kagoya.jp/howto/cloud/container/wsl2_docker/)

Web開発の現場をはじめとして、Dockerが使われる機会が増えています。手軽に使えるDockerのテスト環境・開発環境を調達したい、と考えている方は多いでしょう。 Windowsでは「WSL2」の登場により、Docker環境を簡単に確保できるようになりました。この記事では、WSL2とは何かといった概要と、Windows＋WSL2でDocker環境を用意する方法について紹介します。 ※KAGOYA…

## Docker Hubとは【Dockerイメージ(コンテナ)の共有サービス】

Docker Hubとは、Docker社がクラウド上で提供しているDockerイメージ（コンテナ）の共有サービスです。Docker Hubには、さまざまなDockerイメージが公開されています。ユーザーはDocker Hubから任意のイメージを取得後、コンテナ化してすぐにいろいろなアプリケーションを利用可能です。

Docker Hubには誰でも利用可能な公開リポジトリの他、非公開のプライベートリポジトリがあります。ユーザーは自分で作成したイメージをそれらリポジトリにアップロードし、他ユーザーと共有することも可能です。

以下にDocker HubのURLを記載します。Docker Hubはお使いのブラウザからもアクセスが可能です。

[https://hub.docker.com/](https://hub.docker.com/)

### Docker Hubの仕組み

Docker Hubにおいて、Dockerイメージは「レジストリ」と呼ばれるデータベースに登録されます。(Docker公式では、Docker Hubのことを「クラウド上のレジストリサービス」と呼んでいます。)より専門的には、Dockerイメージを共有・公開するサービス全体を「レジストリ」と呼ぶのです。

レジストリのなかには、イメージの種類ごとに「リポジトリ」と呼ばれるデータベースが格納されています。各イメージは、「タグ」によって区別することが可能です。

タグには上記イメージのように、バージョン番号がよく使われます。タグにバージョン番号を使うことで、同じアプリケーションのイメージでも、新旧やバージョンが確認しやすくなるわけです。

### Docker Hubの利点

Docker Hubを使うことで、すぐにコンテナ化して使えるDockerイメージを、簡単に取得・共有可能です。Docker Hubにはすぐに使える、様々なアプリケーションのDockerイメージが公開されています。またDockerイメージを取得したり、アップロードしたりするのに料金もかかりません。

### 無料プランと有料プランの違い

Docker Hubは基本的に無料で利用できますが、無料プランで提供される非公開のプライベートリポジトリは1つのみとなります。プライベートリポジトリを2つ以上作成して、組織内でグループごとに使い分けたい場合は有料プランの登録が必要です。（個人で利用する場合など、プライベートリポジトリを複数使う必要がない場合は無料プランで十分です。）

有料プランの具体的な種類や詳細については、以下公式URLをご覧ください。

[https://www.docker.com/pricing/](https://www.docker.com/pricing/)

## Docker Hubの使い方

Docker Hubの使い方は難しくありません。専門知識がない方でも、手軽に使い始めることが可能です。以下、実際の使い方をみていきましょう。

### まずはDocker Hubのアカウントを作成する

Docker Hubを使う場合、まず以下公式サイトへアクセスし専用のアカウントを作成します。

※Dockerイメージを取得するだけであれば、アカウントは必要ありません。  
※Dockerイメージをアップロードする際に必要となります。

[https://hub.docker.com/](https://hub.docker.com/)

１．登録する名前（Username）・メールアドレス・パスワードを入力し、「I agree…」にチェックを入れた後、最後に「Sign UP」をクリックします。

２．名前（Username）、もしくはメールアドレスを入力し「Continue」をクリックします。

３．パスワードを入力し「Continue」をクリックします。

４．プランの選択画面に遷移します。  
ここでは「Continue with free（無料プランを使う）」をクリックしてください。  
※あとでプランを変更することも可能です。

５．メールアドレスの確認をするよう指示されます。  
入力したメールアドレス宛に、Docker Hubから確認用のメールが届いているのでチェックして下さい。

６．メール本文内の「Vertify email adresss」をクリックします。

これでDocker Hubのアカウント作成は完了です。

### Dockerイメージを検索する手順

Dockerイメージは、以下コマンドで検索できます。

```
docker search [オプション] 検索対象
```

たとえばubuntuのイメージを検索したい場合は、以下のように入力します。

```
docker search ubuntu

NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                           Ubuntu is a Debian-based Linux operating sys…   15343     [OK]
……
```

Dockerイメージを検索するコマンドでは、以下オプションを利用できます。

**＜–filter,-f＞**  
指定された条件でフィルター検索を行うオプションです。  
以下の検索条件を指定できます。

**・stars**  
イメージがもつ星数で検索します。たとえば星印が3つとなっているイメージの検索方法は以下の通りです。

```
docker search --filter stars=3 busybox

NAME                    DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
busybox                 Busybox base image.                             2839      [OK]
･････
```

**・is-official**  
公式イメージか否かで検索します。公式イメージに絞って検索する場合、以下のように入力してください。

```
docker search --filter is-official=true busybox

NAME      DESCRIPTION           STARS     OFFICIAL   AUTOMATED
busybox   Busybox base image.   2839      [OK]
･････
```

**<–limit>**  
検索結果の最大数を指定するオプションで、最大数は1～100までの範囲で指定が可能です。（デフォルトは25）以下のように利用します。

```
docker search --limit 10 busybox

NAME                     DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
busybox                  Busybox base image.                             2839      [OK]
radial/busyboxplus       Full-chain, Internet enabled, busybox made f…   52                   [OK]
･････
```

**<–no-trunc>**  
詳細な説明を省略せずに表示するためのオプションです。以下のように利用します。

```
docker search --no-trunc busybox

NAME                                DESCRIPTION                                                                               STARS     OFFICIAL   AUTOMATED
busybox                             Busybox base image.                                                                       2839      [OK]
radial/busyboxplus                  Full-chain, Internet enabled, busybox made from scratch. Comes in git and cURL flavors.   52                   [OK]
･････
```

### Dockerイメージをダウンロードして利用するまでの手順

Docker Hubから取得（ダウンロード）したDockerイメージは、実行（run）することですぐにDockerコンテナとして利用できます。

dockerイメージをダウンロードする際のコマンドは以下の通りです。

```
docker image pull [オプション] イメージ名
```

以下のように利用します。

※ここでは参考までに、Webサーバー「Apache(httpd)」の公式イメージをダウンロードする例を紹介します。

```
docker image pull httpd

･････
```

次にdockerイメージを実行（run）する際のコマンドは以下の通りです。

```
docker container run [オプション] イメージ名
```

以下のように使います。

※ここでは先にダウンロードしたApache(httpd)のDockerイメージを実行する例を紹介します。

```
docker container run -d -p 8080:80 httpd
```

※「-d」はコンテナをバックグラウンドで実行するオプションです  
※「-p」はコンテナのポート番号と、サーバーのポート番号を紐づけるオプションです。  
　本例ではコンテナの80番ポートと、サーバーの8080番ポートを紐づけています。

本コマンドを実行し、ブラウザで「http://DockerコンテナのIPアドレス：8080」へアクセスすると、以下のようなWebページが表示されます。

実際の表示画面

実行中のコンテナは、以下コマンドで確認できます。

```
docker container ls

CONTAINER ID   IMAGE     COMMAND              CREATED         STATUS         PORTS                                   NAMES
10d8cc64387b   httpd     "httpd-foreground"   6 minutes ago   Up 6 minutes   0.0.0.0:8080->80/tcp, :::8080->80/tcp   eager_volhard
root@v133-18-227-131:~#
```

実行中のコンテナは、以下「docker stop」コマンドで停止できます。コマンドの引数として使用するコンテナID（CONTAINER ID）は、上記「docker container ls」コマンドで確認可能です。

```
docker container stop 10d8cc64387b
```

### Dockerイメージをアップロードする手順

自分で作成したDockerイメージを、Docker Hubにアップロードして公開したり他ユーザーと共有したりすることも可能です。

Dockerイメージは、Dockerfileと呼ばれるDockerイメージの設計図を基に作成します。

※Dockerfileの作成手順については、以下公式サイトのURLを確認下さい。

[https://docs.docker.jp/develop/develop-images/dockerfile\_best-practices.html](https://docs.docker.jp/develop/develop-images/dockerfile_best-practices.html)

DockerfileからDockerイメージを作成するコマンド例は以下の通りです。

```
docker image build -t イメージ名 Dockerfileが保存されているディレクトリパス
```

Docker hubに作成したイメージをアップロードするため、以下コマンドにてタグを指定します。

```
docker tag イメージID Docker hubアカウント名/イメージ名：タグ
```

コマンド例は以下の通りです。

※各項目について、それぞれ以下の通りであるとします。

・イメージID：aaaaaaaaaaa  
・Docker hubアカウント名：yamada ※1  
・イメージ名：imagename  
・タグ：latest ※2

```
docker tag aaaaaaaaaaa yamada/imagename:latest
```

※1「」の部分には別の文字が入るものとします  
※2タグには最新版を示す「latest」を指定するのが一般的です。

作成したDockeイメージをDocker Hubにアップロードするためには、まず以下コマンドでDocker Hubへログインします。

```
docker login -u アカウント名
```

※このあと、パスワードを聞かれますので指示に従って入力してください。

dockerイメージをアップロードするコマンドは以下の通りです。

```
docker image push イメージ名
```

上記でタグ付けしたイメージをpushする場合のコマンド例は以下の通りです。

```
docker image push yamada***/imagename:latest
```

上記コマンド実行後、以下のようにdockerイメージを検索すると、アップロードしたイメージが確認できます。

```
docker search imagename
```

## Docker Hub利用上の注意点

Docker Hubは、Dockerイメージを共有するのに便利なサービスです。ただパブリックのレジストリへアップロードする場合は、そのイメージが全世界に公開される点は注意しなくてはなりません。たとえばパスワードのような公開すべきでない情報は、パブリックレジストリにアップロードするイメージには含めないように注意して下さい。

またDocker Hubにアップロードされているイメージによっては、マルウェアなどリスクのあるデータが含まれていることも否定できません。Docker HubからDockerイメージをダウンロードする際は、十分に注意しましょう。

## まとめ

Docker Hubは、公式のDockerイメージ（コンテナ）共有サービスです。クラウド上のDocker Hubには、様々なアプリケーションのDockerイメージが公開されています。そのためユーザーは、それらイメージを取得しDocker上で目的のアプリケーションを簡単に実行可能です。ユーザー自身が作成したイメージをDocker Hub上で公開し、他ユーザーと共有することもできます。

KAGOYA CLOUD VPSでは初期費用無料、月額 550円(日額 20円)～の低価格で手軽にDockerを利用可能です。KAGOYA CLOUD VPSには [Docker CEのアプリケーションセットアップ](https://www.kagoya.jp/vps/dev/docker/?argument=vqHX23Xs&dmai=a627ca98183f8b) も用意されています。そのためDocker環境を、非常に簡単な手順で手間なく作成可能です。

KAGOYA CLOUD VPSについて詳しくは、以下公式サイトで確認下さい。

![](https://acq-3pas.admatrix.jp/if/5/01/c47515aa0dcee053f3abf91638b225b5.fs?cb=1958372&rf=https%3A%2F%2Fwww.kagoya.jp%2Fhowto%2Fcloud%2Fcontainer%2Fdockerhub%2F%3F_fsi%3Dlas7kSbo&prf=&i=las7kSbo)