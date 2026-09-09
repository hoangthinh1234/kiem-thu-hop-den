# Danh sách Test Case – Kiểm thử hộp đen

## Quy ước

- **EP (Equivalence Partitioning):** phân lớp tương đương.
- **BVA (Boundary Value Analysis):** phân tích giá trị biên.
- `PASS`: kết quả thực tế khớp expected.
- Lỗi đầu vào được coi là đúng khi chương trình trả về `ValueError`/`TypeError` đúng theo miền đầu vào đã định nghĩa.

## Bài 1 – Chu vi hình chữ nhật

| ID | Kỹ thuật | Đầu vào | Expected |
|---|---|---|---|
| TC01 | EP hợp lệ | length=5, width=3 | 16 |
| TC02 | EP hợp lệ | length=0.5, width=2 | 5 |
| TC03 | BVA hợp lệ | length=1, width=7 | 16 |
| TC04 | BVA không hợp lệ | length=0, width=3 | ValueError |

Phân lớp: `length > 0` và `width > 0` hợp lệ; một trong hai `<= 0` là không hợp lệ.

## Bài 2 – Diện tích hình chữ nhật

| ID | Kỹ thuật | Đầu vào | Expected |
|---|---|---|---|
| TC05 | EP hợp lệ | length=5, width=3 | 15 |
| TC06 | EP hợp lệ | length=0.5, width=2 | 1 |
| TC07 | BVA | length=1, width=7 | 7 |
| TC08 | BVA không hợp lệ | length=5, width=-1 | ValueError |

## Bài 3 – Phương trình bậc hai

Miền chính: `a != 0`.

| ID | Kỹ thuật | a,b,c | Expected |
|---|---|---|---|
| TC09 | EP Δ > 0 | 1,-3,2 | 2 nghiệm thực: 1 và 2 |
| TC10 | EP Δ = 0 | 1,2,1 | 1 nghiệm kép: -1 |
| TC11 | EP Δ < 0 | 1,0,1 | Không có nghiệm thực |
| TC12 | BVA không hợp lệ | 0,2,1 | ValueError |

## Bài 4 – Số ngày trong tháng

| ID | Kỹ thuật | month, year | Expected |
|---|---|---|---|
| TC13 | EP 31 ngày | 1,2025 | 31 |
| TC14 | EP 30 ngày | 4,2025 | 30 |
| TC15 | EP năm nhuận | 2,2024 | 29 |
| TC16 | EP không nhuận | 2,2025 | 28 |
| TC17 | BVA biên trên hợp lệ | 12,2025 | 31 |
| TC18 | BVA không hợp lệ | 0,2025 | ValueError |
| TC19 | BVA không hợp lệ | 13,2025 | ValueError |

## Bài 5 – Số nguyên tố

| ID | Kỹ thuật | n | Expected |
|---|---|---:|---|
| TC20 | BVA | 0 | False |
| TC21 | BVA | 1 | False |
| TC22 | BVA | 2 | True |
| TC23 | EP | 3 | True |
| TC24 | EP | 4 | False |
| TC25 | EP | 17 | True |
| TC26 | Dữ liệu không hợp lệ | -1 | ValueError |
| TC27 | Dữ liệu không hợp lệ | 2.5 | TypeError |

## Bài 6 – Tổng xen kẽ

| ID | Kỹ thuật | n | Expected |
|---|---|---:|---:|
| TC28 | BVA | 1 | 1 |
| TC29 | BVA | 2 | -1 |
| TC30 | EP | 3 | 2 |
| TC31 | EP | 4 | -2 |
| TC32 | EP | 10 | -5 |
| TC33 | BVA không hợp lệ | 0 | ValueError |

## Bài 7 – UCLN

| ID | Kỹ thuật | a,b | Expected |
|---|---|---|---|
| TC34 | EP số dương | 24,18 | 6 |
| TC35 | BVA | 0,9 | 9 |
| TC36 | BVA | 9,0 | 9 |
| TC37 | EP số âm | -24,18 | 6 |
| TC38 | BVA không hợp lệ | 0,0 | ValueError |

## Bài 8 – Tổng giai thừa

| ID | Kỹ thuật | n | Expected |
|---|---|---:|---:|
| TC39 | BVA | 1 | 1 |
| TC40 | EP | 2 | 3 |
| TC41 | EP | 3 | 9 |
| TC42 | EP | 5 | 153 |
| TC43 | BVA không hợp lệ | 0 | ValueError |

## Ghi chú

Đây là **black-box test**: expected được xác định từ đặc tả toán học và miền dữ liệu, không phụ thuộc vào cách cài đặt bên trong. Bộ test có cả dữ liệu hợp lệ, dữ liệu không hợp lệ và các giá trị biên.

## Issue #1 - Valid Data Test Cases

Đã hoàn thành thiết kế và kiểm thử các test case với dữ liệu hợp lệ
cho 8 bài toán bằng phương pháp Phân lớp tương đương (EP) và
Phân tích giá trị biên (BVA).

Kết quả: toàn bộ test case hợp lệ đã PASS.

## Issue #2 - Invalid and Boundary Test Cases

Đã hoàn thành thiết kế và kiểm thử các test case với dữ liệu
không hợp lệ và các trường hợp dữ liệu biên cho 8 bài toán.

Các trường hợp được kiểm thử gồm:
- Giá trị bằng 0.
- Giá trị âm.
- Giá trị vượt giới hạn.
- Tháng = 0 và tháng = 13.
- a = 0 trong phương trình bậc hai.
- n = 0 trong bài kiểm tra số nguyên tố.
- n = 0 trong bài tổng xen kẽ.
- UCLN(0,0).
- n = 0 trong bài tổng giai thừa.

Kết quả: chương trình xử lý dữ liệu không hợp lệ theo miền đầu vào
đã xác định và các test case đều PASS.