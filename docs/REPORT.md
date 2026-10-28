# Отчёт по практической работе: CI/CD с GitHub Actions

Репозиторий: <https://github.com/vavilon5/rea_practice_2>  
Итоговая версия: **1.1.0** (тег [`v1.1.0`](https://github.com/vavilon5/rea_practice_2/releases/tag/v1.1.0))

## 1. Проект и тесты

Python-пакет `calculator` (`src/calculator`): арифметические операции, вычислитель выражений `evaluate` и CLI `python -m calculator "2 + 3"`.

- Unit-тесты: `tests/test_core.py` — операции `add`, `subtract`, `multiply`, `divide`, `power`, `modulo`.
- Интеграционные тесты: `tests/test_integration.py` — `evaluate`, функция `main` и запуск CLI отдельным процессом.
- Doctest в `src/calculator/expression.py`.

Локальный запуск: `pip install -e . -r requirements-dev.txt && pytest` — 23 теста проходят.

## 2. Настройка CI

| Workflow | Файл | Триггер | Задачи |
|---|---|---|---|
| CI | `.github/workflows/main.yml` | push в **любую** ветку, PR в `main`, вручную | `lint` (flake8), `test` на Python 3.10/3.12/3.13 с покрытием, `automerge` |
| Docs | `.github/workflows/docs.yml` | push в `main`, `development`, `release` | генерация API-документации `pdoc`, артефакт `docs-<ветка>`, публикация из `main` в `gh-pages` |
| Release | `.github/workflows/release.yml` | push тега `v*` | тесты, проверка совпадения версии и тега, сборка пакета, GitHub Release |

CI запускается автоматически при каждом коммите в любую ветку (`branches: ["**"]`).

## 3. Ход работы

1. В `main` добавлены проект, тесты, workflow и документация (`040982f`) — CI и Docs прошли.
2. Создана ветка `development`, в ней реализована новая функция — операции `^` (степень) и `%` (остаток) с тестами (`fc9cb8c`). CI на `development` прошёл.
3. Создан [PR #1](https://github.com/vavilon5/rea_practice_2/pull/1) `development → main`. CI запустился на событии `pull_request`, после успешных `lint` и `test` задача `automerge` слила PR (`0463b51`) и запустила CI и Docs на `main`.
4. Создана ветка `release`: версия поднята до 1.1.0, обновлён `CHANGELOG.md`, CLI показывает версию (`1e87492`). CI на `release` прошёл.
5. `release` влита в `main`, создан и опубликован тег `v1.1.0`. Workflow Release собрал пакет и создал [GitHub Release v1.1.0](https://github.com/vavilon5/rea_practice_2/releases/tag/v1.1.0) с файлами `calculator-1.1.0-py3-none-any.whl` и `calculator-1.1.0.tar.gz`.
6. Документация (`README.md`, `docs/`, API-справка из docstring) автоматически пересобирается на каждый push и публикуется в ветку `gh-pages`. В ней по одному коммиту на каждое обновление `main`; файл `BUILD_INFO.txt` содержит хеш и время сборки.

## 4. Запущенные workflow (вкладка Actions)

| Workflow | Ветка/тег | Событие | Коммит | Статус | Время (UTC) | Лог |
|---|---|---|---|---|---|---|
| CI #1 | `main` | push | `040982f` | ✅ success | 2026-10-28 11:23 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40679578503) |
| Docs #1 | `main` | push | `040982f` | ✅ success | 2026-10-28 11:23 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40679578643) |
| CI #2 | `development` | push | `fc9cb8c` | ✅ success | 2026-10-28 11:24 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40679717918) |
| Docs #2 | `development` | push | `fc9cb8c` | ✅ success | 2026-10-28 11:24 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40679717986) |
| CI #3 | `development` | pull_request | `fc9cb8c` | ✅ success | 2026-10-28 11:27 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680150696) |
| CI #4 | `main` | workflow_dispatch | `0463b51` | ✅ success | 2026-10-28 11:28 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680200245) |
| Docs #3 | `main` | workflow_dispatch | `0463b51` | ✅ success | 2026-10-28 11:28 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680203446) |
| CI #5 | `release` | push | `1e87492` | ✅ success | 2026-10-28 11:28 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680258067) |
| Docs #4 | `release` | push | `1e87492` | ✅ success | 2026-10-28 11:28 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680258086) |
| Docs #5 | `main` | push | `1e87492` | ✅ success | 2026-10-28 11:29 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680362928) |
| CI #6 | `main` | push | `1e87492` | ✅ success | 2026-10-28 11:29 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680362967) |
| Release #1 | `v1.1.0` | push | `1e87492` | ✅ success | 2026-10-28 11:29 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680368814) |
| Docs #6 | `development` | push | `1e87492` | ✅ success | 2026-10-28 11:29 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680376294) |
| CI #7 | `development` | push | `1e87492` | ✅ success | 2026-10-28 11:29 | [лог](https://github.com/vavilon5/rea_practice_2/actions/runs/40680376343) |

## 5. Логи шагов (CI, событие pull_request для PR #1)

- **lint**: checkout → setup-python → `pip install flake8` → `flake8` — success
- **test (3.10 / 3.12 / 3.13)**: checkout → setup-python → Install dependencies → Unit and integration tests — success
- **automerge**: Merge pull request → Run CI and docs on main — success

## 6. Итог

Все workflow завершились успешно. Изменения из `development` влиты в `main` автоматически после прохождения тестов, выпущена версия 1.1.0, документация обновляется автоматически при каждом изменении кода.
