from calculator.core import Number, add, divide, multiply, subtract, power, modulo

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "^": power,
}


def _parse_number(token: str) -> Number:
    try:
        return int(token)
    except ValueError:
        return float(token)


def evaluate(expression: str) -> Number:
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError(f"Неверный формат выражения: {expression!r}")
    left, op, right = parts
    if op not in OPERATIONS:
        raise ValueError(f"Неизвестный оператор: {op!r}")
    return OPERATIONS[op](_parse_number(left), _parse_number(right))
