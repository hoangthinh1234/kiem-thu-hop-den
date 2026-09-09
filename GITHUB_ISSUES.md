# Nội dung tạo GitHub Issue

## Issue 1 – Thiết kế test case cho dữ liệu hợp lệ

**Title:** `Black-box testing – test cases for valid data`

**Body:**

### Mục tiêu
Xây dựng test case kiểm thử hộp đen cho 8 bài toán với dữ liệu hợp lệ.

### Kỹ thuật áp dụng
- Phân lớp tương đương (Equivalence Partitioning).
- Phân tích giá trị biên (Boundary Value Analysis).
- Kiểm tra kết quả đầu ra mong đợi dựa trên đặc tả bài toán.

### Phạm vi
1. Chu vi hình chữ nhật.
2. Diện tích hình chữ nhật.
3. Phương trình bậc hai với Δ > 0, Δ = 0, Δ < 0.
4. Số ngày trong tháng.
5. Kiểm tra số nguyên tố.
6. Tổng xen kẽ.
7. UCLN.
8. Tổng giai thừa.

### Tiêu chí hoàn thành
- Có danh sách test case cho dữ liệu hợp lệ.
- Có expected result.
- Đã chạy test và test hợp lệ đều PASS.
- Có commit liên kết với Issue này.

---

## Issue 2 – Thiết kế test case cho dữ liệu không hợp lệ / giá trị biên

**Title:** `Black-box testing – invalid and boundary data`

**Body:**

### Mục tiêu
Xây dựng test case cho dữ liệu không hợp lệ và giá trị biên để quan sát khả năng xử lý lỗi của chương trình.

### Ví dụ phạm vi
- length = 0 hoặc width < 0 đối với hình chữ nhật.
- Phương trình bậc hai với a = 0.
- month = 0 hoặc month = 13.
- year <= 0.
- n < 0 hoặc sai kiểu dữ liệu.
- n = 0 đối với bài yêu cầu n >= 1.
- gcd(0,0).

### Kỹ thuật áp dụng
- Phân lớp tương đương cho lớp dữ liệu không hợp lệ.
- Phân tích giá trị biên: ngay trước biên, tại biên và ngay sau biên.

### Tiêu chí hoàn thành
- Có ít nhất 1 trường hợp dữ liệu sai/không hợp lệ cho mỗi bài.
- Có test cho các mốc quan trọng.
- Chương trình xử lý lỗi bằng exception phù hợp.
- Test đều PASS.
- Có commit liên kết với Issue này.
