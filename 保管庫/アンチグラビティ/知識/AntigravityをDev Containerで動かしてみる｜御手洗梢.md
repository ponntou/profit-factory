# 要約：AntigravityをDev Containerで動かしてみる｜御手洗梢

## 概要
AIエージェントであるAntigravityが意図せずローカル環境の大事なファイルを変更してしまうリスクを避けるため、隔離された安全な環境「Dev Container」上でAntigravityを動作させる手順と検証結果をまとめた記事です。

## 要点
- **背景と目的**: アンチグラビティの自律的なファイル操作に対する安全性を担保するため、標準搭載されているDev Container機能を活用する実験。
- **環境構築手順 (Windows)**:
  - WSL2とDocker Desktopの設定を行う。
  - プロジェクトフォルダに`.devcontainer/devcontainer.json`を配置し、使用するイメージ（Ubuntu）やツール（Node.js, Playwright, Python等）を定義。
  - Antigravity内で「Reopen in Container」を実行してコンテナ環境を立ち上げる。
- **制約と工夫**: Dev Container内ではAntigravity標準のブラウザ操作（GUI）が使えないため、Playwrightのヘッドレスモードをインストールし、AIに「見えないブラウザでスクショを撮って保存させる」という代替手段をとっている点。
- **結果**: 隔離環境内でAIがコードを生成し、ヘッドレスブラウザでプレビュー画像を保存するまでの一連のタスクが無事に完遂できた。
