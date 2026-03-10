import os

files_to_rename = [
    ("/workspaces/profit-factory/保管庫/雑多なもの/ブログ教材/【最重要】月収10万円以上を達成する為の自立マインドセット動画講座.md",
     "/workspaces/profit-factory/保管庫/雑多なもの/ブログ教材/既読_【最重要】月収10万円以上を達成する為の自立マインドセット動画講座.md"),
    ("/workspaces/profit-factory/保管庫/雑多なもの/チャットGPT/タスク管理アプリ設計.md",
     "/workspaces/profit-factory/保管庫/雑多なもの/チャットGPT/既読_タスク管理アプリ設計.md"),
    ("/workspaces/profit-factory/保管庫/雑多なもの/ジェミニ/フリーランスプログラマーへのロードマップ.md",
     "/workspaces/profit-factory/保管庫/雑多なもの/ジェミニ/既読_フリーランスプログラマーへのロードマップ.md"),
]

for old, new in files_to_rename:
    try:
        os.rename(old, new)
        print(f"Renamed: {old} -> {new}")
    except Exception as e:
        print(f"Failed: {old} - {e}")