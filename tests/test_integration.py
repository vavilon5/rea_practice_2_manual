"""Интеграционные тесты: вычислитель выражений и CLI."""

import subprocess
import sys

import pytest

from calculator import __version__, evaluate
from calculator.__main__ import main


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("3 * 7", 21),
        ("8 / 2", 4.0),
        ("1.5 + 1", 2.5)
    ],
)
def test_evaluate(expression, expected):
    assert evaluate(expression) == expected


@pytest.mark.parametrize("expression", ["2 +", "2 & 3", "a + b"])
def test_evaluate_invalid(expression):
    with pytest.raises(ValueError):
        evaluate(expression)


def test_main_success(capsys):
    assert main(["6 * 7"]) == 0
    assert capsys.readouterr().out.strip() == "42"


def test_main_error(capsys):
    assert main(["1 / 0"]) == 1
    assert "Ошибка" in capsys.readouterr().err


def test_cli_subprocess():
    result = subprocess.run(
        [sys.executable, "-m", "calculator", "2 + 2"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout.strip() == "4"


def test_main_usage_shows_version(capsys):
    assert main([]) == 2
    assert __version__ in capsys.readouterr().err
