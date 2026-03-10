---
title: "VSCode(VisualStudioCode)の定番機能を一挙解説"
source: "https://qiita.com/midiambear/items/bc0e137ed77153cb421c"
author:
  - "[[midiambear]]"
published: 2023-10-16
created: 2026-03-09
description: "はじめに コードエディタ界の王様VisualStudioCode。開発の際に使っている方も多いのではないでしょうか。 本記事では、VSCode(VisualStudioCode)の定番機能を紹介していきます。 この記事を読んで、VSCodeマスターになりましょう！ 弊..."
tags:
  - "clippings"
---

## VSCode(VisualStudioCode)の定番機能を一挙解説

530

投稿日

## はじめに

コードエディタ界の王様VisualStudioCode。開発の際に使っている方も多いのではないでしょうか。  
本記事では、VSCode(VisualStudioCode)の定番機能を紹介していきます。  
この記事を読んで、VSCodeマスターになりましょう！

弊社Nucoでは、他にも様々なお役立ち記事を公開しています。よかったら、Organizationのページも覗いてみてください。  
また、Nucoでは一緒に働く仲間も募集しています！興味をお持ちいただける方は、 [こちら](https://www.recruit.nuco.co.jp/?qiita_item_id=bc0e137ed77153cb421c) まで。

## そもそもVSCodeって？

VSCode（VisualStudioCode)はMicrosoft社が提供する無償のコードエディタです。2015年リリースですが、着々とユーザーを増やしており、2023年現在、世界で最もポピュラーなコードエディタの1つとなっています。

### コードエディタって？

字や記号などのテキストで構成されているファイルを編集するソフトのことをテキストエディタと呼びます。  
その中でも、ソースコードの編集を主な目的としたものがコードエディタと呼ばれます。

### VSCodeが選ばれる理由

コードエディタはたくさんリリースされていますが、なぜVSCodeが人気なのでしょうか。

- OSS（オープンソースソフトウェア)として開発されており、進化スピードが速い
- macOS、Windows、Linuxといった主要なプラットフォームをサポートしている
- 様々な言語に対応している
- 「拡張機能」をインストールすることで、機能を強化することができる
- Git連携ができる

このように、たくさんの特徴を持っており使い勝手が良いため人気のコードエディタとなっています。

## VSCodeのインストールと使い方

ここでは、VSCodeを全く使ったことがない人向けにインストールから使い方まで解説します

### VSCodeインストール方法

#### Windowsの場合

1\. まず [公式ダウンロードページ](https://code.visualstudio.com/Download) からインストーラーをダウンロードします

[![スクリーンショット 2023-09-14 12.55.41.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/c22ec1b5-4f35-382e-7e26-ecfc7ae56af7.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc22ec1b5-4f35-382e-7e26-ecfc7ae56af7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fd604dd4440304ddee065787fa96c394)

2\. ダウンロードしたインストーラーを開く  
3\. 使用許諾契約書の同意について聞かれるため、よく読んだ後「同意する」を選択し、「次へ」をクリック  
4\. VSCode のインストール先のフォルダを指定し、「次へ」をクリック  
5.　スタートメニューフォルダを指定し、「次へ」をクリック  
6\. 追加タスクを選択し、「次へ」をクリック  
7\. 設定内容を確認し、「インストール」を行う

#### Mac OSの場合

1\. [公式ダウンロードページ](https://code.visualstudio.com/Download) からインストーラーをダウンロードします  
[![スクリーンショット 2023-09-14 12.56.02.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/1da7be99-73ce-9b5f-67c7-0b2e152fe28e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F1da7be99-73ce-9b5f-67c7-0b2e152fe28e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4be90bd0c69a5b7a03c19d292aa30f44)

2\. ダウンロードしたファイルを解凍する  
3\. Visual Studio Code.appをアプリケーションフォルダに移動させる

これでインストールが完了します！

### 基本的な使い方

#### 日本語拡張機能インストール

VSCodeのデフォルト言語は英語なので、日本語設定にするための拡張機能をインストールします。

1\. 画像の左側の拡張機能のアイコンから拡張機能検索画面を開く  
2\. 検索窓に「japanese」と打ち込み、「Japanese Language Pack for Visual Studio Code」を開く  
3\. インストールする  
[![日本語拡張機能.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/c0b753fa-88db-b671-a2c2-0c8f1058c610.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc0b753fa-88db-b671-a2c2-0c8f1058c610.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c1c0386150665a73883f7869d9b55062)

4\. VSCode再起動をすると日本語の設定になる

#### 画面構成

VSCodeの画面は下の図のように5つに分かれています。  
[![画面構成　①.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/c40fc286-e6af-264b-0825-ea3d91c9a92e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc40fc286-e6af-264b-0825-ea3d91c9a92e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3aef55c7f67f515c088eccb1b922eac7)

①アクティビティバー  
左側にあり、ビューを切り替えることができます。  
設定から、アクティビティバーに表示するアイコンの数を増減させたり、非表示にしたりすることができます。

②サイドバー  
選択しているビューを表示できます。上図では「エクスプローラー」を選択しているので、現在開いているファイル名とそのファイルが入っているファイルが表示されています。

③エディタ  
ファイルを編集するためのエリア。複数エディタを開くことも可能です。

④パネル  
出力やデバッグ情報、統合ターミナルなどを表示させることができます。  
パネルの場所は設定から変更できます。

⑤ステータスバー  
開いているプロジェクト、編集しているファイルに関する情報を表示しています。

#### 基本機能解説

- **書式設定**  
	VSCodeのエディタには2種類のフォーマットアクションがあります。  
	**1\. Format Document**  
	ファイル全体をフォーマットする  
	**コマンド**  
	macOS：Shift + option + F  
	Windows：Shift + Alt + F  
	**2\. 選択の書式設定**  
	選択したテキストの書式の設定ができる  
	**コマンド**  
	macOS：Command + K → Command + F  
	Windows：Ctrl + K → Ctrl + F
- **検索・置換**  
	開いているファイル内を検索して置き換えができます。  
	**コマンド**  
	macOS：Command + F  
	Windows：Ctrl + F  
	開いているフォルダ内の全てを検索できるコマンドもあります。  
	macOS：Shift + Command + F  
	Windows：Shift + Ctrl + F  
	検索エディタからフォルダ内を検索することも可能です。  
	[![検索.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/9fbc9e71-6415-ef39-bce6-290ebd582f59.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9fbc9e71-6415-ef39-bce6-290ebd582f59.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=cf46b6969b329dae6862d77a2a9aa583)
- **複数選択**  
	macOSでoption（WindowsだとAlt）を押しながら、カーソルを動かすと、複数選択ができます。  
	[![スクリーンショット 2023-10-08 16.36.53.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f50e4a4a-3726-ff60-f2cc-10d8a93741fb.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff50e4a4a-3726-ff60-f2cc-10d8a93741fb.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2ba4f9f287dff53b07b94dbd1a2e149b)
- **自動保存**  
	ファイルの自動保存にチェックを入れると、自動で保存してくれます。  
	[![自動保存.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/b5e72c06-c983-0e4e-bfbe-771bfc75eb43.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fb5e72c06-c983-0e4e-bfbe-771bfc75eb43.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=681785f9d1b62a75068eb12a8ae81199)
- **折りたたみ**  
	折りたたみアイコンを使用して、ソースコードを折りたたんだり展開したりすることができます。  
	[![4gWTJB8S5ZJROToAZzVI1695567309-1695567339.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9334b493-09bc-a001-f792-1b6d172c0ec9.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ab3d626e51c50a93cf185ade5a745bb3)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9334b493-09bc-a001-f792-1b6d172c0ec9.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ab3d626e51c50a93cf185ade5a745bb3)

## VsCodeでコーディングする

ここでは、コーディングがはかどる機能を紹介していきます。  
知っているだけで、コーディング生活が快適なものになるはずです。

### タブ

ファイルを開いている状態で、別のファイルをクリックすると、新しいファイルがタブとして開かれます。  
タブとして開かれているファイルを右側に寄せると、画面を左右分割させることができます。（上下分割もできます。）  
[![69aXh4Zkrq4WkaWdlZbe1695569109-1695569131.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4cc10295-314a-d9d6-4d54-e74aebb97491.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f3cd5bc0054e69ca4431f1f00f7fa3d9)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4cc10295-314a-d9d6-4d54-e74aebb97491.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f3cd5bc0054e69ca4431f1f00f7fa3d9)

### コード補完

エディタにコードを入力すると、補完の候補が表示されます。カーソルキーで選択し、EnterまたはTabで補完候補のコードが挿入されます。文脈に沿って提案されるので非常に便利です。

### コマンドパレット

いろいろなコマンドを検索して実行することができます。  
[![スクリーンショット 2023-10-09 13.09.28.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/ec311c94-3566-1dc5-c690-292e46ff5cb3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fec311c94-3566-1dc5-c690-292e46ff5cb3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2260d29147ee4fc170dd30424912d601)

**コマンド**  
macOS：Command + Shift + P または F1  
Windows：Ctrl + Shift + P または F1

### エラー

VSCodeの拡張機能で、それぞれの言語の拡張機能やリンタの拡張機能を入れることで、コンパイルエラーやリンタエラーに波線が引かれ、エラー箇所がわかりやすくなります。また、エラーの詳しい内容も表示されるため便利です。  
[![エラー.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/a8b0b4e9-4349-9438-c142-5936a60c82cf.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa8b0b4e9-4349-9438-c142-5936a60c82cf.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fa0a51bb62a21b2fbbddb70de1011677)

### クイックフィックス

機械的に修正可能なエラーに関しては、コードの冒頭に電球マークが付くことがあり、マークをクリックすると、修正の候補が出てきます。修正したいものをクリックすると、修正を行なってくれます。  
[![クイックフィックス.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/530206b8-789b-0386-aec0-4d923f391ae3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F530206b8-789b-0386-aec0-4d923f391ae3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f15f0c1e2bfa6e47a2d25520d1090315)

### ユニットテスト

VSCode上ユニットテストを行う際には、使用している言語に合わせたテストフレームワークを導入する必要があります。この導入も、拡張機能から使っている言語に合わせたフレームワークをインストールして行います。テストの設定やテストの実行を簡単に行うことができます。  
拡張機能の検索画面で「:"testing"」と打ち込むと、テストのフレームワークがたくさん出てきます。  
[![テスト.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/e68805a2-6d96-84ae-2203-4948b2996c83.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fe68805a2-6d96-84ae-2203-4948b2996c83.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7dc3f0b4720d6e0c93699c54c160175f)

### デバッグ実行

テストを実行して、失敗した際に、テストの失敗を検証する作業をデバッグと呼びます。  
アクティビティバーの「デバッグと実行」を選択するとデバッグセッションが開始できます。画面上にデバッグツールバーが表示され、簡単にデバッグを実行することができます。また、デバッグコンソールでログを見ることもできます。

#### デバッグアクション

デバッグツールバーの使い方を紹介します。  
[![スクリーンショット 2023-10-09 15.29.55.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/2be1233a-5d87-6472-f61f-95c9f37a1b14.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F2be1233a-5d87-6472-f61f-95c9f37a1b14.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7dfef0d3d06351d5a12cdc99e221e873)  
画像の左側から表にまとめてみました。

| デバッグアクション | 説明 |
| --- | --- |
| 続行/一時停止 | プログラムの実行を一時停止したり、一時停止したプログラムを次のブレイクポイントまで実行したりできます。 |
| ステップオーバー | 現在の行を実行し、関数呼び出しは無視します。関数呼び出しの内部の詳細を追わずに、単に次の行に進みたい場合に使用します。 |
| ステップイン | 関数またはメソッド内に入ることができます。 |
| ステップアウト | 関数またはメソッドから出たい場合に使用します。 |
| 再起動 | デバッグセッションを再起動します。 |
| 停止 | デバックセッションを停止して、プログラムの実行を終了します。 |

#### ブレークポイント

デバッグを行う際に一時停止する点をブレークポイントと言います。  
VSCodeではこれを簡単に設定することができます。

デバッグを行うファイルを開き、余白をクリックすることでブレークポイントを設置できます。また、ブレークポイントの赤丸を再度クリックすることでブレークポイントを削除することも可能です。  
[![YaW5GD1lDEsIUYq6HvAJ1696840145-1696840188.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F0def1797-fd4f-a0bf-f3fb-9dbda8a927a2.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d335f79d58b8e80f9e14ddc049b139b5)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F0def1797-fd4f-a0bf-f3fb-9dbda8a927a2.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d335f79d58b8e80f9e14ddc049b139b5)

- **ブレークポイントの無効化**  
	サイドバーのブレークポイントの欄のチェックを入れたり外したりすることで、ブレイクポイントを有効にしたり無効にしたりできます。無効化したブレークポイントは白丸として表示されます。  
	（無効化:ブレイクポイントは置いているもののブレークポイントが実行されない状態にすること）  
	[![DiSYoIvhD2CCCMYRHu561696840307-1696840327 (1).gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F520d9ef9-7772-aab3-4aa6-09ef75e21eb7.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a95ec15c8aed6bfc106b7bc52fd7ab3b)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F520d9ef9-7772-aab3-4aa6-09ef75e21eb7.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a95ec15c8aed6bfc106b7bc52fd7ab3b)
- **条件付きブレークポイント機能**  
	条件式を入力することができ、条件を満たした場合にブレークポイントが実行されます。  
	[![pAMfFiBPtWs2cKwwnwnr1696841379-1696841431.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F691fd9b9-d3bc-1f49-d6c8-61d545b2d6f0.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=735328ac70fb11e51aa79ca620424f1b)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F691fd9b9-d3bc-1f49-d6c8-61d545b2d6f0.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=735328ac70fb11e51aa79ca620424f1b)
- **ヒットカウント機能**  
	ヒットカウントを設定することができ、設定した回数分コードが実行されるとブレークポイントが実行されます。  
	[![pAMfFiBPtWs2cKwwnwnr1696841379-1696841966.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F00147179-d32d-9fde-b985-e9aaa0c4945c.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e6a96ae9ac1e3dd49656788c567d0a89)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F00147179-d32d-9fde-b985-e9aaa0c4945c.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e6a96ae9ac1e3dd49656788c567d0a89)
- **ログポイント機能**  
	ブレークポイントに到達した際にログを出力することができます。  
	[![pAMfFiBPtWs2cKwwnwnr1696841379-1696841787.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F09b905f0-52fa-eaee-1db7-834a9b8a7a22.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=cc95107be593516e3bd63a3b56b94ce5)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F09b905f0-52fa-eaee-1db7-834a9b8a7a22.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=cc95107be593516e3bd63a3b56b94ce5)
- **関数ブレークポイント**  
	関数でブレークポイントを実行できます。  
	サイドバーのブレークポイントの欄の「+」をクリックし、関数を入力することでブレークポイントを関数で設定できます。  
	[![JFUxsHnxTkB12K5vSzgT1696842740-1696842759.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F455828df-33bd-6bfd-f5c4-2b20043886bd.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f7c40b87dc974701a493ca3b37c4eaa3)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F455828df-33bd-6bfd-f5c4-2b20043886bd.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f7c40b87dc974701a493ca3b37c4eaa3)
- **インラインブレークポイント**  
	コードの途中にブレークポイントを挟むことができる機能です。  
	まず、ブレークポイントを入れたい位置で右クリックを行います。「インラインブレークポイントを追加」をクリックします。  
	[![スクリーンショット 2023-10-09 15.42.08.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/18713c38-0254-ed99-b211-972e9e9046ff.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F18713c38-0254-ed99-b211-972e9e9046ff.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=92be7ecf4a6e602c9b29a1e76e679ff1)  
	ブレークポイントがコード内に入っていることが確認できます。  
	[![スクリーンショット 2023-10-09 15.42.22.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/4eacb767-341d-1ede-86df-75cc0890e2d6.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4eacb767-341d-1ede-86df-75cc0890e2d6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a349a03c070de56d278609965d9dfa15)

## チーム開発でVScodeを使う

チーム開発をする際に必要不可欠なGitですが、VSCodeからも操作することができます。VScode上でのGit操作の仕方を紹介します。

### Gitとの連携

#### そもそもGitとは？

Gitとは分散型のバージョン管理システムのことです。簡単に言うと、ファイルのバージョン管理がすごく簡単にできるツールになります。バージョン管理システムには、「集中型」と「分散型」の2種類が存在しますが、近年は個人でファイルの保管場所を持って好きなタイミングで同期させることができる「分散型」が主流になっています。

#### Git操作

Gitの操作はVSCodeの画面のソース管理から行う方法と、ターミナルから行う方法があります。

##### ソース管理から操作したい場合

画面左側のアクティビティバーのソース管理からGit操作ができます。  
視覚的にわかりやすく、コマンドを覚えていない初心者でも簡単に操作ができます。  
[![Git.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/ad06c21f-385d-8f7d-e29c-2ca48d9e2052.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fad06c21f-385d-8f7d-e29c-2ca48d9e2052.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ee06016d21a4fe7b6a6cbec3919b1cde)

- **リポジトリ作成（リポジトリ初期化）**  
	まず、ローカルリポジトリを作成します。  
	ファイルを開いて、「リポジトリを初期化する」をクリックすることでローカルリポジトリを作成できます。  
	[![スクリーンショット 2023-10-08 14.07.40.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/c00fabe0-a9c7-dee5-ac55-7e86242a08cd.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc00fabe0-a9c7-dee5-ac55-7e86242a08cd.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fea7eca68ab20d286c8edb36d1d127e6)
- **コミット**  
	「new.txt」というファイルを作成し、コミットする場合を考えます。  
	ファイルに「B」というテキストを入力したとします。  
	[![スクリーンショット 2023-10-08 14.34.42.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f05a7394-7e54-65bc-d2f5-378b7738d453.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff05a7394-7e54-65bc-d2f5-378b7738d453.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d2da423617f2f7d0574f76b0bb013d5d)  
	左側のソース管理のところにある「変更」というところのファイルの「＋」をクリックして、ステージング状態にします。  
	[![スクリーンショット 2023-10-08 14.35.29.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/daf77f83-d7f8-6faf-ce35-3e4b294419c1.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fdaf77f83-d7f8-6faf-ce35-3e4b294419c1.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2e0015a252a0146eb22240fb637202df)  
	ステージング状態になるとこのような画面になります。  
	[![スクリーンショット 2023-10-08 14.35.37.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/e5be4e0c-65d2-bddc-5feb-36ab9243c8e8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fe5be4e0c-65d2-bddc-5feb-36ab9243c8e8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d2c1ff67cf119ea92a16b146e37d18c7)  
	この状態で、メッセージの部分にコメントを入れ、コミットをクリックします。（ここではコメントは「add B」としました。）  
	こうすることでコミットが完了します。
- **ブランチ**  
	**ブランチの作成**  
	新しいブランチを作るためには、まず、画面左下にあるブランチ名（この場合は「main」）をクリックします。  
	[![スクリーンショット 2023-10-09 14.32.14.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/042ad536-2835-a8b2-3ac5-fd961f1e9e6a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F042ad536-2835-a8b2-3ac5-fd961f1e9e6a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=60f2fa425c311c14e9ecda3c671020a8)  
	次に、新しいブランチの作成をクリックし、ブランチ名を入力します。  
	[![スクリーンショット 2023-10-08 14.37.39.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/ea5e5e12-9048-4b6f-5d5c-734d7e80f24c.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fea5e5e12-9048-4b6f-5d5c-734d7e80f24c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=735866c919851ffa43dc7b1041410e50)  
	[![スクリーンショット 2023-10-08 14.37.47.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/cf461847-b5a5-0e1d-c105-e7e5ee6957b8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fcf461847-b5a5-0e1d-c105-e7e5ee6957b8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=132178c9899cc1e8e514ac33a230ef57)  
	こうすることで、新しいブランチを作成することができます。（ここでは「new branch」という名前のブランチを作成）  
	[![スクリーンショット 2023-10-08 14.40.19.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f35ff942-b15a-e3e3-1b50-214d1feba2c5.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff35ff942-b15a-e3e3-1b50-214d1feba2c5.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4f9ff2a27d00cfe528eda7b5e54008bc)

**作成したブランチをmain（master）にマージ**  
「new branch」でコミットした内容を「main」にマージします。ここでは、「new branch」で「add C」「add D」という内容をコミットしている状態からはじめます。  
[![スクリーンショット 2023-10-08 14.42.44.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/60c7108a-2f83-7b8d-404b-a0e99920b0a0.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F60c7108a-2f83-7b8d-404b-a0e99920b0a0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=bd1f72063d1433dd8949867413e6a99b)

まず、ブランチを「main」に切り替えます。先程ブランチを作った方法と同じようにしてブランチ名をクリックし、「main」に切り替えを行います。  
[![スクリーンショット 2023-10-08 14.43.52.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f3a3c399-519f-76ab-be01-5e0242a06df0.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff3a3c399-519f-76ab-be01-5e0242a06df0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a2fa97bbf3277bf7f2b8e4db8402e127)

マージしたい内容のコミットの「More」という部分をクリックし、「Marge this」をクリックします。（ここでは「add C」をマージします）  
[![スクリーンショット 2023-10-08 14.44.27.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/427822a3-fa20-ef30-f012-8b8746345db3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F427822a3-fa20-ef30-f012-8b8746345db3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=0c5c6c747624b945c859f06402066381)  
確認画面が出てくるので、「Yes」を選択します。  
[![スクリーンショット 2023-10-08 14.44.37.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/2ccbdd60-84bb-4981-86eb-2816b49bd4ad.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F2ccbdd60-84bb-4981-86eb-2816b49bd4ad.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=77a7cea48a62f66b44522f3c9ea84a08)  
マージが完了していることがわかります。  
[![スクリーンショット 2023-10-08 14.45.04.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/2aa98138-5127-dc7e-7fc5-b2951aaf8506.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F2aa98138-5127-dc7e-7fc5-b2951aaf8506.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=bafb42977d57557e51df5d08c610e62b)

また、マージして不要になったブランチは、ブランチ名の「×」ボタンから簡単に削除できます。

- **プッシュ**  
	ローカルリポジトリをプッシュする方法です。  
	まず、GitHubにリモートリポジトリを作成します。作成した「new repository」にプッシュしたいと思います。  
	[![スクリーンショット 2023-10-08 15.45.49.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/fa8ce290-252b-23c7-85e8-effdd259d374.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ffa8ce290-252b-23c7-85e8-effdd259d374.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=6ad081d2a0ab84784c25e38f7331bfab)

コマンドパレットで「git add remote」を打ち込み、リモートリポジトリを選択します。  
[![スクリーンショット 2023-10-09 14.52.48.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/fc2eef7a-ccbb-0405-2f58-a63635f89594.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ffc2eef7a-ccbb-0405-2f58-a63635f89594.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=45524f0a6a478b69b7dd2f6f41f09093)  
「GitHubからリモートを追加する」を選択します。  
[![スクリーンショット 2023-10-09 14.53.41.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/b3217823-a58e-1b62-0664-70e5ceba3769.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fb3217823-a58e-1b62-0664-70e5ceba3769.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2fcf28d6a8bec41198b49b66ca2d0845)  
先程作った「new repository」を選択します。  
[![スクリーンショット 2023-10-09 14.53.49.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/9df1eddb-afc0-6afa-e293-fe520fb6d5de.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9df1eddb-afc0-6afa-e293-fe520fb6d5de.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2445677fdd2547da14516eaa7ed0cd63)

プッシュする先のリポジトリを選択した後、ソース管理のメニューからプッシュを行います。  
[![スクリーンショット 2023-10-09 14.52.05.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/00ef44e2-678c-1cb0-6374-8087d7f36821.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F00ef44e2-678c-1cb0-6374-8087d7f36821.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2ad293142773aa1b8c6c5e49acdc4cf7)

きちんとプッシュされていることが確認できます。  
[![スクリーンショット 2023-10-08 15.46.07.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f11b4907-5f15-0f6b-a27b-ff02c6273e57.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff11b4907-5f15-0f6b-a27b-ff02c6273e57.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3f336e12ea3f23c3aab611230563f747)

##### ターミナルから操作したい場合

ターミナルはツールバーのターミナルから開くことができます。また、分割もすることもできます。  
ターミナルをVSCode上で開くことができれば、エディタを開いたままGit操作ができ、快適です。  
[![DLp2sKourhmvqlU6ONO71695599512-1695599544.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F80d42116-0310-b9e1-7eb9-4b4a6b92c819.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=eae21ddaff12fe6474b845cd54b1eb6c)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F80d42116-0310-b9e1-7eb9-4b4a6b92c819.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=eae21ddaff12fe6474b845cd54b1eb6c)

### Gitの拡張機能解説

#### GitLens

Gitの変更履歴をわかりやすく表示する拡張機能です。誰がいつコミットしたかが表示されるようになり、チームで開発を行う際にとても便利です。  
[![gitlens.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/9d99d107-7426-f65b-ce4e-3568fd679c98.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9d99d107-7426-f65b-ce4e-3568fd679c98.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e1642a58d2289f9ac25a284af373bf02)

どのコードを誰が、いつコミットしたか表示されていることがわかります。  
[![gitlens2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/43c19c28-2115-9f8a-3b6e-b2753997060a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F43c19c28-2115-9f8a-3b6e-b2753997060a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2fbd986eefa819f510048602dc297a38)

#### Git History

gitのログをファイル単位で見やすくしてくれます。  
[![git history.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/11377014-3418-d1dc-e42e-2482e850ec8e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F11377014-3418-d1dc-e42e-2482e850ec8e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ce1aca659babf3d312cbbd0b4650a6ca)

コミット履歴を検索することができたり、ファイルの更新履歴を一覧にしてくれたりします。  
[![githistory2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/a544070f-9be9-fbbc-cf48-a2d585de00f7.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa544070f-9be9-fbbc-cf48-a2d585de00f7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=6c7da102da925940191d086b9eeb7bcf)

#### Git Graph

Gitの操作履歴をツリー状で確認できます。  
[![gitgraph.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/43cbe0cb-5bd4-18fe-564e-0afe2b3c8825.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F43cbe0cb-5bd4-18fe-564e-0afe2b3c8825.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9394ee33cf08807754d6fdd491adbb7e)

このように表示されます。（チーム開発をする際にはもっと枝分かれします）  
[![git graph2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/e580d709-63be-841f-0c2e-a92892755c7b.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fe580d709-63be-841f-0c2e-a92892755c7b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=410d872163e3c95e4d89c86f1df08090)

## VScodeを自分仕様にしてみる

エンジニアにとってコードエディタは必需品です。自分が使っているコードエディタを自分好みにカスタマイズしたいと感じる方も多いのではないでしょうか。ここでは、VScodeの見た目やUIを自分好みにする方法を解説します。

### テーマ配色とアイコン

#### テーマ配色

1\. 拡張機能の検索画面で自分の好きなテーマを探しましょう。  
検索窓に「:"themes"」と打ち込むと、配色テーマの拡張機能に絞ることができます。  
[![配色テーマ6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/68c55b95-4a40-53a6-0a6b-552d0ac97e6e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F68c55b95-4a40-53a6-0a6b-552d0ac97e6e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7d44123aa12519749ff676e6b21a4d11)

2\. アクティビィバーの管理アイコンをクリックし、「配色テーマ」をクリック  
[![配色テーマ1.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/57ee0489-764e-cf49-a7fa-20d13473a183.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F57ee0489-764e-cf49-a7fa-20d13473a183.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=66260102442f95a3e837bd275e14bb55)

3\. テーマを選ぶ  
[![配色テーマ4.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/605b92f6-e2bc-4df1-d340-448e16019ce0.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F605b92f6-e2bc-4df1-d340-448e16019ce0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2c34e8c77b7b5169acbd629c93c07b5d)

4\. 選んだテーマに変わる（既存のDarkテーマからAtom One Dark Themeに変更）  
[![配色テーマ5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/dac9f2c2-4171-39d3-f503-ca7d0167e97f.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fdac9f2c2-4171-39d3-f503-ca7d0167e97f.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4f3a8954012998ce6e369bf21ce8e5d6)

#### オススメテーマ配色

- [**One Dark Pro**](https://marketplace.visualstudio.com/items?itemName=zhuangtongfa.Material-theme)  
	よく使われている定番テーマです。コードも見やすく、視覚的にも優しい配色です。  
	[![スクリーンショット 2023-10-08 16.03.00.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/f52cbfa8-cb56-a632-98bb-143b001516c8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ff52cbfa8-cb56-a632-98bb-143b001516c8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3b50485d00b191aecc85f896a2c58271)
- [**Ayu**](https://marketplace.visualstudio.com/items?itemName=teabyii.ayu)  
	ライト、ダーク、ミラージュの3つの背景色からテーマを選ぶことができ、人気のテーマです。  
	[![スクリーンショット 2023-10-08 16.01.57.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/14d3cc4a-1ce4-53d3-3c5d-78376eb38313.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F14d3cc4a-1ce4-53d3-3c5d-78376eb38313.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ef8b22cc6a06d6430cc040c45e092eeb)
- [**Dracula Official**](https://marketplace.visualstudio.com/items?itemName=dracula-theme.theme-dracula&ssr=false#overview)  
	青みがかった背景色が特徴の人気テーマです。  
	[![スクリーンショット 2023-10-08 16.04.01.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/51513c1f-946f-d9ec-f249-90aa6c39b26b.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F51513c1f-946f-d9ec-f249-90aa6c39b26b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e23465511e4785e58eb52df691b6193b)
- [**GitHub Theme**](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme)  
	GitHubのクラシックなテーマが好きな人はぜひ使ってほしいテーマです。  
	[![スクリーンショット 2023-10-08 15.57.53.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/9c3b9931-20fc-b262-1a4e-345d6995e1c5.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9c3b9931-20fc-b262-1a4e-345d6995e1c5.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=048b1cb5cb46c2df616d15b1068736f4)

#### アイコン

1\. 拡張機能の検索画面で自分の好きなテーマを探しましょう。  
検索窓に「icon」と打ち込むと、配色テーマの拡張機能に絞ることができます。  
[![アイコン.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/6d36da19-3fe7-678a-3b97-07fb461b0117.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F6d36da19-3fe7-678a-3b97-07fb461b0117.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b3271e7d4d4c0be4e7522550ee7e133b)

2\. アクティビィバーの管理アイコンをクリックし、「ファイル　アイコンのテーマ」をクリック  
[![アイコン6.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/4c0a33e6-5aef-cd0f-9df0-2a312cd158c8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4c0a33e6-5aef-cd0f-9df0-2a312cd158c8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=18535d692901b9d33070918709e48100)

3\. テーマを選ぶ  
[![アイコン7.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/b168acc9-cbbf-f47e-b9b9-f0ecf39a2853.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fb168acc9-cbbf-f47e-b9b9-f0ecf39a2853.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d3e2c4b094e5d63d5ffbeec349f08064)

4\. 選んだテーマに変わる（既存のテーマからvscode-iconsに変更）  
[![アイコン8.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/ba221727-d654-db2a-fbec-e7fbba1844a0.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fba221727-d654-db2a-fbec-e7fbba1844a0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=10acd7df309db980738fcd3a32292065)

#### オススメアイコンテーマ

よく使われているアイコンテーマをご紹介します。

- [**vscoode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons)  
	[![スクリーンショット 2023-10-09 13.45.18.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/e08f2711-ef0f-0810-b447-017b427668b3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fe08f2711-ef0f-0810-b447-017b427668b3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b524e5f6f2b9d53710bfefc786162b3a)
- [**Material Icon Theme**](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)  
	[![スクリーンショット 2023-10-08 16.07.19.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/aaa05d68-c181-fcba-195b-f256e43e3ea5.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Faaa05d68-c181-fcba-195b-f256e43e3ea5.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=9b0c15a7b94651f608ee404aaa90741e)
- [file-icons](https://marketplace.visualstudio.com/items?itemName=file-icons.file-icons)  
	[![スクリーンショット 2023-10-08 16.08.11.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/5681fe8d-54a8-3d25-9831-ccecf4d78471.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F5681fe8d-54a8-3d25-9831-ccecf4d78471.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=ac2204429da6398dd0c04ef99b881306)

### ミニマップ

長いコードを書くときに、自分がどこを書いているのかわからなくなることありますよね？  
それを解決してくれるのがミニマップです。  
開いているファイルのコードの全体像を表示してくれ、どのあたりを書いているのかを把握することができます。  
ミニマップは、ツールバーの「表示」をクリックし、ミニマップにチェックを入れると表示できます。  
[![uSi30f7BjbP7WCgRgKIW1695611429-1695611460.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc00fca95-f090-d234-5449-93d65a640887.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d51dbbf348d942730c24f11dbd8d6567)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc00fca95-f090-d234-5449-93d65a640887.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=d51dbbf348d942730c24f11dbd8d6567)

### インデント・タブスペース

インデントの設定は、エディタの下、ステータスバーから見ることができます。  
「スペース：4」と表示されているため、現在はインデントはスペース4つ分が設定されていることがわかります。  
[![インデント2.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/83c06a7e-e425-b6af-2ffd-106d67dad418.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F83c06a7e-e425-b6af-2ffd-106d67dad418.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=2ccd23ff6f7a60f4c0008c46a561b407)  
先ほどの部分をクリックすると、インデントの設定画面が出てきます。自分好みのインデントを設定しましょう。  
[![インデント.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/91360a7e-df93-fb9e-30b3-290eafcda3cf.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F91360a7e-df93-fb9e-30b3-290eafcda3cf.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=26d0062c7d2316f0c3ac640a83245670)

### スニペット

スニペットとはよく使うコードを簡単に呼び出せるようにする機能です。  
for文などであらかじめ登録されているものもありますが、自分で登録することも可能です。  
設定方法は、ツールバーの「Code」から「基本設定」をクリックし、「ユーザースニペットの構成」をクリックします。そうすると、スニペットの設定画面が出てきます。  
[![Ipi1bn6oNU8hpUEh1THt1695613514-1695613555.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F46f7a118-e7e1-84dd-cf2d-487df58deb0d.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8cb5c7e891ec056c0e491ed18bcfb085)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F46f7a118-e7e1-84dd-cf2d-487df58deb0d.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8cb5c7e891ec056c0e491ed18bcfb085)

また、拡張機能からスニペットを呼び出すことができます。  
拡張機能画面から「:"snippets"」と打ち込んで検索できます。  
[![スニペット5.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/aa6d77fc-b8be-a7a2-1cd6-c1c9acfd15dc.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Faa6d77fc-b8be-a7a2-1cd6-c1c9acfd15dc.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=aa450d4c8a3d1ae7a9dd37c58a90488b)

### ショートカットキー

一瞬でやりたいことができるショートカットキー、自分好みに登録したい方も多いのではないかと思います。  
ショートカットキーの設定は、ツールバーの「Code」から「基本設定」をクリックし、「キーボード ショートカット」をクリックします。そうすると、ショートカットキーの設定ができます。  
[![qVH1OJGUdDu5RzO5NKLd1695613608-1695613647.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4a45d623-a595-6d9e-1b10-2234a66781f3.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5815126436d7adbaa38c14fc8a9d7bb6)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4a45d623-a595-6d9e-1b10-2234a66781f3.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5815126436d7adbaa38c14fc8a9d7bb6)

上記では、VSCodeのメニューからカスタマイズする方法を紹介しましたが、VSCodeのカスタマイズ方法は複数あります。  
自分が使いやすい方法を選択できると良いかもしれません。

### 設定変更の方法

#### エディタで設定タブを開く（GUIで操作）

エディタで設定タブを開くことでカスタマイズを簡単に行うことができます。

- 「Code」から開く  
	Code→基本設定→設定で開けます  
	[![zd1YqUnt8Jsxiw4kafpu1696980313-1696980390.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa6f93b32-182b-40e1-190d-c8b4c99624fe.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3635dd16448c9e9c803b620b9b961dec)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa6f93b32-182b-40e1-190d-c8b4c99624fe.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=3635dd16448c9e9c803b620b9b961dec)
- コマンドパレットから開く  
	1\. 表示→コマンドパレットを開く  
	（「Command(Ctrl)」+「Shift」+「P」）  
	2\. 検索窓に「open settings」と入力  
	3\. 「設定（UI）を開く」をクリック  
	上記の手順で開くことができます  
	[![qYcOH4zfwq96JioeWgLi1696980457-1696980491.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fdb39e7e9-3e62-e670-53a4-8c994d6dc6d7.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=abba3ba14e9b3fc6f46bf6c67cf6d6fc)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fdb39e7e9-3e62-e670-53a4-8c994d6dc6d7.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=abba3ba14e9b3fc6f46bf6c67cf6d6fc)
- アクティビティバーの設定アイコンから開く  
	設定アイコンをクリックし、「設定」を選択すると開きます  
	[![hftkvgKjYLFjl0Ja6v0H1696980521-1696980562.gif](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc7e01389-514b-3bd0-be3b-8ac4ca7d188d.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7970a8695135abe9bed510c20f6ad4af)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fc7e01389-514b-3bd0-be3b-8ac4ca7d188d.gif?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=7970a8695135abe9bed510c20f6ad4af)
- ショートカットで開く  
	Mac：「Command」+「,」  
	Windows：「Ctrl」+「,」  
	で開くことができます。

#### 「setting.json」ファイルを編集する

「setting.json」ファイルを編集することでもカスタマイズができます。  
より詳細に設定したい場合はこちらでカスタマイズすると良いでしょう。

- 設定タブから開く  
	設定タブを開き、右上のアイコンから「settings.json」ファイルを開くことができます。  
	[![スクリーンショット 2023-10-11 8.10.52.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/0a638677-c18b-f5e6-1055-e8a16f33a2dc.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F0a638677-c18b-f5e6-1055-e8a16f33a2dc.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fdaa9b88680c45277fda8c9fcd57afee)
- コマンドパレットから開く  
	1\. 表示→コマンドパレットを開く  
	（「Command(Ctrl)」+「Shift」+「P」）  
	2\. 検索窓に「open settings」と入力  
	3\. 「ユーザー設定を開く（JSON）」をクリック  
	上記の手順で開くことができます

### オススメ設定

こちらでは、コードを書く際にオススメの設定を紹介します。

#### 最終行に改行を挿入する

[![スクリーンショット 2023-10-11 8.57.06.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/d7124b6d-b69f-e021-c23d-7ef718276a9b.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fd7124b6d-b69f-e021-c23d-7ef718276a9b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e0b8c8df2b91f1bc3a64f9d518425618)

settings.json

```json
"files.insertFinalNewline": true
```

### ファイル保存時にコードを整形する

[![スクリーンショット 2023-10-11 10.21.18.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/2bfb3768-1ff1-2ef1-dc59-80ccebfad6af.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F2bfb3768-1ff1-2ef1-dc59-80ccebfad6af.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=1cab09ac6374b39f00d7cac621a7d9e6)

settings.json

```json
"editor.formatOnSave": true
```

### 最終行以降の不要な行を削除する

[![スクリーンショット 2023-10-11 10.31.33.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/8c66175b-ad6f-a849-5673-1e3622b464a9.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F8c66175b-ad6f-a849-5673-1e3622b464a9.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=bc400ef17fc38d87fb72638e0a9e30a3)

settings.json

```json
"files.trimFinalNewlines": true
```

### 行の末尾にある無駄な空白を削除する

[![スクリーンショット 2023-10-11 10.31.46.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/81814c0a-b89c-a800-57f1-d5153b9ac30e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F81814c0a-b89c-a800-57f1-d5153b9ac30e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=b36ed8755b3fe6872dddecb73eca86b3)

settings.json

```json
"files.trimTrailingWhitespace": true
```

### 制御文字の表示

[![スクリーンショット 2023-10-11 10.45.10.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/3416c66d-7d7e-3097-e446-89066236f451.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F3416c66d-7d7e-3097-e446-89066236f451.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e76a7ed71100dbb1904f40091146b69a)

settings.json

```json
"editor.renderControlCharacters": true
```

### 折り返し

[![スクリーンショット 2023-10-11 10.45.41.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/07d9a94a-a1d9-08cb-3389-3fbe49829c7c.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F07d9a94a-a1d9-08cb-3389-3fbe49829c7c.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=68b8ff4adc82d55b484c7a520d4ab4ad)

settings.json

```json
"editor.wordWrap": "on"
```

### パンくずリスト（階層リスト）表示

[![スクリーンショット 2023-10-11 10.49.57.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/18db1e1a-a29d-cbb1-397d-b25bd5336eb7.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F18db1e1a-a29d-cbb1-397d-b25bd5336eb7.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=66596a40fa2602aa8763853b2d3b2090)

settings.json

```json
"breadcrumbs.enabled": true
```

### ツリーのインデントガイド表示

[![スクリーンショット 2023-10-11 10.46.43.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/de861d39-d98b-425f-48e6-295145a7b1a4.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fde861d39-d98b-425f-48e6-295145a7b1a4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=dfe55f3b4c39e9bfd07189a3d61f939a)

settings.json

```json
"workbench.tree.renderIndentGuides": "always"
```

### ツリーのアニメーション表示

[![スクリーンショット 2023-10-11 10.48.19.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/9b1eb9f7-415d-1512-2d29-da93caac02e3.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F9b1eb9f7-415d-1512-2d29-da93caac02e3.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=89942fa9d649325a16898ef45f6057d6)

settings.json

```json
"workbench.reduceMotion": "on"
```

### 書式設定無しでテキストをコピーできる

[![スクリーンショット 2023-10-11 10.49.00.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/be256b6b-67ec-ec43-8bdd-0f43331b612a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fbe256b6b-67ec-ec43-8bdd-0f43331b612a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=8ae4cd24f7bb6fffd90bf6f0f6054b95)

settings.json

```json
"editor.copyWithSyntaxHighlighting": false
```

他にもたくさん設定できるので、自分で使いやすいように設定してみてください。

## 拡張機能

VSCodeは拡張機能の豊富さが大きな魅力です。  
ここでは、入れておくと便利な拡張機能をいくつか紹介します。

### Live Share

リモートでも、リアルタイムで共同編集やデバッグなどができます。ターミナルやサーバーの共有もできてしまう優秀拡張機能です。  
[![Liveshare.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/4c28ba6c-bc75-999b-c87e-1620bddcb8c8.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F4c28ba6c-bc75-999b-c87e-1620bddcb8c8.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=e69fb2943bb51b8536a7a618e29278be)

### Live Server

簡易的なローカルサーバを立てることができ、HTMLファイルをサーバーに上げた時の様子を確認できる拡張機能です。  
[![Liveserver.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/5d0a7c4e-2216-4c50-3fe2-c51e6284c7e4.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F5d0a7c4e-2216-4c50-3fe2-c51e6284c7e4.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=005681e0d881561e3c594f62d56518ad)

### Dev Containers

Dockerを用いたリモート開発をする場合に重宝する拡張機能です。  
[![スクリーンショット 2023-10-08 16.20.41.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/a8b17f8b-6466-4548-7c5e-455f1a2dd880.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa8b17f8b-6466-4548-7c5e-455f1a2dd880.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=f4c610cc2cb946a8bdb212ecf3387e5b)

### REST Cliant

VSCode上でHTTPリクエストを簡単に行えるようになる拡張機能です。  
[![Rest cliant.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/89775508-f240-d47e-3e02-63b26e36d3c0.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F89775508-f240-d47e-3e02-63b26e36d3c0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=fc2ffffcd935c29fff75a3a412e67d22)

### Prettier - Code formatter

HTML、JavaScript、Markdownなどのフォーマットを自動で行なってくれる拡張機能です。  
[![Prettier.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/065ca605-fa63-c962-d9c6-094111182d5e.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F065ca605-fa63-c962-d9c6-094111182d5e.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=1f62956fb6e0a29d052d4afdbcd04e1e)

### Rainbow CSV

CSVのそれぞれのカラムを色分けして見やすくしてくれます。  
[![スクリーンショット 2023-10-08 16.15.54.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/eeef17a6-6d26-057b-ec06-6e54dab16690.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Feeef17a6-6d26-057b-ec06-6e54dab16690.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c62018e57d387442f22cd2c80c0d8933)

### IntelliCode

コードの文脈やパターンを見て、次に書くコードを予測してくれるコード補完拡張機能です。  
[![スクリーンショット 2023-10-14 21.08.50.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/e4cf23dd-468b-311d-6413-156a506f6c2b.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fe4cf23dd-468b-311d-6413-156a506f6c2b.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=0e7045ffae0ee0540f246c740960729d)

### Auto Rename Tag

HTMLタグの開始タグを修正した際に、閉じタグも一緒に修正してくれる拡張機能です。閉じ忘れや修正し忘れを防ぐことができます。  
[![スクリーンショット 2023-10-14 21.09.50.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/a494fac3-fbd4-7e1d-6c69-ddc84017809d.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Fa494fac3-fbd4-7e1d-6c69-ddc84017809d.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=4baf98e46532df0647af0aa095add621)

### Code Runner

プログラムを簡単に実行することができる拡張機能です。様々な言語に対応しており、便利です。  
[![スクリーンショット 2023-10-14 21.10.33.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/7ff1991a-d700-f16c-9c40-8609d20832f6.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F7ff1991a-d700-f16c-9c40-8609d20832f6.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=c11207b2b96ffffd3d60d6a2ae68b559)

## VScodeの最新機能

VSCodeは毎月継続的に更新されており、毎月新しいバージョンにアップデートされています。  
アップデート内容は [公式サイト](https://code.visualstudio.com/updates/v1_82) から確認できます。

### 最新バージョンの機能

この記事を書いている時点での最新バージョン　（version 1.82）の機能をいくつか紹介します。

- **組み込みのポートの転送**  
	VSCode内から、ローカルで実行されているサービスをインターネットを経由して他の人やデバイスと共有できます
- **コマンドセンターをデフォルトで表示**  
	タイトルバーから素早くファイルを開いたり、コマンドを実行できるようになりました。
- **ノートブックの出力をコピー**  
	セル出力と生成されたイメージを簡単にコピーできるようになった。

かなりの頻度でアップデートされるのでチェックしてみましょう。

### Visual Studio Code for the Web

Webブラウザ上でVSCodeが無料で利用できるサービスです。  
デスクトップ版VSCodeが導入できないChromebookなどでコードを編集したい場合やiPadやAndroidタブレットでアプリを開発したい場合に重宝します。基本的にはデスクトップ版と同じように使用できますが、利用できない拡張機能があったり、統合ターミナルが使えないなどのデメリットがあったりするため、普段はデスクトップ版を使い、緊急でコードを直さなければならない場面などに使うのが良さそうです。  
[![VScode for Web.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/fa0f2f8e-6f87-d450-03d3-61f7af394f57.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2Ffa0f2f8e-6f87-d450-03d3-61f7af394f57.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=a113ec3eac779b54b782a1461a8cd9a8)

### Github Codespaces

こちらもブラウザ上でVSCodeが利用できるサービスです。  
上記の「Visual Studio Code for　the Web」と違う点は、GitHubが提供するクラウド上に開発環境を構築し、操作していくという点です。「Visual Studio Code for　the Web」よりも多くの機能がサポートされており、特にチーム開発をする場合に、開発環境を個人のPCで準備することなく統一できるので非常に便利です。しかし、使用料金はリソースの使用量によるため、注意が必要です。

### GitHub copilot

専用の拡張機能を入れることによって、AIがコードを自動生成してくれるサービスです。  
コードを書いている途中に、AIが予測したコードが出てきて、かなりの時短になるでしょう。  
もちろん、全てのコードが正しいとは限らないので、あくまでも「Copilot」として精査しながらコードを書いていく必要があります。利用は有料で、個人用アカウントで月10ドルで利用できます。  
[![github copilot.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/3033130/34f33dde-7182-8da0-55ca-3fec208e2e2a.png)](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.ap-northeast-1.amazonaws.com%2F0%2F3033130%2F34f33dde-7182-8da0-55ca-3fec208e2e2a.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=dfd3bc8409311f5610c136f6dc732c4e)

#### GitHub copilotの活用

- コメントからコード生成  
	コメントを書くだけで、やりたいことをコードとして出してくれます。  
	コメントを書く→コードが生成されるのでEnterで採択→またコメントを書く  
	という手順で作りたいものが完成します。便利すぎますね
- コード補完  
	コードを書いている途中に予測コードが出てきます。
- コメント生成  
	書いたコードに対するコメントを自動でつけることができます。  
	同じファイル内の既存コードと調和するように自動生成してくれます。
- テスト生成  
	関数等を作った後に同じファイル内に「テストコードを生成する」旨のコメントをつけると、テストコードを生成してくれます。自分で1から書かなくていいのでいいので非常に楽です。

## 参考サイト

- [開発の定番「VSCode」とは？ インストールから使い方までを解説](https://codezine.jp/article/detail/16467)
- [Visual Studio Codeの便利な使い方とは？インストール・拡張機能についても解説！](https://udemy.benesse.co.jp/development/system/visual-studio-code.html#:~:text=Visual%20Studio%20Code%E3%81%AE%E5%88%A9%E7%82%B9,%E3%81%AE%E3%81%8C%E4%B8%80%E7%95%AA%E3%81%A7%E3%81%99%E3%80%82)
- [【コーディングが爆速に！】ユーザースニペットとは？【Visual Studio Code】](https://zenn.dev/miz_dev/articles/157a7aaad0bdcf)
- [VSCode ではじめる GitHub Copilot 活用術](https://qiita.com/RyoWakabayashi/items/1207128e88669c76bf5f)
- [Visual Studio Codeを使うなら絶対に入れておきたい拡張機能Top20【2022最新版】](https://qiita.com/yamaguchi2000/items/76060c08764ce4c704f9)
- [VSCodeでのGitの基本操作まとめ](https://qiita.com/y-tsutsu/items/2ba96b16b220fb5913be)
- [君はVS Codeのデバッグの知られざる機能について知っているか](https://qiita.com/_ken_/items/c5aa4841be74b06530b4)
- [VSCodeのオススメ拡張機能 24 選 (とTipsをいくつか)](https://qiita.com/sensuikan1973/items/74cf5383c02dbcd82234)

## まとめ

今回はVSCodeの定番機能をご紹介しました。定番機能だけでも十分使い勝手がいいですが、様々な拡張機能によるカスタマイズで使い方は無限の可能性があります。VSCodeで快適な開発生活を送りましょう！

[0](https://qiita.com/midiambear/items/#comments)

コメント一覧へ移動

X（Twitter）でシェアする

Facebookでシェアする

はてなブックマークに追加する

新規登録して、もっと便利にQiitaを使ってみよう

1. あなたにマッチした記事をお届けします
2. 便利な情報をあとで効率的に読み返せます
3. ダークテーマを利用できます
[ログインすると使える機能について](https://help.qiita.com/ja/articles/qiita-login-user)

[新規登録](https://qiita.com/signup?callback_action=login_or_signup&redirect_to=%2Fmidiambear%2Fitems%2Fbc0e137ed77153cb421c&realm=qiita) [ログイン](https://qiita.com/login?callback_action=login_or_signup&redirect_to=%2Fmidiambear%2Fitems%2Fbc0e137ed77153cb421c&realm=qiita)