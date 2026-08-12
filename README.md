# Трекер полезных привычек

API-сервис для формирования полезных привычек по принципам книги
"Атомные привычки": пользователь создаёт привычку, задаёт периодичность
и время выполнения, а сервис сам присылает напоминание в Telegram в
нужный момент.

## Возможности

- CRUD для привычек: действие, место, время, периодичность
- Разделение на полезные и приятные привычки, связка полезной с приятной как вознаграждением
- Публичные и приватные привычки — публичные видны другим пользователям
- Валидация данных на уровне API (сериализаторы DRF)
- Напоминания в заданное время через Telegram-бота (Celery + Celery Beat)
- Регистрация и авторизация пользователей
- Документация API: Swagger (`/swagger/`) и ReDoc (`/redoc/`)

## Стек

Python 3.11 · Django · Django REST Framework · PostgreSQL 16 · Celery + Celery Beat · Redis 7.4 · Docker / docker-compose · GitHub Actions

## Тестирование

Тесты Django, реальное покрытие — **80%**.

    docker compose exec web poetry run pytest --cov

## Быстрый старт

Создайте `.env` в корне проекта:

    POSTGRES_DB=
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    DATABASE_HOST=
    DATABASE_PORT=
    EMAIL_HOST=
    EMAIL_PORT=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    EMAIL_USE_TLS=True
    EMAIL_SENDER=
    EMAIL_USE_SSL=False

Соберите и запустите сервисы:

    docker-compose up --build

API будет доступен на `http://localhost:8000`, документация — на `http://localhost:8000/swagger/` или `/redoc/`.

## Архитектура

- **web** — Django + DRF, порт 8000, запускается после `db`
- **db** — PostgreSQL 16, данные в томе `postgres_data`
- **celery** — фоновые задачи (отправка напоминаний), зависит от `db` и `redis`
- **celery-beat** — планировщик периодических задач
- **redis** — брокер и бэкенд для Celery, порт 6379

## CI/CD

GitHub Actions запускается на каждый `push` и последовательно выполняет:

1. **lint** — flake8
2. **test** — прогон тестов Django через Poetry (`SECRET_KEY` берётся из GitHub Secrets)
3. **copy_files_in_server** — синхронизация файлов на сервер по SSH через rsync (только после успешных тестов)
4. **run_server** — пересборка и перезапуск контейнеров на сервере (`docker compose up --build`)

Требуемые секреты репозитория: `SECRET_KEY`, `DOCKER_HUB_USERNAME`, `DOCKER_HUB_ACCESS_TOKEN`, `SSH_KEY`, `SSH_USER`, `SERVER_IP`, `DEPLOY_DIR`.