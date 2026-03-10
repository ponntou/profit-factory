---
title: "VSCodeからGoogle Antigravityへ"
source: "https://zenn.dev/iwatagumi/articles/9d143653579ab8"
author:
  - "[[Zenn]]"
published: 2025-11-25
created: 2026-03-09
description:
tags:
  - "clippings"
---
[岩田組](https://zenn.dev/p/iwatagumi) [Publicationへの投稿](https://zenn.dev/faq/what-is-publication)

72

67[tech](https://zenn.dev/tech-or-idea)

こんにちは！kirigayaです  
VSCodeからGoogle Antigravityへ移行した時のメモを残します  
ついでにAntigravity使って記事にしました  
Review機能すごく使いやすい！  
あなたも反重力を体験しよう！反重力って....  
![](https://storage.googleapis.com/zenn-user-upload/5c0c041108c1-20251125.png)

## Google Antigravity 導入と設定

Google Antigravity は、VS Code をベースにした AI ネイティブな IDE です。エージェント機能とエディタ機能が統合されており、コーディング体験を大きく変える可能性を秘めています。  
この記事では、Antigravity を VS Code ライクに快適に使うための導入と設定方法を紹介します。

## インストール

Antigravity は専用の [インストーラー](https://antigravity.google/) からインストールします。  
インストール後は、VS Code と似たインターフェースが表示されますが、左側にエージェント管理画面があるのが特徴です。

## 設定：拡張機能マーケットプレイスの変更

デフォルトでは OpenVSX 等が設定されている場合がありますが、VS Code の公式マーケットプレイスを利用できるように設定を変更することで、使い慣れた拡張機能をそのまま利用できるようになります。

1. **設定を開く**: `Settings` -> `Antigravity Settings` -> `Editor` へ移動します。
2. **URL を更新する**: 以下の項目を VS Code の公式 URL に変更します。
	- **Marketplace Item URL**:
		```
		https://marketplace.visualstudio.com/items
		```
	- **Marketplace Gallery URL**:
		```
		https://marketplace.visualstudio.com/_apis/public/gallery
		```
3. **再起動**: 設定変更後、Antigravity を再起動します。

これで、拡張機能の検索やインストールが VS Code と同様に行えるようになります。

## ブラウザー機能をオンにする

Web ブラウジング機能を活用するために、以下の Chrome 拡張機能をインストールすることをお勧めします。

[Antigravity Browser Extension](https://chromewebstore.google.com/detail/antigravity-browser-exten/eeijfnjmjelapkebgockoeaadonbchdd)

![](https://storage.googleapis.com/zenn-user-upload/70e9265894dd-20251125.png)

## 拡張機能のインストールと環境構築

マーケットプレイスの設定が完了したら、必要な拡張機能をインストールして環境を整えましょう。

### おすすめの拡張機能

- **テーマとアイコン**: `GitHub Theme` や `vscode-icons` などを入れると、見た目が VS Code に近づき違和感が減ります。
- **AMP**: コマンドラインツールやドキュメント作成に便利な拡張機能です。API Key を使用してログインします。
- **CodeX**: CodeX は直接ダウンロードリンクがない場合があるため、VS Code からエクスポートしてインポートします。
	1. **VS Code で準備**: VS Code に CodeX 拡張機能がインストールされていることを確認します。
	2. **エクスポート**: VS Code の拡張機能管理画面から CodeX を探し、`.vsix` ファイルとしてエクスポートします。
	3. **インポート**: Antigravity の拡張機能パネルを開き、メニューから「Install from VSIX...」を選択します。
	4. **インストール**: 先ほどエクスポートした `.vsix` ファイルを選択してインストールします。

### エディタ設定の最適化

既存の VS Code の `settings.json` の内容（インデント、フォーマット設定など）を Antigravity のワークスペース設定にコピーすることで、移行コストを最小限に抑えることができます。

1. **VS Code の設定を開く**: VS Code でコマンドパレット (`Cmd+Shift+P`) を開き、 `Preferences: Open Settings (JSON)` を実行して `settings.json` の内容をコピーします。
2. **Antigravity の設定を開く**: Antigravity でも同様にコマンドパレットを開き、 `Preferences: Open Settings (JSON)` を実行します。
3. **貼り付け**: コピーした内容を Antigravity の `settings.json` に貼り付けます。
	- ※ Antigravity 特有の設定と競合しないよう、必要な部分（フォーマットやエディタの挙動など）を選んで移行することをお勧めします。

## 現時点での移行に関するメリットとデメリット

最後に、現時点で VS Code から Antigravity へ移行する際のメリットとデメリットをまとめます。

### メリット

- **強力なエージェント統合**: エージェント機能とエディタがシームレスに統合されており、コード修正の速度と完了率が高いです。
- **VS Code ベースの親和性**: 基本的な操作感は VS Code そのものであり、設定変更により VS Code の豊富な拡張機能エコシステムを活用できます。

### デメリット・課題

- **カスタマイズ性の制限**: GitHub Copilot Chat のようなカスタムプロンプトやエージェントの作成が現状では制限されています。
- **モデルの選択肢**: OpenAI や Anthropic などの主要な最新モデルがネイティブに統合されておらず、GitHub Copilot に劣る部分があります。
- **安定性**: リリースしてからまだ短い時間で、安定性が保たれていない可能性があります。

72

67

72

67