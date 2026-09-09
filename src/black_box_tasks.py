"""Eight small programs for Black-box Testing Practical 03.

The functions validate their input domains so invalid test cases can be
observed explicitly during black-box testing.
"""

from __future__ import annotations

import math
from numbers import Real, Integral


def _require_real(value: Real, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} phải là số")


def _require_integer(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} phải là số nguyên")


def rectangle_perimeter(length: Real, width: Real) -> Real:
    """Return perimeter of a rectangle. Domain: length > 0, width > 0."""
    _require_real(length, "chiều dài")
    _require_real(width, "chiều rộng")
    if length <= 0 or width <= 0:
        raise ValueError("Chiều dài và chiều rộng phải > 0")
    return 2 * (length + width)


def rectangle_area(length: Real, width: Real) -> Real:
    """Return area of a rectangle. Domain: length > 0, width > 0."""
    _require_real(length, "chiều dài")
    _require_real(width, "chiều rộng")
    if length <= 0 or width <= 0:
        raise ValueError("Chiều dài và chiều rộng phải > 0")
    return length * width


def solve_quadratic(a: Real, b: Real, c: Real) -> dict:
    """Solve ax^2 + bx + c = 0 for real roots.

    Raises ValueError when a == 0 because the task is specifically a
    quadratic equation.
    """
    _require_real(a, "a")
    _require_real(b, "b")
    _require_real(c, "c")
    if a == 0:
        raise ValueError("a phải khác 0 để là phương trình bậc hai")

    delta = b * b - 4 * a * c
    eps = 1e-12
    if delta > eps:
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return {"type": "two_real_roots", "delta": delta, "roots": (root1, root2)}
    if abs(delta) <= eps:
        root = -b / (2 * a)
        return {"type": "one_double_root", "delta": 0.0, "roots": (root,)}
    return {"type": "no_real_roots", "delta": delta, "roots": ()}


def days_in_month(month: int, year: int) -> int:
    """Return number of days in month. Domain: month 1..12, year > 0."""
    _require_integer(month, "tháng")
    _require_integer(year, "năm")
    if not 1 <= month <= 12:
        raise ValueError("Tháng phải trong khoảng 1..12")
    if year <= 0:
        raise ValueError("Năm phải > 0")

    if month == 2:
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        return 29 if leap else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


def is_prime(n: int) -> bool:
    """Return whether n is prime. Domain: integer n >= 0; 0 and 1 are not prime."""
    _require_integer(n, "n")
    if n < 0:
        raise ValueError("n phải >= 0")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def alternating_sum(n: int) -> int:
    """Compute S = 1 - 2 + 3 - 4 + ... + n. Domain: n >= 1."""
    _require_integer(n, "n")
    if n < 1:
        raise ValueError("n phải >= 1")
    # Closed form: for even n=2k => -k; for odd n=2k+1 => k+1.
    return -(n // 2) if n % 2 == 0 else (n + 1) // 2


def gcd(a: int, b: int) -> int:
    """Return greatest common divisor of a and b. Both zero is invalid."""
    _require_integer(a, "a")
    _require_integer(b, "b")
    if a == 0 and b == 0:
        raise ValueError("a và b không được đồng thời bằng 0")
    return math.gcd(a, b)


def factorial(n: int) -> int:
    """Return n!. Domain: n >= 0."""
    _require_integer(n, "n")
    if n < 0:
        raise ValueError("n phải >= 0")
    return math.factorial(n)


def sum_factorials(n: int) -> int:
    """Compute S = 1! + 2! + ... + n!. Must use factorial(n)."""
    _require_integer(n, "n")
    if n < 1:
        raise ValueError("n phải >= 1")
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total
