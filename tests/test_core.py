"""Unit-тесты базовых операций."""

import pytest

from calculator import add, divide, modulo, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 2.5) == 10


def test_divide():
    assert divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)



def test_power():
    assert power(2, 10) == 1024


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)
