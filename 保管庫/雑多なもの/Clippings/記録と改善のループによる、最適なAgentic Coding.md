---
title: "記録と改善のループによる、最適なAgentic Coding"
source: "https://zenn.dev/sun_asterisk/articles/claude-code-with-otel"
author:
  - "[[Zenn]]"
published: 2026-03-06
created: 2026-03-10
description:
tags:
  - "clippings"
---
[Sun\* Developers](https://zenn.dev/p/sun_asterisk) [Publicationへの投稿](https://zenn.dev/faq/what-is-publication)

8

4[tech](https://zenn.dev/tech-or-idea)

## はじめに

Claude CodeのようなAIエージェントと一緒に開発を進めていると、以下が振り返りにくいと感じることはありませんか？

- 今日のセッションで何をやったのか
- どれだけのコミットやPRをエージェントと一緒に作ったのか

リポジトリのコミットログ・PRの一覧などは、GitHubのリポジトリのページや、 `git log` などから追うことができます。  
ただし、Claude Codeのログについては、以下のようにファイルが生成されるようになっています。

| パス | 内容 |
| --- | --- |
| ~/.claude/history.jsonl | コマンド入力の履歴 |
| ~/.claude/debug/\*.txt | デバッグログ（セッションごと） |
| ~/.claude/stats-cache.json | 使用統計キャッシュ |

つまり、 **Agentic Coding の文脈ではエージェントがどのように動いたか** について、  
ツール呼び出しの回数やログの詳細、どのプロジェクトで何をしたかといった情報は、デフォルトでは手元に残りません。  
そういった情報を取得したい時、Claude Codeが標準でサポートしている **OpenTelemetry (OTel) によるテレメトリ出力** を活用することで実現できます。

## Claude Code の OpenTelemetry サポート

Claude Codeは環境変数を設定するだけで、セッション中の各種テレメトリをOpenTelemetry経由で外部に送出できます。

主要な環境変数は以下のとおりです。

| 環境変数 | 説明 |
| --- | --- |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | `1` に設定するとテレメトリを有効化 |
| `OTEL_METRICS_EXPORTER` | メトリクスのエクスポート先（ `otlp` / `prometheus` / `console` ） |
| `OTEL_LOGS_EXPORTER` | ログのエクスポート先（ `otlp` / `console` ） |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLPのプロトコル（ `grpc` / `http/protobuf` / `http/json` ） |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLPエンドポイントのURL |
| `OTEL_METRIC_EXPORT_INTERVAL` | メトリクスのエクスポート間隔（ミリ秒、デフォルト: `60000` ） |
| `OTEL_LOGS_EXPORT_INTERVAL` | ログのエクスポート間隔（ミリ秒、デフォルト: `5000` ） |
| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | メトリクスの時系列タイプ（ `delta` / `cumulative` 、デフォルト: `delta` ） |
| `OTEL_LOG_TOOL_DETAILS` | `1` に設定するとMCPサーバー名やスキル名をログ出力 |
| `OTEL_LOG_USER_PROMPTS` | `1` に設定するとユーザープロンプトもログ出力 |
| `OTEL_RESOURCE_ATTRIBUTES` | リソース属性（ `project.name=myapp` 等）を付与できる |

これらを `~/.claude/settings.json` の `env` に追加するだけで、Claude Codeはセッション内のツール呼び出し・メトリクス・トレースをOTLPエンドポイントへ送信し始めます。

### settings.json への設定

`~/.claude/settings.json` を開き、以下のように `env` ブロックを追加します。

```
{
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp",
    "OTEL_LOGS_EXPORTER": "otlp",
    "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
    "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4317",
    "OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE": "delta",
    "OTEL_LOG_TOOL_DETAILS": "1"
  }
}
```

これだけで、次回以降のセッションから自動的にテレメトリが送出されます。

### プロジェクト名を自動付与する（SessionStart フック）

複数プロジェクトを行き来していると、どのプロジェクトのテレメトリか判別できなくなります。  
`SessionStart` フックを使えば、セッション開始時に作業ディレクトリ名を `project.name` として自動付与できます。

```
{
  "env": { "...": "上記と同じ..." },
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "jq -n --arg v \"project.name=$(basename $PWD)\" '{env: {OTEL_RESOURCE_ATTRIBUTES: $v}}'"
          }
        ]
      }
    ]
  }
}
```

これにより、ダッシュボードで `project.name` ごとのフィルタリングが可能になります。

## テレメトリ収集インフラの構成

Docker Composeで起動するインフラは以下の構成です。

```
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.103.0
    ports:
      - "4317:4317" # OTLP gRPC
      - "4318:4318" # OTLP HTTP
    volumes:
      - ./otelcol-config.yaml:/etc/otelcol-contrib/config.yaml
    depends_on:
      - openobserve

  openobserve:
    image: openobserve/openobserve:v0.60.1
    ports:
      - "127.0.0.1:5080:5080" # Web UI (localhost only)
    environment:
      - ZO_ROOT_USER_EMAIL=root@example.com
      - ZO_ROOT_USER_PASSWORD=${OPENOBSERVE_PASSWORD:?OPENOBSERVE_PASSWORD is required}
    volumes:
      - openobserve-data:/data

volumes:
  openobserve-data:
```

- **otel-collector**: Claude CodeからのOTLPデータを受け取り、OpenObserveへ転送します
- **OpenObserve**: ログ・メトリクス・トレースをオールインワンで可視化できる軽量バックエンドです。起動後は `http://localhost:5080` でダッシュボードにアクセスできます

### OTel Collector の設定ファイル

`docker-compose.yml` と同じディレクトリに `otelcol-config.yaml` を作成します。

`Authorization` の値は次のコマンドで生成します。 `docker-compose.yml` の認証情報を変更した場合は合わせて更新してください。

```
# read -s で入力するとシェル履歴にパスワードが残りません
read -rsp "OpenObserve password: " PASS && echo || exit 1
echo -n "root@example.com:${PASS}" | base64
unset PASS
```

### 利用可能な組み込みメトリクス

Claude Codeは追加設定なしで以下のメトリクスを標準出力します（抜粋）。

| メトリクス名 | 内容 |
| --- | --- |
| `claude_code.session.count` | セッション開始回数 |
| `claude_code.commit.count` | git commit の作成回数 |
| `claude_code.pull_request.count` | PR の作成回数 |
| `claude_code.lines_of_code.count` | 変更した行数（ `type: added/removed` ） |
| `claude_code.token.usage` | トークン使用量（ `type: input/output` 等） |
| `claude_code.cost.usage` | セッションのコスト（USD） |
| `claude_code.active_time.total` | 実際に操作していた時間（秒） |

コミット数やPR数は追加設定なしでそのまま取得できます。OpenObserve上でプロジェクト別にフィルタリングすれば「今月のエージェントとの協働の成果」を定量的に確認できます。

## 使い方の流れ

### 1\. 収集インフラを起動する

Docker Composeでotel-collectorとOpenObserveを起動します。

```
docker compose up -d
```

起動後は `http://localhost:5080` でOpenObserveの管理画面にアクセスできます。

### 2\. セッションを開くだけで記録が始まる

`settings.json` への設定が済んでいれば、 **何もしなくても** セッションを開くだけでテレメトリが収集されます。

`SessionStart` フックが自動的に `project.name` をセットし、プロジェクト名が付与された状態でテレメトリが流れ始めます。

### 3\. OpenObserve でデータを確認・分析する

セッション中に行ったツール呼び出しのログや、git commit / PR作成のカウントメトリクスをOpenObserveのダッシュボードで確認できます。

プロジェクト名でフィルタリングすれば「このプロジェクトの今月のエージェント活動量」なども把握できます。

## 記録から改善へのループ

テレメトリを取るだけでは意味がありません。重要なのは **記録→分析→改善** のループを回すことです。

例えば以下のような振り返りが可能になります。

- **ツール呼び出しの頻度分析** ：特定のツールが異常に多い場合、プロンプトや設定の見直しのヒントになる
- **プロジェクト別の活動量比較** ：どのプロジェクトにエージェントを多く使っているか把握できる
- **コミット数・PR数の推移** ：エージェントとの協働の成果を定量的に可視化できる
- **セッションあたりのコスト感覚** ：メトリクスとコスト情報を組み合わせることで、費用対効果の分析にも応用できる
- **試験的に導入した設定の効果検証** ：新しく追加したSkill・SubAgent・Hookが実際に呼ばれているかを `tool_result` イベントの `tool_name` や `skill_name` （ `OTEL_LOG_TOOL_DETAILS=1` が必要）で確認できる。「導入したのに使われていない」「意図しない頻度で発火している」といった問題を定量的に把握できる
- **チームへの展開** ：OTelは複数人のデータを同じバックエンドに集約できる。 `user.email` や `user.account_uuid` などの属性でメンバーごとに絞り込めるため、「チーム全体でどのツールが多用されているか」「誰のセッションでコストが高いか」といったチーム視点の分析も可能になる

### 具体例①：CLI コマンドをエージェントスキルに組み込む

毎日手動で打っているコマンド群をAgent Skillにするだけで、振り返りが一発で完了します。

例えば「今日の開発活動をまとめる」ために毎回、以下のコマンドをClaude Codeが実行しているとします。

```
git log --since=1.day --oneline
gh pr list --author=@me --json number,title,state
```

これを `.claude/agents/daily-summary.md` に定義します。

```
---
description: 今日のコミットと PR をまとめてレポートする
---

以下のコマンドを順番に実行し、今日の開発活動を日本語で箇条書きにまとめてください。

1. \`git log --since=1.day --oneline\` でコミット一覧を取得する
2. \`gh pr list --author=@me --json number,title,state\` で PR 状況を取得する
3. 取得した情報を日本語の箇条書きでまとめる
```

あとはClaude Code上で `/daily-summary` と打つだけです。「手順①→②→③を毎回実行する」という繰り返しが1つのコマンドに集約されます。

### 具体例②：テレメトリ分析をエージェントスキルに組み込む

ここでは収集したテレメトリを分析して改善提案を出すまでの流れを、 **Python スクリプト + Agent Skill** で実装する例を紹介します。

#### 1\. OpenObserve からデータを取得するスクリプト

`~/.claude/scripts/query_telemetry.py` を作成します。

```
#!/usr/bin/env python3
"""OpenObserve から直近 N 日分のテレメトリを取得して JSON で出力する。"""
import json
import os
from datetime import datetime, timedelta, timezone

import httpx

OPENOBSERVE_URL = os.getenv("OPENOBSERVE_URL", "http://localhost:5080")
OPENOBSERVE_USER = os.getenv("OPENOBSERVE_USER", "root@example.com")
OPENOBSERVE_PASSWORD = os.getenv("OPENOBSERVE_PASSWORD", "")
ORG = "default"
DAYS = int(os.getenv("REVIEW_DAYS", "7"))

if not OPENOBSERVE_PASSWORD:
    raise RuntimeError(
        "OPENOBSERVE_PASSWORD が設定されていません。"
        "実行前に環境変数を設定してください: export OPENOBSERVE_PASSWORD=..."
    )

def search(sql: str) -> list[dict]:
    now = datetime.now(timezone.utc)
    start = now - timedelta(days=DAYS)
    resp = httpx.post(
        f"{OPENOBSERVE_URL}/api/{ORG}/default/_search",
        json={
            "query": {
                "sql": sql,
                "start_time": int(start.timestamp() * 1_000_000),
                "end_time": int(now.timestamp() * 1_000_000),
                "size": 1000,
            }
        },
        auth=(OPENOBSERVE_USER, OPENOBSERVE_PASSWORD),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("hits", [])

def main() -> None:
    tool_stats = search(
        "SELECT tool_name, COUNT(*) AS cnt FROM default "
        "WHERE event_name='tool_result' GROUP BY tool_name ORDER BY cnt DESC LIMIT 10"
    )
    cost_stats = search(
        "SELECT SUM(cost_usd) AS total_cost, COUNT(*) AS api_calls "
        "FROM default WHERE event_name='api_request'"
    )
    error_stats = search(
        "SELECT COUNT(*) AS errors FROM default WHERE event_name='api_error'"
    )
    print(
        json.dumps(
            {
                "period_days": DAYS,
                "tool_usage_top10": tool_stats,
                "cost": cost_stats[0] if cost_stats else {},
                "api_errors": error_stats[0] if error_stats else {},
            },
            ensure_ascii=False,
            indent=2,
        )
    )

if __name__ == "__main__":
    main()
```

このスクリプトはOpenObserveの検索APIを通じて、直近 `REVIEW_DAYS` 日分のツール使用上位10件・コスト合計・APIエラー数をJSONで標準出力します。

#### 2\. Agent Skill を定義する

`.claude/agents/telemetry-review.md` を作成します。スクリプトの実行から分析・提案まで、Agent Skillの指示として記述します。

```
---
description: 直近のテレメトリを分析して Claude Code の運用改善を提案する
---

以下の手順でテレメトリを分析し、改善提案を作成してください。

1. \`python3 ~/.claude/scripts/query_telemetry.py\` を実行してデータを取得する
2. ツール使用回数の上位項目と、コストが高い傾向を読み取る
3. 異常なパターン（特定ツールの多用、高コスト操作など）を特定する
4. \`~/.claude/CLAUDE.md\` の現在の内容を確認する
5. テレメトリに基づいた具体的な改善案を提示する（必要に応じて CLAUDE.md への追記案も含める）
```

#### 3\. 実行する

スクリプト実行前に、環境変数 `OPENOBSERVE_PASSWORD` を設定してください。

```
# シェル履歴に残らないよう read -s で入力する
read -rsp "OpenObserve password: " OPENOBSERVE_PASSWORD && echo || exit 1
if [ -z "$OPENOBSERVE_PASSWORD" ]; then
  echo "Error: パスワードが未入力です。" >&2
  exit 1
fi
export OPENOBSERVE_PASSWORD
```

毎回入力するのが手間な場合は、 `~/.zshrc` や `~/.bashrc` に `export OPENOBSERVE_PASSWORD=...` を追記する方法もありますが、その場合はファイルのパーミッションに注意してください（ `chmod 600 ~/.zshrc` など）。

設定後、Claude Code上で以下と入力するだけです。

```
/telemetry-review
```

エージェントがスクリプトを実行し、結果を分析したうえで改善提案を返してくれます。テレメトリの取得から提案の生成まで一連の流れが自動化されるため、定期的な振り返りのコストが大幅に下がります。

Agentic Codingは「使えば終わり」ではなく、記録と改善のループを組み込むことで初めて最適化が可能になります。

## まとめ

- Claude Codeは `~/.claude/settings.json` に数行追加するだけでOpenTelemetryテレメトリを出力できる
- `SessionStart` フックで作業ディレクトリ名を `project.name` として自動付与すれば、複数プロジェクトの分離も一行で解決できる
- `claude_code.commit.count` や `claude_code.pull_request.count` などの組み込みメトリクスを追加設定なしでOpenObserveで可視化できる
- 記録されたデータをもとに改善ループを回すことで、Agentic Codingの質を高めていける

ぜひ自分のワークフローに組み込んで、エージェントとの協働を最適化してみてください。

[GitHubで編集を提案](https://github.com/UtakataKyosui/MyZenns/blob/main/articles/claude-code-with-otel.md)

8

4

8

4