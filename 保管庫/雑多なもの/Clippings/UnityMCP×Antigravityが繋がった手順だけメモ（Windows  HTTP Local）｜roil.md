---
title: "UnityMCP×Antigravityが繋がった手順だけメモ（Windows / HTTP Local）｜roil"
source: "https://note.com/roils/n/ncdd326f4b806"
author:
  - "[[roil]]"
published: 2026-01-11
created: 2026-03-09
description: "UnityをAntigravityから操作できるようにしたくて、UnityMCPを入れました。 この記事は、実際に自分の環境で「疎通確認まで成功した手順だけ」を、順番どおりにまとめた備忘録です。  ゴールはこれです。Antigravityから unityMCP / debug_request_context を叩いて、session_id と接続先が返ってくるところまで。   やったこと全体の流れ    uv を入れる    Unityに MCP for Unity を追加する    Unity側でサーバー起動して Session Active にする    Unity側で Antig"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/243085615/rectangle_large_type_2_5821402ac223c508b789432a89952ed7.png?width=1280)

## UnityMCP×Antigravityが繋がった手順だけメモ（Windows / HTTP Local）

[roil](https://note.com/roils)

UnityをAntigravityから操作できるようにしたくて、UnityMCPを入れました。  
この記事は、実際に自分の環境で「疎通確認まで成功した手順だけ」を、順番どおりにまとめた備忘録です。

ゴールはこれです。Antigravityから unityMCP / debug\_request\_context を叩いて、session\_id と接続先が返ってくるところまで。

---

## やったこと全体の流れ

1. uv を入れる
2. Unityに MCP for Unity を追加する
3. Unity側でサーバー起動して Session Active にする
4. Unity側で Antigravity を Configure する
5. Antigravity側で unityMCP を Enabled にして、ツールをONにする
6. debug\_request\_context が通るか確認する

---

## 1\. uv を入れる

PowerShellで実行しました。

```swift
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

入ったか確認。

```swift
uv --version
```

---

## 2\. Unityに MCP for Unity を追加する

Unityでプロジェクトを開いて、Package ManagerからGit URLで追加しました。

- Window > Package Manager
- 左上の +
- Add package from git URL...

入力したURLはこちら。

```javascript
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity
```

---

## 3\. Unity側でサーバー起動 → Session Active

次にUnityのMCPウィンドウを開きます。

- Window > MCP for Unity > Toggle MCP Window

Connectionはこう設定しました（どちらもデフォルトです）。

- Transport: **HTTPLocal**
- HTTP URL: [**http://localhost:8080**](http://localhost:8080/)

そのまま、

- Start Server を押す
- Start Session を押す

画面に緑で **Session Active** が出れば、この時点でUnity側の準備はOKです。

![画像](https://assets.st-note.com/img/1768130867-VS7b9l0hvx6wJTngk5NXApID.png?width=1200)

![画像](https://assets.st-note.com/img/1768131386-uPihblYZNeLCU86onpmXx10y.png?width=1200)

同時にcmdでこんな表示が立ち上がります

---

## 4\. Unity側で Antigravity を Configure

同じMCPウィンドウを下にスクロールしたところにある Client Configuration で、

- Client: **Antigravity**
- Configure を押す

緑で **Configured** が出ました。

![画像](https://assets.st-note.com/img/1768130978-TGK4ZUcvjkMD7YPbA8HIhfez.png?width=1200)

---

## 5\. Antigravity側で unityMCP を Enabled にする

Antigravityで、

- MCP Servers→Manage MCP Servers

をクリック（画像を参考）。

![画像](https://assets.st-note.com/img/1768131180-I0qE9b7lt24nLgdJwV356RsT.png)

![画像](https://assets.st-note.com/img/1768131207-5GPBQ6klMjxAOp4T8FZ9Dcyv.png)

![画像](https://assets.st-note.com/img/1768131261-qMpLjgosteKVEhN50m2F17SU.png?width=1200)

何も出てないときはRefreshを押すと出てきます。  
**Enabled** をONに。

---

## 6\. 疎通確認：debug\_request\_context を実行

Antigravityのチャットでこれを実行。

> UnityMCPの debug\_request\_context を実行して、session\_id と接続先URLを教えて

返ってきた結果はこんな感じでした。

- session\_id: 9189c7c62f08484c9bde0527d436abb2
- 接続先URL: http://localhost:8080

ここまで出たので、UnityMCPとAntigravityの接続は成功。

## いいなと思ったら応援しよう！

UnityMCP×Antigravityが繋がった手順だけメモ（Windows / HTTP Local）｜roil