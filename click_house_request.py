# ch_client.py
# ------------------------------------------------------------
# Утилиты для работы с ClickHouse:
#  - создание клиента
#  - безопасные SELECT-запросы
#  - возврат данных в pandas.DataFrame
# ------------------------------------------------------------
import pandas as pd
from clickhouse_driver import Client
from read_dict_from_text_file import read_dict_from_text_file


# ============================================================
# ЗАГРУЗКА КОНФИГУРАЦИИ CLICKHOUSE
# ============================================================
LEVELS_UP = 1
CREDITS_FILE = "credits\\clickhouse.text"

ch_config = read_dict_from_text_file(LEVELS_UP, CREDITS_FILE)


# ============================================================
# СОЗДАНИЕ КЛИЕНТА CLICKHOUSE
# ============================================================
def create_ch_client():
    """
    Создаёт и возвращает ClickHouse Client
    """
    return Client(
        host=ch_config['host'],
        port=int(ch_config.get('port', 9000)),
        user=ch_config.get('user', 'default'),
        password=ch_config.get('password', ''),
        database=ch_config.get('database', 'default'),
        send_receive_timeout=300,
        connect_timeout=10
    )


# ============================================================
# ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# ============================================================

def list_to_str(lst, quotes=False):
    """
    Безопасное преобразование списка в строку для IN (...)
    """
    if not lst:
        return ''
    if quotes:
        return ",".join(f"'{x}'" for x in lst)
    return ",".join(map(str, lst))


# ============================================================
# ЧТЕНИЕ ДАННЫХ В pandas.DataFrame
# ============================================================

def pd_read_ch(
    query: str,
    params: dict | None = None,
    column_names: list[str] | None = None,
    max_memory_usage: int = 2_000_000_000,
    max_threads: int = 2
) -> pd.DataFrame:
    """
    Выполняет SELECT-запрос в ClickHouse и возвращает pandas.DataFrame

    :param query: SQL запрос
    :param params: параметры запроса
    :param column_names: явное указание имён колонок
    :param max_memory_usage: лимит памяти запроса (байты)
    :param max_threads: число потоков
    """

    client = create_ch_client()

    try:
        data, meta = client.execute(
            query,
            params=params,
            with_column_types=True,
            settings={
                "max_memory_usage": max_memory_usage,
                "max_threads": max_threads
            }
        )
    finally:
        client.disconnect()

    columns = column_names or [c[0] for c in meta]
    return pd.DataFrame(data, columns=columns)


# ============================================================
# ПОСТРОЧНОЕ ЧТЕНИЕ (БЕЗ ПЕРЕПОЛНЕНИЯ ПАМЯТИ)
# ============================================================

def pd_read_ch_iter(
    query: str,
    params: dict | None = None,
    chunk_size: int = 50_000,
    max_memory_usage: int = 1_000_000_000
):
    """
    Генератор DataFrame-чанков (стриминг)
    """

    client = create_ch_client()

    try:
        stream = client.execute_iter(
            query,
            params=params,
            with_column_types=True,
            settings={
                "max_memory_usage": max_memory_usage,
                "max_block_size": chunk_size
            }
        )

        header = next(stream)
        columns = [c[0] for c in header]

        chunk = []
        for row in stream:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield pd.DataFrame(chunk, columns=columns)
                chunk.clear()

        if chunk:
            yield pd.DataFrame(chunk, columns=columns)

    finally:
        client.disconnect()
