# lehuutuyen.com
## Tài liệu bối cảnh (context.txt) và các file content cho trang lehuutuyen.com.
Mục đích: lưu tất cả nội dung trang lehuutuyen.com để AI/automation đọc nhanh.

## Cấu trúc
- `/pages` : mỗi trang 1 file .txt (header metadata + nội dung nguyên văn)
- `/index.json` : sitemap tóm tắt (title, url, path, type, tags)
- `/meta` : tags, redirects, taxonomy

## Cách AI truy xuất (hướng dẫn ngắn)
1. Đọc `index.json` và sitemap để lấy danh sách file.
2. Mở file tương ứng trong `/pages`.
3. Parse header (dòng trước `---`) để lấy URL/type/tags.
4. Dùng body làm nguồn nội dung nguyên văn.

## Ghi chú cho con người
- Nếu chỉnh nội dung, update `LAST_UPDATED` ở header.
- Commit message mẫu: `content: update home.txt — chỉnh sửa CTA`
- Để thêm page mới: tạo file trong `/pages`, thêm mục vào `index.json`.

## Sitemap
lehuutuyen.com-content/
- ├─ README.md
- ├─ index.json            # (tổng mục lục, lightweight)
- ├─ pages/
- │  ├─ home.txt
- │  ├─ about.txt
- │  ├─ my-story.txt
- │  ├─ blog/
- │  │  ├─ index.txt       # danh mục blog
- │  │  ├─ 2025-01-01-post-title.txt
- │  ├─ landing-product-a.txt
- │  └─ faq.txt
- ├─ assets/               # ảnh, logo nếu cần
- ├─ meta/                 # optional: taxonomy, redirects
- │  └─ tags.json
- └─ CHANGELOG.md

## Liên hệ
- Owner: Lê Hữu Tuyến
- Website: http://lehuutuyen.com
