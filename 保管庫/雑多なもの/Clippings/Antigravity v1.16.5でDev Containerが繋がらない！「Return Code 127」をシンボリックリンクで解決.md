---
title: "Antigravity v1.16.5でDev Containerが繋がらない！「Return Code 127」をシンボリックリンクで解決"
source: "https://zenn.dev/katy/articles/e7aec10c2f1076"
author:
  - "[[Zenn]]"
published: 2026-02-11
created: 2026-03-09
description:
tags:
  - "clippings"
---
3[tech](https://zenn.dev/tech-or-idea)

## 1\. はじめに

Antigravity を **v1.16.5** で使用していたところ、Dev Containers 機能でコンテナへ接続できない不具合に遭遇しました。

コンテナのビルドおよび起動は正常に完了するものの、その後の Server との通信フェーズで無限にリトライが発生する状態になります。

「最近になってコンテナに入る際にエラーが出るようになった」という場合、本記事の内容が参考になる可能性があります。

---

## 2\. 発生した事象

Dev Containers のログを確認すると、以下のエラーが繰り返し出力されていました。

```
[Error - 09:19:14.748] forwardPort stderr: forwarder error: handleClient Error: subprocess terminated immediately with return code 127
```

### return code 127 の意味

Linux において `127` は以下を意味します。

> Command not found（コマンドが見つからない）

つまり、IDE がコンテナ内で実行しようとした通信用バイナリが存在しない状態です。

ビルド失敗ではなく、「実行ファイルの探索パス不一致」が原因である可能性が高いことがここから読み取れます。

---

## 3\. 原因：ディレクトリ構造の不整合

ログを詳細に確認した結果、Antigravity v1.16.5 のインストーラーがバイナリを配置するパスと、IDE が探索するパスに不整合があることが判明しました。

### 実際に配置されたパス

```
~/.antigravity-server/bin/1.16.5-[COMMIT_HASH]/
```

### IDE が探索していたパス

```
~/.antigravity-server/bin/[COMMIT_HASH]/
```

### 問題の本質

- インストーラーは「バージョン番号付きディレクトリ」に配置
- IDE は「バージョン番号なし（旧形式）」のパスを参照

その結果、IDE 側が実行ファイルを見つけられず、 `return code 127` が発生していました。

これは **パス互換性の破綻** が原因です。  
（Googleさん修正頼んます）

---

## 4\. 解決方法：シンボリックリンクで互換パスを補完

この問題は不具合としてそのうち修正されると思いますが、今すぐなんとかしたいという場合は旧形式パスから新形式パスへシンボリックリンクを作成することで回避可能です。

つまり、

```
[COMMIT_HASH] → 1.16.5-[COMMIT_HASH]
```

というリンクを張ります。

---

### 手順 1：コンテナへ root で入る

まず使用するコンテナ ID を確認します。（Antigravityのログからも確認出来ます）

```
docker ps
```

例：

```
0311de7ae387
```

その後、root 権限でコンテナに入ります。

```
docker exec -u root -it 0311de7ae387 /bin/bash
```

---

### 手順 2：シンボリックリンクを作成

```
cd /home/vscode/.antigravity-server/bin
ls
ln -s 1.16.5-[COMMIT_HASH] [COMMIT_HASH]
```

`[COMMIT_HASH]` は実際のログに出ている値に置き換えてください。

---

### 手順 3：IDE をリロード

VS Code で以下を実行します。

```
Ctrl + Shift + P
→ Developer: Reload Window
```

これで正常に接続できるようになります。

---

## 5\. まとめ

今回の問題のポイントは以下です。

- ビルド失敗ではない
- return code 127 は「コマンド未検出」
- 原因はバイナリ配置パスと探索パスの不整合
- シンボリックリンクで後方互換を補完可能

同様のトラブルに遭遇した方の助けになれば幸いです。

3

### Discussion

![](https://static.zenn.studio/images/drawing/discussion.png)

ログインするとコメントできます

3