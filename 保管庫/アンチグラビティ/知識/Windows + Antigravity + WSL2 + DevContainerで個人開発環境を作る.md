# 要約：Windows + Antigravity + WSL2 + DevContainerで個人開発環境を作る

## 概要
MacではなくWindows環境を利用している開発者が、ネイティブに近いパフォーマンスと環境のポータビリティ（再現性）を両立させるため、WSL2、Docker、そしてAIエディターの「Google Antigravity」を組み合わせた個人開発環境を構築する手順を紹介した記事。

## 主要なポイント
- **アーキテクチャの基本**:
  - Windows側にファイルを置くとI/Oパフォーマンスが極端に低下するため、ソースコードは必ず**WSL側（Linux側）**に配置する。
- **DevContainerを用いたプロジェクト管理**:
  - プロジェクトルートに `.devcontainer/devcontainer.json` を配置。
  - `repos/` フォルダを起点にして複数のプロジェクトをCloneし、環境そのものをGitHubでコード化・管理する仕組みを導入。（`.gitignore`で`repos/`を除外して外枠のみを管理）。
- **Antigravityにおけるトラブルと解決**:
  - WSLから「Reopen in Container」を使用する際のエラーを避けるため、WindowsからUNCパス（`\\wsl.localhost\Ubuntu\home\...`）を直接指定してプロジェクトを開くことで成功。
  - プロジェクトルートに特定の指示を書いた `GEMINI.md` （AIエージェントへのルールファイル）を配置し、プロジェクト共通のコンテキストを認識させる。
