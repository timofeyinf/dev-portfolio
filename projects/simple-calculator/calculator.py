"""
Простой калькулятор с базовыми операциями
"""

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def power(base, exponent):
    """Возведение в степень (поддерживает отрицательные степени)"""
    if exponent >= 0:
        return base ** exponent
    else:
        return 1 / (base ** abs(exponent))

if __name__ == "__main__":
    # Пример использования
    print("Калькулятор запущен!")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
