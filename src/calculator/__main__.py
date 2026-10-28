import sys

from calculator import __version__
from calculator.expression import evaluate


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print(f"calculator {__version__}", file=sys.stderr)
        print('Использование: python -m calculator "<a> <op> <b>"', file=sys.stderr)
        return 2
    try:
        print(evaluate(args[0]))
    except (ValueError, ZeroDivisionError) as exc:
        print(f"Ошибка: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
