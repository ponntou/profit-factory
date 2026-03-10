import json
import os
import urllib.request
import urllib.parse

def main():
    json_path = "/home/vscode/.gemini/antigravity/brain/d15b113b-0d45-4c92-b8ea-45a53aebd1e5/.system_generated/steps/762/output.txt"
    target_dir = "/workspaces/profit-factory/保管庫/雑多なもの/Clippings"
    
    os.makedirs(target_dir, exist_ok=True)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        if item.get("type") == "file" and "download_url" in item:
            file_name = item["name"]
            download_url = item["download_url"]
            target_path = os.path.join(target_dir, file_name)
            
            print(f"Downloading: {file_name}")
            req = urllib.request.Request(download_url)
            # Add basic user agent just in case
            req.add_header('User-Agent', 'Mozilla/5.0')
            try:
                with urllib.request.urlopen(req) as response, open(target_path, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {file_name}: {e}")

if __name__ == "__main__":
    main()