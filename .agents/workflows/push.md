---
description: ワークスペース全体をGitHubにバックアップとしてプッシュします（profit-factoryリポジトリ用）。
---
ワークスペース全体（/workspaces/profit-factory）の変更を自動的にコミットし、GitHubにプッシュ（アップロード）します。コンテナの完全バックアップを取るために使用します。

// turbo-all
1. ワークスペースのディレクトリに移動します。
```bash
cd /workspaces/profit-factory
```

2. 新規追加および変更されたすべてのファイルをGitのトラッキング対象としてステージングします。
```bash
git add .
```

3. 一括でコミットメッセージを生成してコミットします。
```bash
git commit -m "chore: auto backup push from workspace"
```

4. 現在の変更状態を、GitHubのメイン環境へプッシュします。
```bash
git push origin main
```
