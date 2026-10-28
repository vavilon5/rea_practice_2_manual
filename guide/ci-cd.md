# Процесс CI/CD

| Workflow | Файл | Когда запускается | Что делает |
|---|---|---|---|
| CI | `.github/workflows/main.yml` | push в любую ветку, PR в `main` | flake8, unit- и интеграционные тесты на Python 3.10/3.12/3.13, автослияние PR из `development` |
| Docs | `.github/workflows/docs.yml` | push в `main`, `development`, `release` | генерация API-документации `pdoc`, артефакт `docs-<ветка>`, публикация из `main` в `gh-pages` |
| Release | `.github/workflows/release.yml` | push тега `v*` | тесты, проверка версии, сборка пакета, GitHub Release |

## Ветки

- `main` — стабильная ветка.
- `development` — разработка новых функций. PR из `development` в `main` сливается автоматически после успешных `lint` и `test`.
- `release` — подготовка выпуска (версия, CHANGELOG). Выпуск фиксируется тегом `vX.Y.Z`.
