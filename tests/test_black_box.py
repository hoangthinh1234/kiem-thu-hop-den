import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest

from black_box_tasks import (
    alternating_sum,
    days_in_month,
    gcd,
    is_prime,
    solve_quadratic,
    rectangle_area,
    rectangle_perimeter,
    sum_factorials,
)


@pytest.mark.parametrize("length,width,expected", [
    (5, 3, 16),
    (0.5, 2, 5),
    (1, 7, 16),
])
def test_rectangle_perimeter_valid_and_boundary(length, width, expected):
    assert rectangle_perimeter(length, width) == expected


def test_rectangle_perimeter_invalid_zero_length():
    with pytest.raises(ValueError):
        rectangle_perimeter(0, 3)


@pytest.mark.parametrize("length,width,expected", [
    (5, 3, 15),
    (0.5, 2, 1),
    (1, 7, 7),
])
def test_rectangle_area_valid_and_boundary(length, width, expected):
    assert rectangle_area(length, width) == expected


def test_rectangle_area_invalid_negative_width():
    with pytest.raises(ValueError):
        rectangle_area(5, -1)

@pytest.mark.parametrize("a,b,c,expected_type", [
    (1, -3, 2, "two_real_roots"),       # Δ > 0
    (1, 2, 1, "one_double_root"),       # Δ = 0
    (1, 0, 1, "no_real_roots"),          # Δ < 0
])
def test_quadratic_partitions(a, b, c, expected_type):
    result = solve_quadratic(a, b, c)
    assert result["type"] == expected_type


def test_quadratic_two_roots_values():
    roots = solve_quadratic(1, -3, 2)["roots"]
    assert sorted(roots) == pytest.approx([1, 2])


def test_quadratic_invalid_a_zero_boundary():
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 1)


@pytest.mark.parametrize("month,year,expected", [
    (1, 2025, 31),
    (4, 2025, 30),
    (2, 2024, 29),              # leap year
    (2, 2025, 28),
    (12, 2025, 31),             # upper boundary month
])
def test_days_in_month_partitions(month, year, expected):
    assert days_in_month(month, year) == expected


def test_days_in_month_invalid_month_zero():
    with pytest.raises(ValueError):
        days_in_month(0, 2025)


def test_days_in_month_invalid_month_13():
    with pytest.raises(ValueError):
        days_in_month(13, 2025)


def test_days_in_month_year_boundary():
    assert days_in_month(2, 1) == 28


@pytest.mark.parametrize("n,expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
])
def test_prime_partitions_and_boundaries(n, expected):
    assert is_prime(n) is expected


def test_prime_invalid_negative():
    with pytest.raises(ValueError):
        is_prime(-1)


def test_prime_invalid_non_integer():
    with pytest.raises(TypeError):
        is_prime(2.5)


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, -1),
    (3, 2),
    (4, -2),
    (10, -5),
])
def test_alternating_sum_partitions_and_boundary(n, expected):
    assert alternating_sum(n) == expected


def test_alternating_sum_invalid_zero():
    with pytest.raises(ValueError):
        alternating_sum(0)


def test_gcd_positive_numbers():
    assert gcd(24, 18) == 6


def test_gcd_zero_boundary():
    assert gcd(0, 9) == 9
    assert gcd(9, 0) == 9


def test_gcd_negative_numbers():
    assert gcd(-24, 18) == 6


def test_gcd_invalid_both_zero():
    with pytest.raises(ValueError):
        gcd(0, 0)


@pytest.mark.parametrize("n,expected", [
    (1, 1),
    (2, 3),
    (3, 9),
    (5, 153),
])
def test_sum_factorials_partitions(n, expected):
    assert sum_factorials(n) == expected


def test_sum_factorials_boundary_one():
    assert sum_factorials(1) == 1


def test_sum_factorials_invalid_zero():
    with pytest.raises(ValueError):
        sum_factorials(0)
