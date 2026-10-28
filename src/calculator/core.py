
Number = int | float


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def power(a: Number, b: Number) -> Number:
    return a**b


def modulo(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a % b
