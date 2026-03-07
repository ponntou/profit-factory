---
title: "Windows + Antigravity + WSL2 + DevContainerで個人開発環境を作る"
source: "https://zenn.dev/yydevelop/articles/ba10fae0b65902"
author:
  - "[[Zenn]]"
published: 2026-01-10
created: 2026-03-08
description:
tags:
  - "clippings"
---


Google AI Proの年間プランが50%オフになっていたので、勢いで契約してしまいました。  
せっかくなのでこれを最大限活用したい。そう思ってGoogleが提供しているAIネイティブなコードエディタ「Antigravity」を使った個人開発を始めることにしました。

私はMacを持っていません。普段はWindowsを使っています。  
ただ、開発環境はなるべく汚したくないし、PCを買い替えても同じ環境を再現してコードを書き始めたい。そんな理由から、WSL2 + Docker（DevContainer）という構成で環境を作りました。

この記事では、Antigravityのインストールから、DevContainerを起動し、GitHubで管理するまでの手順をログとして残します。

## 最初にハマったこと

実は環境構築を始める前、Webブラウザ版のGeminiチャットに質問しながら進めていました。  
ところが、「Google AntigravityでWSL環境を作りたい」と聞いたら、Googleのサービスにもかかわらず「そのようなサービスは見つかりません」という回答が返ってきました。

Antigravityの公式ページ（ `https://antigravity.google/` ）のURLをいちいちチャットに貼り付けて「このページを読んで」と伝えないと認識してくれなくて、そこはイマイチでした。  
ただ、エラーが出たときにそのスタックトレースをそのまま投げたら、意外と推論して解決策を提示してくれたので、最近のGemini の解決能力はすごいなと感じました。

## 環境構築の手順

### 1\. 事前準備：ツールのインストール

#### 1-1. Antigravityのインストール

1. Google Antigravityの公式サイト（ `https://antigravity.google/` ）またはGoogle AI Proのダッシュボードからインストーラーをダウンロードして実行します。
2. インストール後の初回起動時に、 **VS Codeの設定をインポートするか** 聞かれます。私はVS Codeの設定を引き継ぎたかったのでインポートを選びました。
3. その後、Googleアカウントでサインインし、エージェントモードを選択すれば準備完了です。見た目はVS Codeそのものですが、左パネルにAIエージェントが常駐しています。

#### 1-2. WSL2の有効化

PowerShell（管理者）で以下を実行して再起動しました。これだけでUbuntuが入るので楽です。

```
wsl --install
```

再起動後、Ubuntuのセットアップ画面が開くのでユーザー名とパスワードを設定しました。

#### 1-3. Docker Desktop for Windows

公式サイトからインストーラーを落として入れました。  
インストール後、 `Settings > Resources > WSL integration` を開き、「Enable integration with my default WSL distro」にチェックが入っていることと、「Ubuntu」のスイッチがONになっていることを確認しました。

### 2\. プロジェクトフォルダの作成

プロジェクトフォルダはWindows側（ `C:\Users\...`）ではなく、WSL側（ `/home/user/...`）に作りました。

#### なぜWSL側に作るのか

WSL2の仕様上、ファイルの保存場所によってI/Oパフォーマンスが劇的に変わるからです。

| 保存場所 | パフォーマンス |
| --- | --- |
| Linux側（ `/home/user/` ） | 速い（ネイティブ並み） |
| Windows側（ `/mnt/c/` ） | 遅い（約5倍〜） |

Windows側に置くと、 `git clone` や `npm install` が遅すぎて開発になりません。Microsoftのドキュメントでも同じOSのファイルシステムに置くことが推奨されています。

手順としては、Windowsのスタートメニューから「Ubuntu」を開き、以下のコマンドを打ちました。

```
cd ~
mkdir profit-factory
cd profit-factory
```

### 3\. DevContainerの定義

Ubuntuのターミナルで `.devcontainer/devcontainer.json` を作成しました。

```
mkdir .devcontainer
nano .devcontainer/devcontainer.json
```

中身はこんな感じです。ひとまず最低限の設定にしています。

```
{
  "name": "Profit Factory",
  "image": "mcr.microsoft.com/devcontainers/typescript-node:1-20-bullseye",
  "remoteUser": "root",
  "customizations": {
    "vscode": {
      "settings": {},
      "extensions": [
        "dbaeumer.vscode-eslint"
      ]
    }
  },
  "postCreateCommand": "npm install"
}
```

ついでに `repos/` ディレクトリをGit管理から外す設定もしました。

今後、この `repos/` 配下に個別のアプリケーションリポジトリをCloneして開発していく運用イメージです。  
`profit-factory` 自体はあくまで「開発環境のコンテナ」を管理するための外枠という位置づけになります。

```
profit-factory/          # 開発環境（DevContainer）管理用リポジトリ
 ├── .devcontainer/      # コンテナ定義
 │   └── devcontainer.json
 ├── repos/              # ★ここに各プロジェクトをCloneする（Git除外対象）
 │   ├── my-app-1/       # 個別のWebアプリなど
 │   └── my-app-2/
 ├── GEMINI.md           # エージェントへの指示
 └── .gitignore
```

```
echo "repos/" > .gitignore
```

```
echo "repos/" > .gitignore
```

### 4\. GitHub CLIのインストールと認証

Ubuntu上で `gh` コマンドを使えるようにしました。aptで入ります。

```
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
&& sudo mkdir -p -m 755 /etc/apt/keyrings \
&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

インストール後、 `gh auth login` でブラウザ認証を通しました。

### 5\. Gitリポジトリ作成

この環境構築用のリポジトリをPrivateで作りました。

```
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

git init
git add .
git commit -m "Initial commit"

# CLIだけでリポジトリ作成からPushまで完結
gh repo create profit-factory --private --source=. --remote=origin
git push -u origin main
```

### 6\. AntigravityでDevContainerを開く

ここで少しハマりました。

#### 失敗パターン

Antigravityで「Connect to WSL」してから「Reopen in Container」するとエラー（ `TypeError: Cannot read properties of undefined...`）が出ました。どうやら多段接続がまだ不安定なようです。

#### 成功パターン

Windows側から直接UNCパスを指定する方法です。

1. Antigravity起動。
2. `F1` キー → `Dev Containers: Open Folder in Container...` を選択。
3. パス入力欄に以下を入力。

```
\\wsl.localhost\Ubuntu\home\あなたのユーザー名\profit-factory
```

これで無事にビルドが走り、DevContainerが立ち上がりました。

### 7\. エージェント設定

最後に、AIエージェントのコンテキスト設定を行いました。  
Antigravityでは、プロジェクトルートに `GEMINI.md` というファイルを置くと、そのプロジェクト全体（プロジェクトスコープ）で有効な指示としてエージェントに認識されます。Cursorでいう `.cursorrules` や、Anthropicのエージェントにおける `CLAUDE.md` のようなものです。

今回は `GEMINI.md` を作成し、以下のカスタム指示を書きました。

```
日本語で回答してください。
この環境は個人開発を行うためのdevcontainer環境です
repos配下に開発プロジェクトごとのリポジトリを作成します
```

## 感想

最初は「Google製のサービスなのにGeminiがAntigravityを知らない」というコントみたいな状況でしたが、エラー対応能力はずば抜けて高く、無事に環境構築できました。  
なにより、PCを買い替えても `git clone` してDevContainerを開くだけで開発環境が戻ってくる安心感は大きいです。

これからこの環境で、いくつか個人開発アプリを作っていこうと思います。

15

7

15

7