"""CLI demo for the eight Practical 03 problems."""

from __future__ import annotations

from black_box_tasks import (
    alternating_sum,
    days_in_month,
    factorial,
    gcd,
    is_prime,
    solve_quadratic,
    rectangle_area,
    rectangle_perimeter,
    sum_factorials,
)


def run() -> None:
    print("=== BÀI THỰC HÀNH 03 - KIỂM THỬ HỘP ĐEN ===")
    print("1. Tính chu vi hình chữ nhật")
    print("2. Tính diện tích hình chữ nhật")
    print("3. Giải phương trình bậc 2")
    print("4. Tính số ngày của một tháng")
    print("5. Kiểm tra n có phải số nguyên tố")
    print("6. Tính S = 1 - 2 + 3 - 4 + ... + n")
    print("7. Tìm UCLN của a và b")
    print("8. Tính S = 1! + 2! + 3! + ... + n!")
    print("0. Thoát")

    while True:
        try:
            choice = int(input("\nChọn bài [0-8]: "))
            if choice == 0:
                print("Kết thúc.")
                break
            if choice == 1:
                length = float(input("Chiều dài = "))
                width = float(input("Chiều rộng = "))
                print("Kết quả chu vi:", rectangle_perimeter(length, width))
            elif choice == 2:
                length = float(input("Chiều dài = "))
                width = float(input("Chiều rộng = "))
                print("Kết quả diện tích:", rectangle_area(length, width))
            elif choice == 3:
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
                print("Kết quả:", solve_quadratic(a, b, c))
            elif choice == 4:
                month = int(input("Tháng = "))
                year = int(input("Năm = "))
                print("Số ngày:", days_in_month(month, year))
            elif choice == 5:
                n = int(input("n = "))
                print("Là số nguyên tố:", is_prime(n))
            elif choice == 6:
                n = int(input("n = "))
                print("S =", alternating_sum(n))
            elif choice == 7:
                a = int(input("a = "))
                b = int(input("b = "))
                print("UCLN =", gcd(a, b))
            elif choice == 8:
                n = int(input("n = "))
                print("S =", sum_factorials(n))
            else:
                print("Vui lòng chọn từ 0 đến 8.")
        except (TypeError, ValueError) as exc:
            print("Dữ liệu không hợp lệ:", exc)


if __name__ == "__main__":
    run()
