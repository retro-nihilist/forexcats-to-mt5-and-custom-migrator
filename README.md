# ForexCats → MT5 и Custom Migrator

Автоматизированный ETL-пайплайн для извлечения, трансформации и загрузки (ETL) истории торгов клиентов из платформы ForexCats в MetaTrader 5 и проприетарные БД.

## Краткое описание
Этот проект предназначен для надёжной миграции клиентских торговых данных: он подключается к источнику (ForexCats), извлекает историю сделок и ордеров, выполняет необходимые преобразования и загружает результаты в MetaTrader 5 и/или в кастомную базу данных/архитектуру.

Типичный сценарий использования:
- миграция истории при переходе клиента на новую платформу;
- синхронизация архивов торговых данных;
- формирование исторических витрин для анализа и расчётов.

## Основные возможности
- Подключение к API ForexCats (экспорт истории и метаинформации).
- Преобразование форматов и нормализация торговых записей.
- Загрузка в MetaTrader 5 (через MT5 API/экспорт/import) и в кастомную БД.
- Конфигурируемые правила маппинга и трансформации.
- Логирование и контроль целостности миграции.
- Набор Jupyter-ноутбуков для анализа и проверки данных (exploratory / validation).

## Архитектура (высокоуровнево)
1. Источник: ForexCats API / экспорт.
2. ETL-слой:
   - Extract — получение сырых записей.
   - Transform — нормализация, обогащение, валидация, согласование временных зон, маппинг инструментов/символов.
   - Load — запись в MT5 и/или в целевую БД.
3. Мониторинг и логирование — отслеживание статуса и ошибок.
4. Тестирование и валидация — сравнительные отчёты до/после миграции.

## Рекомендуемая структура репозитория
(адаптируйте под фактические файлы)
- notebooks/ — Jupyter-ноутбуки (анализ, валидация)
- src/ — исходный код мигратора (Python)
- configs/ — примеры конфигураций (YAML/JSON)
- scripts/ — утилиты запуска
- docs/ — дополнительная документация
- tests/ — модульные и интеграционные тесты

## Требования
- Python 3.9+ (рекомендуется v3.10+)
- Библиотеки: requests, pyyaml, pandas, sqlalchemy (и др. по необходимости)
- Доступ к ForexCats API (ключи/учётные данные)
- Доступ/клиент для MT5 (API/контейнер/утилита)
- Доступ к целевой базе данных (credentials)

## Установка
1. Клонируйте репозиторий:
   git clone https://github.com/retro-nihilist/forexcats-to-mt5-and-custom-migrator.git
2. Перейдите в папку проекта и создайте виртуальное окружение:
   python -m venv .venv
   source .venv/bin/activate  # Linux / macOS
   .venv\Scripts\activate     # Windows
3. Установите зависимости:
   pip install -r requirements.txt

## Конфигурация
Проект конфигурируется через YAML/JSON файл. Пример `configs/example_config.yaml`:

```yaml
# configs/example_config.yaml
forexcats:
  api_base: "https://api.forexcats.example"
  api_key: "YOUR_FOREXCATS_API_KEY"
  date_from: "2020-01-01"
  date_to: "2021-01-01"

mt5:
  enabled: true
  host: "mt5-host.example"
  port: 443
  login: 123456
  password: "PASSWORD"

database:
  type: "postgresql"
  dsn: "postgresql://user:password@db-host:5432/forex_archive"

transform:
  timezone: "UTC"
  mapping_file: "configs/mapping.yaml"
  validate: true

logging:
  level: "INFO"
  path: "logs/migration.log"
