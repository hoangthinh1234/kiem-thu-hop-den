# Bài thực hành 03 – Kiểm thử hộp đen

**Môn:** Đánh giá và kiểm định chất lượng phần mềm  
**Định hướng:** Kiểm thử hộp đen bằng phân lớp tương đương và phân tích giá trị biên.

## 1. Nội dung bài

Chương trình gồm 8 bài theo đề giảng viên:

1. Tính chu vi hình chữ nhật.
2. Tính diện tích hình chữ nhật.
3. Giải phương trình bậc hai.
4. Tính số ngày của một tháng.
5. Kiểm tra n có phải số nguyên tố.
6. Tính S = 1 - 2 + 3 - 4 + ... + n.
7. Tìm UCLN của a và b.
8. Tính S = 1! + 2! + 3! + ... + n!, trong đó dùng hàm `factorial`.

## 2. Cấu trúc thư mục

```text
black-box-testing-bt03/
├── src/
│   ├── black_box_tasks.py
│   └── main.py
├── tests/
│   └── test_black_box.py
├── README.md
├── TEST_CASES.md
├── TEST_RESULTS.txt
├── GITHUB_ISSUES.md
├── CODEX_PROMPT.md
├── requirements.txt
└── .gitignore
```

## 3. Cách chạy

### Windows / Linux / Ubuntu

```bash
python -m venv .venv
```

Linux/Ubuntu:
```bash
source .venv/bin/activate
```

Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Cài thư viện:

```bash
pip install -r requirements.txt
```

Chạy chương trình demo:

```bash
PYTHONPATH=src python src/main.py
```

Trên Windows nếu lệnh trên không tiện dùng:

```powershell
$env:PYTHONPATH="src"
python src/main.py
```

Chạy toàn bộ kiểm thử:

```bash
pytest -q
```

## 4. Cách áp dụng kiểm thử hộp đen

Không dựa vào mã nguồn để sinh expected result. Test case được xây dựng từ yêu cầu đầu vào/đầu ra của từng bài:

- **Phân lớp tương đương:** chia miền dữ liệu thành nhóm hợp lệ/không hợp lệ có cách xử lý giống nhau.
- **Giá trị biên:** kiểm tra sát các mốc như 0, 1, 12, 13, n=1, n=2, a=0, Δ=0.
- **Dữ liệu hợp lệ:** đại diện cho các nhóm đầu vào hợp lệ.
- **Dữ liệu không hợp lệ:** ít nhất một trường hợp cho mỗi bài; nhiều bài có thêm trường hợp biên không hợp lệ.

Chi tiết test case nằm trong `TEST_CASES.md`.

## 5. Hai GitHub Issue cần tạo

### Issue 1 – Dữ liệu hợp lệ

Dùng nội dung trong `GITHUB_ISSUES.md`, phần **Issue 1**. Commit đề xuất:

```bash
git add src tests README.md TEST_CASES.md CODEX_PROMPT.md requirements.txt
 git commit -m "test: add black-box test cases for valid data"
```

### Issue 2 – Dữ liệu không hợp lệ / giá trị biên

Dùng nội dung trong `GITHUB_ISSUES.md`, phần **Issue 2**. Sau khi hoàn thành:

```bash
git add .
git commit -m "test: add invalid and boundary black-box tests"
```

Sau đó push lên GitHub và đóng từng Issue bằng commit tương ứng.

