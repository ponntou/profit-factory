---
description: GitHubから最新の変更をコンテナにプルし、競合を自動解決または通知します（profit-factoryリポジトリ用）。
---
ワークスペース全体（/workspaces/profit-factory）を対象に、GitHubから最新の状態をプルします。
また、コンテナ内で編集中のファイルがある場合（未コミットの変更）は、一時退避（stash）してプルを行ってから戻します。

// turbo-all
1. ワークスペースのディレクトリに移動します。
```bash
cd /workspaces/profit-factory
```

2. 念のためコンテナ内の変更を一時退避します。
```bash
git stash
```

3. 変更をコミットしてマージするためにプルします。
```bash
git pull origin main
```

4. 退避していた変更を元に戻します。
```bash
git stash pop
```

5. もしここで `CONFLICT` (競合) の文字が出た場合は、AI（アンチグラビティ）が内容を確認し、差分を統合して解決します。
