Cписок всех классов и функций, содержащихся в библиотеках, с описанием их назначения и  перечнем аргументов.

### 1. Библиотека `click_house_request.py`
*   **`create_ch_client()`** — Создает и возвращает настроенный клиент ClickHouse, используя глобальную конфигурацию `ch_config`.
*   **`list_to_str(lst, quotes=False)`** — Преобразует список в строку с разделителем-запятой для использования в SQL-запросах (например, в операторе `IN (...)`). Аргумент `quotes=True` добавляет одинарные кавычки к каждому элементу.
*   **`pd_read_ch(query, params=None, column_names=None, max_memory_usage=2_000_000_000, max_threads=2)`** — Выполняет SELECT-запрос к ClickHouse и возвращает результат в виде `pandas.DataFrame`. Позволяет ограничивать использование памяти и количество потоков.
*   **`pd_read_ch_iter(query, params=None, chunk_size=50_000, max_memory_usage=1_000_000_000)`** — Генератор, который выполняет запрос и возвращает данные по частям (чанками), предотвращая переполнение оперативной памяти при работе с большими объемами данных.

### 2. Библиотека `config_loader.py`
*   **`load_config()`** — Определяет рабочую директорию проекта и его родительскую папку для корректной настройки путей.
*   **`setup_libraries(directories)`** — Добавляет путь к папке с библиотеками (извлекаемый из переданного словаря `directories`) в `sys.path` для возможности их импорта.
*   **`import_dynamic_functions(libraries_path)`** — Определяет путь к файлу динамического импорта функций.

### 3. Библиотека `dynamic_import_functions.py`
*   **`import_functions(modules: Dict[str, List[str]])`** — Динамически загружает указанные функции из файлов, пути к которым прописаны в словаре `modules`. Возвращает словарь ссылок на импортированные функции.
*   **`print_import_function_info(modules_to_import, imported)`** — Выводит в консоль подробную информацию обо всех динамически импортированных функциях и их параметрах.
*   **`print_function_info(module_name, function_name, function)`** — Внутренняя вспомогательная функция, использующая модуль `inspect` для анализа и вывода сигнатуры конкретной функции.

### 4. Библиотека `formatting_transactions.py`
*   **`format_balance_trans(df)`** — Форматирует таблицу балансовых операций, преобразуя колонку `deposit_date` в тип datetime.
*   **`format_trade_trans(df)`** — Приводит торговые транзакции к единому стандарту: заменяет типы ордеров BUY/SELL на числовые коды (0/1), устанавливает типы данных и округляет лоты.
*   **`search_cyrillic_characters(symbols_to_create_df)`** — Ищет кириллические символы в названиях инструментов в предоставленном DataFrame.
*   **`search_prohibited_characters(symbols_to_create_df)`** — Выполняет поиск запрещенных специальных символов в строках данных.
*   **`replacing_prohibited_characters(symbols_to_create_df)`** — Заменяет найденные запрещенные спецсимволы на нижнее подчеркивание `_`.
*   **`crm_symbol_tuple(statement_df)`** — Извлекает уникальные ID инструментов и их названия из стейтмента, возвращая кортеж ID.
*   **`currency_counts_def(statement_df, symbols_to_create_df)`** — Анализирует частоту появления инструментов в истории и удаляет дубликаты спецификаций, оставляя наиболее часто используемые.
*   **`statement_format(merged_df)`** — Выбирает и упорядочивает определенный набор колонок для финального формирования CSV-отчета стейтмента.

### 5. Библиотека `mt5_api.py`
*   **`mt_5_manager()`** — Возвращает ссылку на модуль `MT5Manager`.
*   **`mt5admin()`** — Создает и возвращает глобальный объект `AdminAPI` для администрирования сервера MT5.
*   **`mt5manager()`** — Создает и возвращает глобальный объект `ManagerAPI` для управления сервером.
*   **`admin_connect(credits_list=credits_dict_mt5manager)`** — Устанавливает соединение с сервером через AdminAPI, используя переданные учетные данные.
*   **`manager_connect(credits_list=credits_dict_mt5manager, pump_mode=0)`** — Устанавливает соединение через ManagerAPI с возможностью включения режима получения обновлений (pump mode).
*   **`admin_disconnect(admin_connect)`** — Разрывает соединение AdminAPI с сервером.
*   **`manager_disconnect(manager_connect)`** — Разрывает соединение ManagerAPI с сервером.
*   **`admin_connect_with_control(admin=None)`** — Проверяет наличие старого соединения, при необходимости закрывает его и устанавливает новое подключение для администратора.
*   **`admin_disconnect_with_control(admin)`** — Безопасно закрывает соединение администратора и удаляет объект интерфейса.
*   **`manager_connect_with_control(manager=None, pump_mode=None)`** — Проверяет статус и устанавливает новое соединение для менеджера с обработкой существующих сессий.
*   **`manager_disconnect_with_control(manager)`** — Безопасно завершает работу менеджера с сервером.
*   **`symbol_array_attributes(symbol_array, attributes, attributes_last_tick)`** — Формирует DataFrame с характеристиками торговых инструментов на основе массива объектов MT5.
*   **`balance_deal(user_login, balance_transactions, deal_action, comment, Description_action)`** — Проводит балансовую операцию на сервере с механизмом повторных попыток при сетевых сбоях.
*   **`process_deal(user_login, balance_transactions, deal_action, comment)`** — Осуществляет вызов метода проведения балансовой сделки через интерфейс менеджера.
*   **`balance_0(acc_set, summ0, date0, Description_action)`** — Выполняет массовое пополнение или списание средств (коррекцию) для группы счетов на указанную дату.
*   **`getting_array_trading_instruments(symbols_list="*")`** — Запрашивает с сервера массив конфигураций торговых инструментов по заданной маске.
*   **`symbol_update_batch(symbol_array)`** — Пакетно обновляет настройки торговых инструментов на сервере MT5.
*   **`last_error_id(error_mt5)`** — Парсит строку ошибки MT5 для извлечения числового кода последней ошибки.
*   **`creating_position(Description_action, deal, MT5Manager)`** — Пытается открыть торговую позицию на сервере, используя объект сделки, с обработкой ошибок и задержками.
*   **`positioncheck_and_positionfix(acc_set)`** — Проверяет корректность позиций по списку счетов, выявляя несоответствия, недостающие или лишние позиции.
*   **`mt5_connect_with_control(admin, manager, return_admin=False, return_manager=False, pump_mode=False)`** — Универсальная функция для управления подключением обоих типов интерфейсов одновременно.
*   **`mt5_disconnect_with_control(admin, manager, return_admin=False, return_manager=False)`** — Универсальная функция для одновременного отключения администратора и менеджера.
*   **`mt5_error(Description_action)`** — Вспомогательная функция для вывода подробной информации о последней ошибке API.

### 6. Библиотека `project_config.py`
*   **Класс `ProjectConfig`** — Обеспечивает централизованное управление путями к папкам проекта (логи, входные данные, временные файлы) и автоматизирует их создание.

project_config.py
══════════════════════════════════════════════════════════════

    Описание:
        Модуль project_paths.py содержит класс ProjectConfig, который 
        отвечает за централизованное управление структурой директорий 
        проекта. Он автоматически определяет иерархию папок и создаёт 
        все необходимые директории для корректной работы приложения.

    Основные возможности
    ═════════════════════

    • Автоматическое определение уровней проекта:
        
        • file_dir          — директория текущего скрипта
        • sub_project_dir   — директория субпроекта
        • project_dir       — корневая директория проекта
        • parent_dir        — родительская директория (для общих библиотек)

    • Автоматическое создание и проверка всех необходимых папок:

        Input Data (входные данные):
        • input_data/
            ├── input_log_data/     — исходные логи
            ├── input_temp_data/    — временные входные данные
            └── input_samples/      — примеры и сэмплы

        Output Data (результаты работы):
        • output_data/
            ├── output_log_data/    — выходные логи и результаты
            └── output_temp_data/   — временные выходные файлы

        Дополнительно:
        • data_set/             — файлы постоянных конфигураций и датасетов

    Дополнительные функции
    ═══════════════════════
    • Автоматическое добавление папки libraries_py в sys.path
    • Удобные свойства: .input_data и .output_data

### 7. Библиотека `read_dict_from_text_file.py`
*   **`read_dict_from_text_file(levels_up, file_relative_path)`** — Считывает текстовый файл, интерпретирует его содержимое как словарь Python и возвращает объект словаря.

### 8. Библиотека `sed_array_lib.py`
*   **`positions_in_array(array, values_to_find)`** — Ищет координаты заданных значений в двумерном массиве и возвращает их в виде словаря.
*   **`get_column_values(array, column_index)`** — Извлекает данные из указанного столбца структурированного массива NumPy.
*   **`np_set_printoptions(name, array, num, thres_hold=10)`** — Настраивает параметры вывода массивов в консоль и печатает содержимое массива.
*   **`sum_columns_by_indices(array, indices)`** — Подсчитывает сумму значений в указанных колонках числового массива или списка кортежей.
*   **`array_to_dataframe_with_multiline_headers(array)`** — Преобразует структурированный массив в DataFrame, формируя заголовки из имен полей и типов данных.
*   **`array_to_dataframe(array)`** — Стандартное преобразование структурированного массива NumPy в таблицу `pandas.DataFrame`.
*   **`objects_to_dataframe(objects_list, pd)`** — Формирует DataFrame на основе списка однотипных Python-объектов, используя их атрибуты как названия столбцов.
*   **`move_column(df, list_col_name, add_list_col_name=False, new_position=0, new_position_step=0)`** — Позволяет создавать новые пустые столбцы и перемещать их (или существующие) в указанное место в таблице.
*   **`array_element_attributes(array, e)`** — Перебирает и выводит все доступные атрибуты и их значения для конкретного элемента массива.

### 9. Библиотеки `sql_request.py`, `sql_request_2.py`, `sql_request_3.py`
*   **`pd_read_sql(query, file_relative_path, levels_up, params=None)`** — Выполняет SQL-запрос к БД MySQL и возвращает DataFrame. Использует файл для получения учетных данных.
*   **`load_mysql_tab(sql_tab, cred, levels_up=1)`** — Загружает все данные (SELECT *) из указанной таблицы MySQL напрямую в DataFrame.
*   **`get_sql_tab(symbols_sql_tab, file_relative_path, levels_up=1, sep=";")`** — Загружает данные из таблицы, используя разделитель для формирования запроса.
*   **`create_engine_def()`** — Вспомогательная функция для создания движка SQLAlchemy (версия в `sql_request.py`).

### 10. Библиотека `update_swop_open_position.py`
*   **`update_swop_open_position(account_id, deals_swap, deal_id, manager, MT5Manager, print_on=False)`** — Устанавливает новое значение свопа для открытой позиции по ID сделки на стороне сервера.

### 11. Библиотека `yar_sed_general_lib.py`
*   **`np_set_printoptions(name, array, num, threw_hold=10, if_elements_nan=0)`** — Настраивает отображение NumPy массивов с заданным порогом строк.
*   **`df_array_symbols(array_symbols)`** — Преобразует список объектов конфигурации символов MT5 в DataFrame, сохраняя результат в CSV.
*   **`pd_set_option(name_df, df, rows=10, columns=None, min_rows=None, width=100)`** — Устанавливает временные лимиты отображения строк/столбцов и красиво выводит таблицу в консоль.
*   **Класс `CSVLoader`** — Обеспечивает загрузку данных из CSV в DataFrame с контролем кодировок.
    *   **`__init__(self, file_path, delimiter=';', encoding='utf-8', df_name='dataframe')`** — Инициализирует загрузчик.
    *   **`load_data(self)`** — Выполняет чтение файла.
*   **`delete_rows_by_condition(df, column, value)`** — Удаляет строки из таблицы, где значение в колонке равно заданному (поддерживает списки).
*   **`df_to_csv(df, csv_file_path)`** — Сохраняет DataFrame в CSV и выводит абсолютный путь к файлу.
*   **`comparison_sets(set1, set2)`** — Выводит информацию о пересечении и уникальных элементах двух множеств.
*   **`find_intersecting_lists(lists, list_names, save_csv=False)`** — Ищет общие элементы в нескольких списках и выводит статистику.
*   **`list_print(lst, label=None, limit=10)`** — Печатает длину списка и первые элементы (до лимита).
*   **`int_list_to_csv_file(data_list, short_file_path, text)`** — Сохраняет список целых чисел в файл одной строкой через запятую.
*   **`load_account_list(file_path)`** — Загружает идентификаторы из файла и возвращает их в виде списка `int`.
*   **`columns_name_suffix(df, suffix)`** — Массово добавляет строку-суффикс ко всем названиям колонок таблицы.
*   **`file_name_with_time(file_name, short_file_path="", time_in_name=True)`** — Генерирует имя файла, опционально добавляя к нему текущую дату и время.
*   **`int_to_str_csv(int_list, short_file_path, file_name, time_in_name=True, sort=False)`** — Формирует CSV-строку из списка чисел и сохраняет её в файл с временной меткой.
*   **`get_random_three_digits()`** — Возвращает случайное число от 100 до 999.
*   **`time_str_to_unix_time_2(time_str)`** — Конвертирует объект Timestamp в формат Unix UTC (без учета локальных поясов).
*   **`move_column(df, list_col_name, add_list_col_name=False, new_position=0, new_position_step=1, print_info=False)`** — Расширенная версия функции для манипуляции положением столбцов.
*   **`save_dict_to_json(dict_data, short_file_path, file_name, time_in_name=True)`** — Записывает словарь в JSON-файл с форматированием.
*   **`save_dict_data_log_work_file(dict_data, file_name, directory_data_temp_files, directory_data_log_files)`** — Сохраняет словарь в формате JSON одновременно в рабочую папку и папку логов.
*   **`save_int_list_data_log_work_file(int_list, file_name, directory_data_temp_files, directory_data_log_files)`** — Дублирует сохранение числового списка в две папки (temp и log).
*   **`save_data_log_work_file(df, file_name, directory_data_temp_files, directory_data_log_files)`** — Сохраняет DataFrame в CSV одновременно в рабочую папку и лог.
*   **`save_html_log_work_file(full_html, file_name, directory_data_temp_files, directory_data_log_files)`** — Сохраняет HTML-код в две папки.
*   **`save_text_log_file(text, file_name, directory_data_temp_files, directory_data_log_files)`** — Сохраняет произвольный текст в файлы логов и временных данных.
*   **`convert_columns_to_int(df, columns, default_value=-1)`** — Безопасно преобразует выбранные столбцы таблицы в целые числа, заменяя ошибки значением по умолчанию.
*   **`print_file_modification_time(file_path)`** — Возвращает и выводит дату последнего изменения указанного файла.
*   **`load_int_list(parent_dir, directory_data_temp_files, file_name)`** — Читает список целых чисел из файла, расположенного в проектной структуре папок.
*   **`load_string_list(parent_dir, directory_data_temp_files, file_name)`** — Загружает список строк из файла, очищая их от лишних пробелов.
*   **`dict_to_json(data_dict, json_file_path)`** — Сохраняет словарь в JSON по конкретному пути.
*   **`save_dict_log_work_file(data_dict, file_name, directory_data_temp_files, directory_data_log_files)`** — Функция-дубликат для сохранения словарей в две папки.
*   **`detect_encoding(file_path)`** — Проверяет файл и определяет его кодировку с помощью `charset_normalizer`.
*   **`collect_keys_by_depth(obj, depth=0, keys_by_level=None)`** — Рекурсивно собирает все ключи вложенных словарей и группирует их по уровням вложенности.
*   **`files_in_directory(directory_path, operating_mode=0)`** — Выводит список файлов в папке или возвращает их списком в зависимости от режима.
*   **`time_to_minutes(val)`** — Конвертирует строку времени "ЧЧ:ММ" в общее число минут с начала суток.
*   **`list_to_str(list_to_str, quotes=False)`** — Объединяет элементы списка в строку через запятую.
*   **`select_non_numeric_rows(df, columns)`** — Выделяет из таблицы строки, которые содержат нечисловые значения в указанных столбцах.
*   **`load_excel_sheets(file_path, sheets_to_load)`** — Загружает выбранные листы из Excel-файла в словарь из DataFrames.
*   **`filter_df_by_suffix(df, suffixes_list)`** — Фильтрует строки DataFrame по соответствию окончаний в колонке `name` списку суффиксов.
*   **`check_columns_exist_id_df(df, cols_list, df_name="DataFrame")`** — Проверяет наличие всех колонок из списка в таблице, иначе вызывает ошибку.
*   **`check_columns_absent_id_df(df, cols_list, df_name="DataFrame")`** — Проверяет, что указанные колонки отсутствуют в таблице (защита от перезаписи).
*   **`merge_left_with_check(df_left, df_right, left_on, right_on, cols_map)`** — Выполняет левое слияние таблиц с предварительной проверкой конфликтов имен.
*   **`load_csv(file_name, data_dir, delimiter=',', encoding='utf-8', df_name='my_dataframe')`** — Обертка над `CSVLoader` для быстрой загрузки данных.
*   **`save_dict_to_json_zip(dict_data, directory_path, file_name, time_in_name=True)`** — Упаковывает словарь в JSON и затем сжимает его в ZIP-архив.
*   **`save_dict_data_log_work_file_zip(dict_data, file_name, directory_data_temp_files, directory_data_log_files)`** — Сохраняет ZIP-архив со словарем одновременно в две папки.
*   **`read_json_from_zip_or_file(zip_path, json_path, filename_extension)`** — Пытается прочитать JSON-данные либо напрямую из файла, либо извлечь их из ZIP-архива.