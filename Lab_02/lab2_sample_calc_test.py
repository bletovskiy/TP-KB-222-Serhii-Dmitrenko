from lab2_sample_calc import add
from lab2_sample_calc import mul

def test_add():
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    assert add(4, 2) == 6

def test_mul_positive_both():
    assert mul(2, 2) == 4
    assert mul(3, 2) == 6
    assert mul(4, 2) == 8

def test_mul_positive_and_negative():
    assert mul(2, -2) == -4
    assert mul(-3, 2) == -6
    assert mul(4, -2) == -8

def test_mul_negative_both():
    assert mul(-2, -2) == 4
    assert mul(-3, -2) == 6
    assert mul(-4, -2) == 8