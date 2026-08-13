# formatting balance transactions
# Поиск кириллических символов 
# Поиск запрещённых спецсимволов в строках ДФ 
# Замена запрещённых символов на "_" 
# Выявление уникальных символов задействованных в торговле
# Убираем дублирующиеся символы, оставляя те, спецификации которых имеют более частое вхождение в торговую историю
# Итоговое форматирование стейтмента
    # # Преобразование колонки 'open_time' и 'close_time' в тип данных datetime
    # Преобразование 'open_time' в Unix time
    # Преобразование 'close_time' в Unix time
    # Функция для вычисления значения в колонке TimeMsc
    # Добавление новых колонок TimeMsc и CloseTimeMsc
    # Добавление колонки 'type'

import pandas as pd
import numpy as np
from yar_sed_general_lib import pd_set_option, get_random_three_digits, time_str_to_unix_time_2

# formatting balance transactions

def format_balance_trans(df):
    df = df.copy()                                                      # Создаем копию DataFrame перед любыми изменениями, чтобы избежать SettingWithCopyWarning
    df.loc[:, 'deposit_date'] = pd.to_datetime(df['deposit_date'])      # Преобразуем колонку 'deposit_date' в формат datetime

    df.loc[:, 'TimeMsc'] = df['deposit_date'].astype("int64") // 10**6  # Переводим дату в Юникс Тайм (в миллисекундах и секундах) с использованием astype вместо view
    df.loc[:, 'Time'] = df['deposit_date'].astype("int64") // 10**9

    df.loc[:, 'login_user'] = df['lead_id'].astype("int64")             # Преобразуем другие колонки
    df.loc[:, 'comment'] = df['transaction_id'].astype(str)             # Замена кириллической "с" на латинскую "c"
    df.loc[:, 'balance_transactions'] = df['deposit_amount'].astype(float).round(2)

    df = df[['id', 'account_id', 'balance_transactions', 'comment', 'TimeMsc', 'Time', 'finance_type']] # Оставляем нужные колонки
    df.loc[:, 'type'] = 'balance'

    df.loc[:, 'TimeMsc'] = df['TimeMsc'].astype(np.int64)               # Приведение TimeMsc к int64

    return df

def format_trade_trans(df):
    df = df.copy()
    pd.set_option('future.no_silent_downcasting', True)                    # Включение будущего поведения для приведения типов
    # Форматируем данные в ДФ 
    df.loc[:, 'command'] = df['command'].replace({'BUY': 0, 'SELL': 1})    # Замена значений в колонке 'Command'
    df.loc[:, 'command'] = df['command'].astype('int64')                   # Изменение типа данных колонки на int64
    df.loc[:, 'volume_lots'] = df['volume_lots'].astype(float).round(2)

    count_removals = df['symbol'].str.count('/').sum()                        # Количество '/' в колонке 'column_name'
    #df.loc[:, 'symbol'] = df['symbol'].str.replace('/', '')                # Удаление символа '/' в колонке 'column_name'
    #statement_df['Symbol'] = statement_df['Symbol'].str.replace('XAUUSD', 'XAU/USD')
    print(f"Количество УДАЛЕНИЕ ОТКЛЮЧЕНО символа '/': {count_removals}")
    return df


# Поиск кириллических символов <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import re

def search_cyrillic_characters(symbols_to_create_df):

    def highlight_cyrillic(text):                                           # Функция для выделения кириллических символов
        if isinstance(text, str):                                           # Проверяем, является ли текст строкой (чтобы избежать ошибок)
            return re.sub(r'([\u0400-\u04FF])', r'<<<\1>>>', text)
        return text                                                         # Если текст не строка, возвращаем его как есть

    attributes = ['parent_currency_id', 'currency_name', 'symbol_profit', 'symbol_margin', 'symbol_description']    # Список колонок для проверки на кириллицу

    result_dict = {}                                                        # Словарь для записи результатов

    for index, row in symbols_to_create_df.iterrows():                      # Проход по строкам DataFrame
        highlighted_row = []                                                # Список для хранения выделенных значений
        has_cyrillic = False                                                # Флаг, указывающий, содержат ли значения кириллические символы
        
        for col in attributes:                                              # Проход по колонкам, указанным в attributes
            if col in row:
                original_value = str(row[col])                              # Извлекаем исходное значение и преобразуем к строке
                highlighted_value = highlight_cyrillic(original_value)      # Проверка на кириллицу
                
                if highlighted_value != original_value:                     # Если значение было изменено, значит, найдены кириллические символы
                    has_cyrillic = True
                
                highlighted_row.append(highlighted_value)                   # Добавляем результат в список
        
        if has_cyrillic:                                                    # Если хотя бы одно значение содержало кириллицу, добавляем строку в словарь
            result_dict[row['parent_currency_id']] = highlighted_row

    print("Словарь Строк с Кирилическими символами:", result_dict)


# Поиск запрещённых спецсимволов в строках ДФ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import re

def search_prohibited_characters(symbols_to_create_df):

    attributes = ['parent_currency_id', 'currency_name', 'symbol_profit', 'symbol_margin']          # Список колонок для запрещённых спецсимволов
    allowed_special_chars = "._&#"                                                                  # Список разрешённых спецсимволов

    def highlight_special_chars(text):                                                              # Функция для выделения запрещённых спецсимволов
        pass
        if isinstance(text, str):
            return re.sub(r'([^\w\s' + re.escape(allowed_special_chars) + r'])', r'<<<\1>>>', text) # Замена любых неразрешённых спецсимволов на выделенные
        return text

    result_dict = {}                                                                                # Словарь для записи результатов

    for index, row in symbols_to_create_df.iterrows():                                              # Проход по строкам DataFrame
        highlighted_row = []                                                                        # Список для хранения выделенных значений
        has_cyrillic = False                                                                        # Флаг, указывающий, содержат ли значения запрещённых спецсимволов
        
        for col in attributes:                                                                      # Проход по колонкам, указанным в attributes
            if col in row:
                original_value = str(row[col])                                                      # Извлекаем исходное значение и преобразуем к строке
                highlighted_value = highlight_special_chars(original_value)                         # Проверка на запрещённых спецсимволов
                
                if highlighted_value != original_value:                                             # Если значение было изменено, значит, найдены запрещённых спецсимволов
                    has_cyrillic = True
                
                highlighted_row.append(highlighted_value)                                           # Добавляем результат в список
        
        if has_cyrillic:                                                                            # Если хотя бы одно значение содержало кириллицу, добавляем строку в словарь
            result_dict[row['parent_currency_id']] = highlighted_row
                                                                                                    # Теперь словарь result_dict содержит только строки с запрещённых спецсимволов
    display(f"Строки содержащие запрещённые символы за исключением: {allowed_special_chars}", result_dict)


# Замена запрещённых символов на "_" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import re

def replacing_prohibited_characters(symbols_to_create_df):

    attributes = ['parent_currency_id', 'currency_name', 'symbol_profit', 'symbol_margin']  # Список колонок для проверки на запрещённые спецсимволы
    allowed_special_chars = "._&#"                                                          # Список разрешённых спецсимволов

    def highlight_special_chars(text):                                                      # Функция для выделения и замены запрещённых спецсимволов на "_"
        if isinstance(text, str):
            return re.sub(r'([^\w\s' + re.escape(allowed_special_chars) + r'])', r'_', text)# Заменяем все запрещённые спецсимволы на "_"
        return text

    for col in attributes:                                                                  # Проход по строкам DataFrame и замена значений в колонках на месте
        symbols_to_create_df[col] = symbols_to_create_df[col].apply(highlight_special_chars)# Теперь DataFrame symbols_to_create_df содержит заменённые спецсимволы на "_"

    print("FINAL замены запрещённых символов на _ ")

# Выявление уникальных символов задействованных в торговле <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def crm_symbol_tuple(statement_df):
    currency_id_tuple = tuple(set(statement_df['currency_id']))                     # Создание Множества из ID инструментов таблица торговых операций 
    print("Кортеж id торговых инструментов: ",currency_id_tuple)
    filtered_df = statement_df[statement_df['currency_id'].isin(currency_id_tuple)] # Фильтрация датафрейма по значениям currency_id из currency_id_tuple
    symbol_crm_tuple = tuple(set(filtered_df['symbol']))                            # Создание кортежа из значений колонки symbol
    del filtered_df
    print("Кортеж Символов задействованных в торговле: ", symbol_crm_tuple)
    return currency_id_tuple

# Убираем дублирующиеся символы, оставляя те, спецификации которых имеют более частое вхождение в торговую историю <<<<<
def currency_counts_def(statement_df, symbols_to_create_df):
    currency_counts = statement_df['currency_id'].value_counts().reset_index()                                              # Подсчитать количество вхождений каждого значения в statement_df["currency_id"]
    currency_counts.columns = ['currency_id', 'count_in_statement_df']
    symbols_to_create_counts_df = symbols_to_create_df.merge(currency_counts, how='left', on='currency_id')                 # Выполнить слияние non_unique_df с currency_counts по столбцу 'currency_id'
    symbols_to_create_counts_df['count_in_statement_df'] = symbols_to_create_counts_df['count_in_statement_df'].fillna(0)   # Заменить NaN на 0 для тех значений, которые не встречаются в statement_df
    columns = ['count_in_statement_df'] + [col for col in symbols_to_create_counts_df.columns if col != 'count_in_statement_df']    # Перенести колонку 'count_in_statement_df' влево # Получить список колонок и изменить порядок
    df_reordered = symbols_to_create_counts_df[columns]
    sorted_df = df_reordered.sort_values(by='count_in_statement_df', ascending = False)
    unique_sorted_df = sorted_df.drop_duplicates(subset='currency_name', keep='first')                                      # Удалить строки с дублирующимися значениями в колонке 'currency_name', оставив первое вхождение                                                                                      # Отобразить результат
    return unique_sorted_df

def statement_format(merged_df):
    statement_csv_df = merged_df[['mt5_deal_in_id', 'positions_id', 'crm_deals_id', 'account_id', 'lead_id', 'order_id', 'symbol', 'volume_lots', 'command', 're_open', 'position_id', 'swap', 'spread_x', 'open_price', 'close_price', 'current_rate', 'profit_right', 'point_profit',
                                  'open_time', 'close_time', 'rate_profit', 'mapping', 'leverage_x', 'margin', 'only_close',
                                  'sell_last_value', 'buy_last_value', 'symbol_digits_mt5',
                                  "_symbol", "symbol_description", "symbol_profit", "symbol_margin", "symbol_digits", "symbol_point", 'profit', 'profit_crm', "symbol_calc_mode", "symbol_contract_size"]]

    # Преобразование колонки 'open_time' и 'close_time' в тип данных datetime
    statement_csv_df = statement_csv_df.assign(
        open_time=pd.to_datetime(statement_csv_df['open_time'], format="%Y-%m-%d %H:%M:%S"),
        close_time=pd.to_datetime(statement_csv_df['close_time'], format="%Y-%m-%d %H:%M:%S")
    )

    # Преобразование 'open_time' в Unix time
    statement_csv_df = statement_csv_df.assign(
        Time=statement_csv_df['open_time'].apply(time_str_to_unix_time_2)
    ).assign(
        Time=lambda df: pd.to_numeric(df['Time'], errors='coerce').astype('int64')
    )

    # Преобразование 'close_time' в Unix time
    statement_csv_df = statement_csv_df.assign(
        CloseTime=statement_csv_df['close_time'].apply(time_str_to_unix_time_2)
    ).assign(
        CloseTime=lambda df: pd.to_numeric(df['CloseTime'], errors='coerce').astype('int64')
    )

    # Функция для вычисления значения в колонке TimeMsc
    def calculate_time_msc(time_value):
        if time_value > 0:
            random_three_digits = get_random_three_digits()
            time_msc = time_value * 1000 + random_three_digits
            return np.int64(time_msc)
        else: return 0

    # Добавление новых колонок TimeMsc и CloseTimeMsc
    statement_csv_df = statement_csv_df.assign(
        TimeMsc = statement_csv_df['Time'].apply(calculate_time_msc),
        CloseTimeMsc = statement_csv_df['CloseTime'].apply(calculate_time_msc)
    )

    # Добавление колонки 'type'
    statement_csv_df = statement_csv_df.assign(type='trade')

    # Возврат итогового DataFrame
    return statement_csv_df
