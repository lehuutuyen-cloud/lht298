import os
import json
from datetime import datetime

# Cấu hình đường dẫn
PAGES_DIR = 'pages'
INDEX_FILE = 'index.json'

def generate_sitemap():
    library = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_pages": 0,
        "pages": []
    }

    # Kiểm tra nếu thư mục pages tồn tại
    if not os.path.exists(PAGES_DIR):
        print(f"Directory {PAGES_DIR} not found.")
        return

    # Quét từng thư mục con trong /pages/
    # sorted() giúp danh sách ổn định, không bị nhảy thứ tự mỗi lần chạy
    for page_folder in sorted(os.listdir(PAGES_DIR)):
        page_path = os.path.join(PAGES_DIR, page_folder)
        
        # Chỉ xử lý nếu là thư mục
        if os.path.isdir(page_path):
            page_data = {
                "id": page_folder,
                "info": {},
                "chapters": []
            }

            # 1. Đọc file metadata.json nếu có
            meta_path = os.path.join(page_path, 'metadata.json')
            if os.path.exists(meta_path):
                try:
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        page_data["info"] = json.load(f)
                except Exception as e:
                    print(f"Error reading metadata for {page_folder}: {e}")
            else:
                # Nếu không có metadata, tạo info mặc định từ tên thư mục
                page_data["info"] = {
                    "title": page_folder.replace('_', ' ').title(),
                    "id": page_folder
                }
            
            # 2. Quét các file nội dung (.txt hoặc .md)
            # Loại bỏ metadata.json và các file ẩn
            valid_extensions = ('.txt', '.md')
            
            for file in sorted(os.listdir(page_path)):
                if file.endswith(valid_extensions) and file != 'metadata.json':
                    page_data["chapters"].append({
                        "filename": file,
                        "path": f"{PAGES_DIR}/{page_folder}/{file}"
                    })
            
            # Chỉ thêm vào danh sách nếu thư mục có chứa chương hoặc metadata
            if page_data["chapters"] or page_data["info"]:
                library["pages"].append(page_data)

    library["total_pages"] = len(library["pages"])

    # Ghi ra file index.json
    try:
        with open(INDEX_FILE, 'w', encoding='utf-8') as f:
            json.dump(library, f, indent=2, ensure_ascii=False)
        print(f"Sitemap ({INDEX_FILE}) updated successfully with {library['total_pages']} items.")
    except Exception as e:
        print(f"Error writing index file: {e}")

if __name__ == "__main__":
    generate_sitemap()
