"""
Тесты для простого калькулятора
"""
import pytest
from calculator import add, subtract, multiply, divide, power

def test_add():
    """Тест сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    """Тест вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Тест умножения"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    """Тест деления"""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    """Тест деления на ноль"""
    with pytest.raises(ValueError, match="На ноль делить нельзя!"):
        divide(10, 0)

def test_power():
    """Тест возведения в степень"""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9

if __name__ == "__main__":
    pytest.main([__file__])
