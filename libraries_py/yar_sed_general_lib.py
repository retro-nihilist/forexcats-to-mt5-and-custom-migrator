# np_set_printoptions 
    # Функция для отображения массива, отображает массив и возвращает список искомых элементов
        # name              - отображаемое имя маита;
        # array             - сам массив;
        # num               - порядковый номер элементов из которых формируется список
        # thres_hold        - сколько строк выводим
        # if_elements_nan   - какое значение добавляем в список искомых элементов при отсутствии элемента в строке

# df_array_symbols функция формирования ДФ из списка объектов (словарей)

# pd_set_option 
    # Функция установки количества отображаемых строк для display
        # name_df - название таблицы
        # df - сам дата фрейм
        # rows - количество отображаемых строк
        # columns - количество отображаемых колонок

# CSVLoader 
    # Класс для создания ДФ из CSV
        # file_path: путь к CSV-файлу.
        # delimiter: разделитель, используемый в файле (по умолчанию ';').
        # encoding: кодировка файла (по умолчанию 'utf-8').
        # df_name: пользовательское имя для DataFrame (по умолчанию 'dataframe'

# delete_rows_by_condition
    # Функция для удаления строк по заданному значению определённой колонки
        # df - сам ДФ
        # column - колонка в которой ищутся значения 
        # value - Значение, при нахождении которого, удаляется строка

# df_to_csv
    # Сохранение DF в CSV файл
        # df - сам ДФ
        # csv_file_path - полное имя файла без пути к нему

#def comparison_sets(set1, set2):
    # функция сравнения множеств
        # set1 - первое множество
        # set2 - второе множество

#def find_intersecting_lists (lists, list_names, save_csv=False):
    # Функция для поиска пересекающихся списков
        #lists (list of lists): Список, содержащий несколько списков, которые нужно проанализировать на пересечения.
        #list_names (list of str): Список строк, содержащий имена для каждого списка в lists. Эти имена будут использоваться для сохранения списков в файлы CSV.
        #save_csv (bool, optional): Флаг, указывающий, нужно ли сохранять списки в файлы CSV. По умолчанию False.
    #return
        # intersecting_sets (list of tuples): Список кортежей, где каждый кортеж содержит:
            # i (int): Индекс первого списка.
            # j (int): Индекс второго списка.
            # intersection (set): Множество пересекающихся элементов между двумя списками.
            # count (int): Количество пересекающихся элементов.

# list_print list_print(list, label) 
    # Печать длинны и элементов списка 

# def load_account_list(file_path):
    #  Загружаем список счетов из файла

# добавить определенный суффикс ко всем именам колонок в DataFrame
    # def columns_name_suffix(df, suffix):

# сохраним временный и лог файл с результатами
    # def save_data_log_work_file(df, file_name, directory_data_temp_files, directory_data_log_files):

import numpy as np
import pandas as pd
import os
from datetime import datetime
from pathlib import Path
import json


# Функция для отображения массива <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def np_set_printoptions(name, array, num, threw_hold = 10, if_elements_nan = 0):    # Устанавливаем опции  для всей библиотеки NumPy
        # name              - отображаемое имя масива;
        # array             - сам массив;
        # num               - порядковый номер элементов из которых формируется список
        # thres_hold        - сколько строк выводим
        # if_elements_nan   - какое значение добавляем в список искомых элементов при отсутствии элемента в строке
    np.set_printoptions(threshold = threw_hold)
    if isinstance(array, np.ndarray):                                           # Вывод названия и содержимого массива
        print(f"{name} {len(array) if array.size > 0 else 0}:\n", array)

        elements = [deal[num] for deal in array]
        elements = list(map(int, elements))
        print("first_elements = ", elements)
    else:
        print(f"{name} не является массивом NumPy. Значение: {array}")          # Если array не массив, выводим сообщение
        elements = if_elements_nan
    return elements
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# функция формирования ДФ из списка объектов (словарей)  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def df_array_symbols (array_symbols):
    print(f"функция формирования ДФ из массивов конфиграций символов МТ5. \n Колличество объектов к преобразованию в ДФ {[len(array_symbols)]}")
    first_symbol = array_symbols[0]                                         # Получаем список атрибутов первого объекта
    attributes = [attr for attr in dir(first_symbol) if 
                not attr.startswith('__') and 
                not callable(getattr(first_symbol, attr))]
    print(f"Имена атрибутов принятые за названия колонок \n {attributes}")
    data = []                                                               # Собираем данные из всех объектов
    for symbol in array_symbols:
        row = {attr: getattr(symbol, attr, None) for attr in attributes}
        data.append(row)
    df = pd.DataFrame(data)                                                 # Создаём DataFrame
    df.to_csv("symbols_data.csv", index=False)                              # Сохраняем в файл, если нужно
    return(df)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция установки количества отображаемых строк для display <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
"""def pd_set_option(name_df, df, rows=5, columns=None):
        # name_df - название таблиы
        # df - сам дата фрейм
        # rows - количество отображаемых строк
        # columns - количество отображаемых колонок
    pd.set_option('display.max_rows', rows)
    pd.set_option('display.max_columns', columns)
    print(name_df)
    display(df)"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


"""def pd_set_option(name_df, df, rows=5, columns=None, min_rows=None, min_columns=None):
    
    #name_df - название таблицы
    #df - сам датафрейм
    #rows - максимальное количество строк для отображения (если > len(df), покажет все)
    #columns - максимальное количество колонок
    #min_rows - сколько первых и последних строк показывать при сокращении
    
    
    if min_rows is None: min_rows = max(1, rows // 2)                       # Если не указано, min_rows = rows - 1 (чтобы показать rows//2 сверху и снизу)
    pd.set_option('display.max_rows', rows)                                 # Устанавливаем максимальное количество строк для отображения
    pd.set_option('display.min_rows', min_rows)                             # Устанавливаем, сколько первых и последних строк показывать при сокращении
    pd.set_option('display.min_columns', min_columns)                                   
    if columns is not None: pd.set_option('display.max_columns', columns)   

    print(name_df)
    display(df)

    pd.reset_option('display.max_rows')                                     # Сбрасываем опции (опционально, если не хотите влиять на другие вызовы)
    pd.reset_option('display.min_rows')"""


#import pandas as pd
#from IPython.display import display

def pd_set_option(
    name_df: str,
    df: pd.DataFrame,
    rows: int = 10,
    columns: int | None = None,
    min_rows: int | None = None,
    width: int = 100
):
    """
    Красиво выводит DataFrame с заголовком и временными настройками отображения.
    
    Параметры:
    - name_df: название таблицы (будет выведено жирным)
    - df: сам DataFrame
    - rows: сколько строк показывать максимум (по умолчанию 10)
    - columns: сколько колонок максимум (None = все)
    - min_rows: сколько строк сверху и снизу показывать при усечении (по умолчанию rows-2)
    - width: ширина вывода (по умолчанию 100)
    """
    # Автоматически определяем min_rows, если не задан
    if min_rows is None:
        min_rows = max(2, rows - 2)  # чтобы было хотя бы по 1 сверху и снизу + "..."

    # Сохраняем текущие настройки, чтобы потом восстановить
    old_options = {
        'max_rows': pd.get_option('display.max_rows'),
        'min_rows': pd.get_option('display.min_rows'),
        'max_columns': pd.get_option('display.max_columns'),
        'width': pd.get_option('display.width'),
    }

    try:
        # Применяем временные настройки
        pd.set_option('display.max_rows', rows)
        pd.set_option('display.min_rows', min_rows)
        pd.set_option('display.max_columns', columns or 999)  # если None — покажем все
        pd.set_option('display.width', width)

        # Красивый заголовок
        print(f"\n\033[1m{name_df}\033[0m  ({len(df):,} строк × {len(df.columns):,} колонок)")
        display(df)
        
    finally:
        # ВОССТАНАВЛИВАЕМ ВСЕ НАСТРОЙКИ! Это критически важно!
        pd.set_option('display.max_rows', old_options['max_rows'])
        pd.set_option('display.min_rows', old_options['min_rows'])
        pd.set_option('display.max_columns', old_options['max_columns'])
        pd.set_option('display.width', old_options['width'])


# Класс для создания ДФ из CSV <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
class CSVLoader:
    def __init__(self, file_path, delimiter=';', encoding='utf-8', df_name='dataframe'):
        self.file_path = file_path
        self.delimiter = delimiter
        self.encoding = encoding
        self.df_name = df_name
        self.dataframe = None
    def load_data(self):  #Загрузка данных из CSV файла в DataFrame.
        try:
            self.dataframe = pd.read_csv(self.file_path, delimiter=self.delimiter, encoding=self.encoding)
            print(f"✅ Success: [class CSVLoader]: DataFrame '{self.df_name}' успешно создан из '{self.file_path}'.")
            return self.dataframe
        except Exception as e:
            print(f"❌ ERROR: Ошибка при загрузке данных: {e}")
            return None
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для удаления строк по заданному значению определённой колонки <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def delete_rows_by_condition(df, column, value):   
        # df - сам ДФ
        # column - колонка в которой ищутся значения 
        # value - Значение, при нахождении которого, удаляется строка
    if type(value) == list: indices_to_remove = df[df[column].isin(value)].index   # Находим индексы строк для удаления
    else:                   indices_to_remove = df[df[column] == value].index       # Находим индексы строк, которые нужно удалить
    count_to_remove = len(indices_to_remove)                                        # Подсчитываем количество удаляемых строк
    df.drop(indices_to_remove, inplace=True)                                        # Удаляем строки с помощью метода drop
    print(f"Удалено [{count_to_remove}] строк в которых [{column} = {value}]")      # Выводим количество удалённых строк
    return df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Сохранение DF в CSV файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def df_to_csv(df, csv_file_path):
        # df - сам ДФ
        # csv_file_path - полное имя файла без пути к нему
    df.to_csv(csv_file_path, index=False)
    full_path = os.path.abspath(csv_file_path)              # Получение полного пути к фалу
    print(f"💾 Полный путь к сохраняемому файлу: {full_path}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# функция сравнения множеств <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def comparison_sets(set1, set2):
    print("Общие элементы:", sorted(set1 & set2))  # Пересечение множеств
    print("Уникальные для set1:", sorted(set1 - set2))  # Уникальные для set1
    print("Уникальные для set2:", sorted(set2 - set1))  # Уникальные для set2
    print("Объединение:", sorted(set1 | set2))  # Объединение множеств
    if set1==set2:
        return "Множества идентичны"
    else: return "Множества различны"
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для поиска пересекающихся списков <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
"""
lists (list of lists): Список, содержащий несколько списков, которые нужно проанализировать на пересечения.
list_names (list of str): Список строк, содержащий имена для каждого списка в lists. Эти имена будут использоваться для сохранения списков в файлы CSV.
save_csv (bool, optional): Флаг, указывающий, нужно ли сохранять списки в файлы CSV. По умолчанию False.
"""
def find_intersecting_lists(lists, list_names, save_csv=False):
    intersecting_sets = []
    for i in range(len(lists)):
        set_i = set(lists[i])
        for j in range(i + 1, len(lists)):
            set_j = set(lists[j])
            intersection = set_i & set_j                                                    # Проверка пересечения множеств
            if intersection:
                intersecting_sets.append((i, j, intersection, len(intersection)))
    if save_csv:                                                                            # Сохранение списков в файлы CSV
        print(f"Сохранение списков в файлы CSV: {list_names}")    
        for lst, name in zip(lists, list_names):
            df = pd.DataFrame(lst, columns=[name])
            df.to_csv(f"{name}.csv", index=False)
    if intersecting_sets:
        for i, j, intersection, count in intersecting_sets:
            print(f"Списки {i} и {j} имеют пересекающиеся элементы: (Количество: {count}) {intersection}")
    else:
        print("Нет пересекающихся элементов.")
    #return intersecting_sets
"""
intersecting_sets (list of tuples): Список кортежей, где каждый кортеж содержит:
i (int): Индекс первого списка.
j (int): Индекс второго списка.
intersection (set): Множество пересекающихся элементов между двумя списками.
count (int): Количество пересекающихся элементов."""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Печать длинны и элементов списка <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def list_print(lst, label=None, limit=10):
    display_list = lst[:limit]                          # Берем только первые элементы до лимита
    suffix = "..." if len(lst) > limit else ""          # Добавляем пометку, если список длиннее лимита
    print(f"📝 [ {len(lst)} ] элементов в списке [ {label} ] список: {display_list}{suffix}")
#def list_print(list, label = None): print(f"📝 [ {len(list)} ] элементов в списке [ {label} ] список: {list}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# сохранения списка цифровых значений в csv файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_list_to_csv_file(data_list, short_file_path, text):
    acc_set = list({int(x) for x in data_list})           # Преобразуем значения множества в целые числа и формируем список
    open(short_file_path, 'w').close()                            # Создаем пустой файл # Открываем файл в режиме записи и сразу закрываем
    with open(short_file_path, 'w') as f:                         # Открываем файл для записи
        f.write(', '.join(map(str, acc_set)))               # Преобразуем элементы множества в строки и записываем их, разделяя запятыми

    long_file_path = os.path.abspath(short_file_path)                               # Получаем абсолютный путь к файлу
    print(f"💾 Путь к сохранённому списку [{text}]: [{long_file_path}]")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Загружаем список счетов из файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def load_account_list(file_path):
    with open(file_path, 'r') as file:                                          # Читаем файл с идентификаторами
        account_ids = file.read().strip().split(', ')                           # Извлекаем строки и делим их по запятой
    account_ids = [int(id.strip()) for id in account_ids]                       # Преобразуем идентификаторы в целые числа
    print(f"Файл: {file_path}; Длинна списка: {len(account_ids)}")
    return  account_ids
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
# Сохранение списка в CSV (в одну строку) <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_to_str_csv(list,  short_file_path,  file_name, time_in_name = True):

    import csv
    from datetime import datetime
    
    if time_in_name: current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")[:-3]
    else: current_time =""

    file_path = os.path.join(short_file_path, f"{current_time}{file_name}")  # Безопасное соединение путей
                                                           
    os.makedirs(os.path.dirname(file_path), exist_ok=True)   # Проверяем, существует ли папка "file/temp"   # Создаёт папку, если её нет
    
    str_list = sorted({int(x) for x in list})  # Сортируем, если порядок важен
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(str_list)  # Записываем список в CSV-формате++
    print(f"Список из [{len(list)}] элементов, сохранён в файл: {file_path}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

# добавить определенный суффикс ко всем именам колонок в DataFrame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def columns_name_suffix(df, suffix):
    df = df.rename(columns=lambda x: x + suffix)    # Добавление суффикса ко всем именам колонок
    return df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Создание имени файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def file_name_with_time(file_name, short_file_path = "", time_in_name = True):
    from datetime import datetime

    if time_in_name: current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f ")[:-7]
    else: current_time =""
    file_path = os.path.join(short_file_path, f"{current_time}{file_name}")  # Безопасное соединение путей
    #print(f"def file_name_with_time({short_file_path},  {file_name}, {time_in_name}) = {file_path}")
    return file_path
#"""file_name_with_time("dir", "file.csv", time_in_name = True)"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""# Сохранение списка в CSV (в одну строку) с датой в имени файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_to_str_csv(list, short_file_path,  file_name, time_in_name = True):
    print(f"_______________def int_to_str_csv(len[{len(list)}], {short_file_path},  {file_name}, time_in_name = {time_in_name}):")
    import csv

    file_path = file_name_with_time(file_name, short_file_path, time_in_name)    

    os.makedirs(os.path.dirname(file_path), exist_ok=True)   # Проверяем, существует ли папка # Создаёт папку, если её нет
    
    str_list = sorted({int(x) for x in list})  # Сортируем, если порядок важен

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(str_list)  # Записываем список в CSV-формате++
    print(f"Список из [{len(list)}] элементов, сохранён в файл: {file_path}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

# Сохранение списка в CSV (в одну строку) с датой в имени файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def int_to_str_csv(int_list, short_file_path,  file_name, time_in_name = True, sort = False):
    #print(f"def int_to_str_csv(len[{len(int_list)}], {short_file_path},  {file_name}, time_in_name = {time_in_name}):")
    import csv

    file_path = file_name_with_time(file_name, short_file_path, time_in_name)    

    os.makedirs(os.path.dirname(file_path), exist_ok=True)   # Проверяем, существует ли папка # Создаёт папку, если её нет
    
    if sort:
        str_list = sorted({int(x) for x in int_list})  # Сортируем, если порядок важен
    else: str_list = int_list

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(str_list)  # Записываем список в CSV-формате++
    print(f"💾 Список из [{len(int_list)}] элементов, сохранён в файл: {file_path}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Генерация случайного трёхзначного числа 100 - 999 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
"""def get_random_three_digits():
    random_three_digit = f"{random.randint(0, 999):03}"
    random_three_digit = int(random_three_digit)
    return random_three_digit"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Генерация случайного трёхзначного числа 100 - 999 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def get_random_three_digits():
    import random
    return int(f"{random.randint(0, 999):03}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Преобразование Timestamp в Unix время <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
def time_str_to_unix_time_2(time_str):
    import time
    #print(time_str, type(time_str))
    if isinstance(time_str, pd.Timestamp):
        unix_time = int(time.mktime(time_str.timetuple()))     # Преобразование в Unix время
    else: unix_time = 0
    #print("unix_time = ", unix_time)
    return unix_time"""

def time_str_to_unix_time_2(time_str): # Преобразование Timestamp в Unix время как есть (без учёта поясов и летнего времени)
    import calendar
    if isinstance(time_str, pd.Timestamp):
        return int(calendar.timegm(time_str.utctimetuple()))            # UTC-время, без DST
    else:
        print(f"❌ ERROR: Данные не является Timestamp: {time_str}; (def time_str_to_unix_time_2)")
        return 0
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция добавления новых колонок с пустыми значениями и изменения положения этих колонок <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def move_column(df, list_col_name, add_list_col_name=False, new_position=0, new_position_step=1, print_info = False):
    print(" \n [dif] Функция добавления новых колонок с пустыми значениями и изменения положения этих колонок",
          f" \n list_col_name = {list_col_name};",
          f" \n new_position = {new_position}, new_position_step = {new_position_step}")
    
    if add_list_col_name:                                                       # Добавляем новые колонки, если требуется
        for col in list_col_name:
            if col not in df.columns:                                           # Проверяем, что колонки еще не существуют
                df[col] = None
    
    columns = list(df.columns)                                                  # Создаем список колонок для перестановки
    for i, col in enumerate(list_col_name):
        if col in columns:                                                      # Проверяем, что колонка есть в DataFrame
            columns.remove(col)                                                 # Удаляем колонку из текущей позиции
            insert_position = new_position + i * new_position_step              # Вычисляем новую позицию
            columns.insert(insert_position, col)                                # Вставляем колонку на новую позицию
            if print_info == True: print(f"Перемещена колонка '{col}' на позицию {insert_position}")
        else: print(f"❌ ERROR: колонка '{col}' отсутствует не найдена \n")

    return df[columns]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# добавить определенный суффикс ко всем именам колонок в DataFrame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def columns_name_suffix(df, suffix):
    print("dif бобавления суффикса к имени колонки ДФ. суффикс =", suffix)
    df = df.rename(columns=lambda x: x + suffix)    # Добавление суффикса ко всем именам колонок
    return df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Сохраняет словарь в JSON-файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def save_dict_to_json(dict_data, short_file_path, file_name, time_in_name=True):
    import json
    file_path = file_name_with_time(file_name, short_file_path, time_in_name)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        json.dump(dict_data, f, indent=4, ensure_ascii=False)  # Красивый JSON с отступами
    print(f"💾 Словарь сохранён в файл: {file_path}")

# временный и лог файл JSON <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def save_dict_data_log_work_file(dict_data, file_name, directory_data_temp_files, directory_data_log_files):
    if dict_data:
        (f"\n Словарь {dict_data}")
        save_dict_to_json(dict_data, directory_data_temp_files, file_name, time_in_name=False)
        save_dict_to_json(dict_data, directory_data_log_files, file_name)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Cохраняем СПИСОК временный и лог файл с результатами <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def save_int_list_data_log_work_file(int_list, file_name, directory_data_temp_files, directory_data_log_files):
    if int_list:
        int_to_str_csv(int_list, directory_data_temp_files,  file_name, time_in_name = False)    # Сохраняем фал для дальнейшей работы
        int_to_str_csv(int_list, directory_data_log_files,  file_name)                           # Сохраняем файл как лог работы
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Cохраняем временный и лог CSV файл с результатами <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
def save_data_log_work_file(df, file_name, directory_data_temp_files, directory_data_log_files):
    file_temp_name  = file_name_with_time(file_name, directory_data_temp_files, time_in_name = False)
    df_to_csv(df, file_temp_name)                                           # Сохраняем ДФ с данными в CSV файл
    file_log_name   = file_name_with_time(file_name, directory_data_log_files, time_in_name = True)
    df_to_csv(df, file_log_name)                                            # Сохраняем ДФ с данными в CSV файл
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Cохраняем временный и лог HTML файл с результатами <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
def save_html_log_work_file(full_html, file_name, directory_data_temp_files, directory_data_log_files):
    # 1. Формируем путь для временного файла (без даты в имени)
    file_temp_name = file_name_with_time(file_name, directory_data_temp_files, time_in_name=False)
    # Убедимся, что расширение .html (если file_name_with_time его не добавляет)
    if not file_temp_name.endswith('.html'): file_temp_name += '.html'
    
    with open(file_temp_name, 'w', encoding='utf-8') as f: f.write(full_html)
    print(f"💾 Сохраняем в [temp] {file_name} : {file_temp_name}")
    
    # 2. Формируем путь для лог-файла (с датой и временем в имени)
    file_log_name = file_name_with_time(file_name, directory_data_log_files, time_in_name=True)
    if not file_log_name.endswith('.html'): file_log_name += '.html'
        
    with open(file_log_name, 'w', encoding='utf-8') as f: f.write(full_html)
    print(f"💾 Сохраняем в [log] {file_name} : {file_log_name}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
По нижеприведённому принципу:

# Создание имени файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def file_name_with_time(file_name, short_file_path = "", time_in_name = True):
    from datetime import datetime

    if time_in_name: current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f ")[:-7]
    else: current_time =""
    file_path = os.path.join(short_file_path, f"{current_time}{file_name}")  # Безопасное соединение путей
    #print(f"def file_name_with_time({short_file_path},  {file_name}, {time_in_name}) = {file_path}")
    return file_path

# Сохранение DF в CSV файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def df_to_csv(df, csv_file_path):
        # df - сам ДФ
        # csv_file_path - полное имя файла без пути к нему
    df.to_csv(csv_file_path, index=False)
    full_path = os.path.abspath(csv_file_path)              # Получение полного пути к фалу
    print(f"💾 Полный путь к сохраняемому файлу: {full_path}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Cохраняем временный и лог файл с результатами <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
def save_data_log_work_file(df, file_name, directory_data_temp_files, directory_data_log_files):
    file_temp_name  = file_name_with_time(file_name, directory_data_temp_files, time_in_name = False)
    df_to_csv(df, file_temp_name)                                           # Сохраняем ДФ с данными в CSV файл
    file_log_name   = file_name_with_time(file_name, directory_data_log_files, time_in_name = True)
    df_to_csv(df, file_log_name)                                            # Сохраняем ДФ с данными в CSV файл
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Нужно выполнить сохранение словаря: в формате JSON в двух папках: временной и лог-файл
т.е. мне нужна функция аналогичная save_data_log_work_file, но для словаря
"""

# Сохраняем текстовый лог файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def save_text_log_file(text, file_name, directory_data_temp_files, directory_data_log_files):
    file_temp_name = file_name_with_time(file_name, directory_data_temp_files, time_in_name=False)
    print(f"Сохраняем текстовый лог файл: {file_temp_name}")
    with open(file_temp_name, "w", encoding="utf-8") as f:
        f.write(text)
    file_log_name = file_name_with_time(file_name, directory_data_log_files, time_in_name=True)
    print(f"Сохраняем текстовый лог файл: {file_log_name}")
    with open(file_log_name, "w", encoding="utf-8") as f:
        f.write(text)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Преобразует значения в указанных столбцах DataFrame к типу int <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def convert_columns_to_int(df, columns, default_value = -1):
    """
    Преобразует значения в указанных столбцах DataFrame к типу int.
    Если значение отсутствует (NaN) или не может быть преобразовано, присваивает значение по умолчанию.
    
    :param df: pandas.DataFrame
    :param columns: список столбцов для преобразования
    :param default_value: значение по умолчанию для отсутствующих или некорректных значений
    :return: pandas.DataFrame
    """
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')       # Преобразование к числу (замена некорректных значений на NaN)
        df[col] = df[col].fillna(default_value).astype(int)     # Замена NaN и преобразование к int
        #print("\n", df[col].value_counts(dropna=False), "\n")
    return df

# Выводим информацию о времени крайней модbфикации файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def print_file_modification_time(file_path):
    modification_time = os.path.getmtime(file_path)
    modification_date = datetime.fromtimestamp(modification_time)
    modification_date_time_str = modification_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"🕒 [ dif ] вывода времени крайней модификации файла: [ {file_path} ]; \n 📝 Крайняя модификация: {modification_date_time_str}")
    return modification_date_time_str
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Пример использования функции загрузки списка счетов из файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def load_int_list(parent_dir, directory_data_temp_files, file_name):
    file_path_temp              = os.path.abspath(os.path.join(parent_dir, directory_data_temp_files, file_name)) # Преобразуем в абсолютный путь
    print(f"[ def (load_int_list) ] Полный путь к файлу: {file_path_temp}")
    with open(file_path_temp, 'r') as file: account_ids = file.read().strip().split(',')    # Извлекаем строки и делим их по запятой
    account_ids = [int(id.strip()) for id in account_ids]                                   # Преобразуем идентификаторы в целые числа
    return account_ids

def load_string_list(parent_dir, directory_data_temp_files, file_name):
    file_path_temp = os.path.abspath(os.path.join(parent_dir, directory_data_temp_files, file_name))  # Преобразуем в абсолютный путь
    print(f"[ def (load_string_list) ] Полный путь к файлу: {file_path_temp}")
    with open(file_path_temp, 'r') as file:
        string_list = file.read().strip().split(',')  # Извлекаем строки и делим их по запятой
    string_list = [id.strip() for id in string_list]  # Удаляем пробелы и лишние символы
    return string_list

# Сохранение словаря в JSON <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def dict_to_json(data_dict, json_file_path):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)
    full_path = os.path.abspath(json_file_path)
    print(f"💾 Полный путь к сохраняемому JSON-файлу: {full_path}")

# Сохранение словаря JSON в две папки: временную и логовую <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def save_dict_log_work_file(data_dict, file_name, directory_data_temp_files, directory_data_log_files):
    file_temp_name = file_name_with_time(file_name, directory_data_temp_files, time_in_name=False)
    dict_to_json(data_dict, file_temp_name) # Без временной метки
    file_log_name = file_name_with_time(file_name, directory_data_log_files, time_in_name=True)
    dict_to_json(data_dict, file_log_name)  # С временной меткой
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Определение кодировки файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def detect_encoding(file_path):
    print("Определение кодировки файла:", file_path)
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return None
    from charset_normalizer import from_path
    results = from_path(file_path)
    best = results.best()
    encoding_file = best.encoding
    print("Определённая кодировка:", encoding_file)
    print("Уверенность (0.0 — отлично, ближе к 1.0 — плохо):", best.chaos, "\n")  # 0.0 — отлично, ближе к 1.0 — плохо
    return encoding_file

# Функция для сбора ключей по уровням вложенности (Использует defaultdict для хранения ключей на каждом уровне <<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def collect_keys_by_depth(obj, depth=0, keys_by_level=None):
    from collections import defaultdict
    if keys_by_level is None:
        keys_by_level = defaultdict(set)
    if isinstance(obj, dict):
        for key, value in obj.items():
            keys_by_level[depth].add(key)
            collect_keys_by_depth(value, depth + 1, keys_by_level)
    elif isinstance(obj, list):
        for item in obj:
            collect_keys_by_depth(item, depth, keys_by_level)
    return keys_by_level

# Функция для вывода файлов в директории <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def files_in_directory(directory_path, operating_mode = 0): # 0 - только вывод; 1 - только список; 2 - и вывод и список
    import os
    print(f"функция [files_in_directory] вывода файлов; operating_mode = {operating_mode}; \n 0 - только вывод; 1 - только список; 2 - и вывод и список; \n директория: {directory_path}:")
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    if len(files) < 1:
        print(f"❌ В директории [{directory_path}] нет файлов.")
        return
    if operating_mode == 0 or operating_mode == 2:
        for file in files:
            print(" ",file)
    if operating_mode == 1 or operating_mode == 2: return files


# Функция преобразования времени в формате [23:59] в минуты, прошедшие с начала суток <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def time_to_minutes(val):
    if pd.isna(val): return np.nan
    try:
        h, m = map(int, val.strip().split(":"))
        return h * 60 + m
    except: return np.nan
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция преобразования списка в строку с разделителем запятая <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def list_to_str(list_to_str, quotes=False):
    if quotes: return ",".join(f"'{s}'" for s in list_to_str)
    else: return ",".join(list_to_str)

# Возвращает строки, где хотя бы в одной из указанных колонок значение не числовое <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def select_non_numeric_rows(df, columns):
    """df       — исходный DataFrame
       columns  — список колонок для проверки"""
    numeric_df = df[columns].apply(pd.to_numeric, errors='coerce')  # Преобразуем значения в числа, некорректные становятся NaN
    mask = numeric_df.isna().any(axis=1)                            # Маска: строки, где есть хотя бы один NaN → значит значение не число
    return df[mask].copy()                                          # Возвращаем строки
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# Создаём словарь ДФ из нескольких листов Excel файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def load_excel_sheets  (file_path, sheets_to_load):
    # file_path - полный путь к файлу
    # sheets_to_load - список имён листов для загрузки
    dfs = {}                                            # словарь: имя листа → датафрейм 
    for sheet in sheets_to_load:
        df = pd.read_excel(file_path, sheet_name=sheet)
        dfs[sheet] = df
    for name, df in dfs.items(): print(f"Лист '{name}': {df.shape} строк")                              # Проверка
    return dfs

# Фильтрация df по суффиксам (окончаниям) в определённой колонке <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def filter_df_by_suffix(df, suffixes_list):
    print(f"\n Фильтрация акций суффиксам (окончаниям). ")
    list_print(suffixes_list, f"[{suffixes_list}] Суффиксов")
    #mask = df["name"].str.endswith(tuple(suffixes_list))
    mask = (df["name"].astype(str).str.strip().isin(suffixes_list))
    return  df[mask]

# Проверка наличия колонок в DataFrame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''
def check_columns_exist_id_df(df, cols_list, df_name="DataFrame"):
    missing = set(cols_list) - set(df.columns)
    if missing:
        raise KeyError(
            f"{df_name} не содержит колонок: {sorted(missing)}"
        )

def check_columns_absent_id_df(df, cols_list, df_name="DataFrame"):
    present = set(cols_list) & set(df.columns)
    if present:
        raise KeyError(
            f"{df_name} уже содержит одну из колонок: {sorted(present)}"
        )

# Функция слияния ДФ с проверкой наличия колонок и размерности <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def merge_left_with_check(df_left, df_right, left_on, right_on, cols_map):
    """
    Безопасный left merge с проверкой конфликтов имён в df_left.
    
    Параметры:
        df_left     — левый DataFrame (основной)
        df_right    — правый DataFrame (справочник)
        left_on     — колонка-ключа в df_left
        right_on    — колонка-ключа в df_right
        cols_map    — dict {right_col: new_left_col} — переименование колонок из right
    
    Возвращает:
        df_merged   — результат merge
        not_found   — ключи из left, для которых не нашлось match в right
        not_used    — ключи из right, которые не были использованы
    """
    print(f"\n [dif] Функция слияния ДФ с проверкой наличия колонок и размерности: merge_left_with_check()")
    # 1. Проверка наличия ключей (строго)
    check_columns_exist_id_df(df_left, [left_on], "df_left")
    check_columns_exist_id_df(df_right, [right_on] + list(cols_map.keys()), "df_right")
    
    # 2. Проверка конфликтов в df_left (мягкая — только предупреждение)
    forbidden_cols = set(cols_map.values())
    present_forbidden = [col for col in forbidden_cols if col in df_left.columns]
    
    if present_forbidden:
        print("ПРЕДУПРЕЖДЕНИЕ: в df_left уже присутствуют колонки, которые должны появиться после merge:")
        for col in sorted(present_forbidden):
            print(f"  - {col}")
        print("→ Это вызовет конфликт имён. Pandas добавит суффиксы _x / _y.")
        print("Рекомендуется переименовать или удалить их заранее.\n")
    
    # 3. Подготовка правого DF (только нужные колонки + переименование)
    df_right_prepared = df_right[[right_on] + list(cols_map.keys())].rename(columns=cols_map)
    
    # 4. Сам merge
    df_merged = df_left.merge(
        df_right_prepared,
        left_on=left_on,
        right_on=right_on,
        how="left",
        validate="many_to_one"
    )
    
    # 5. Контроль размерности
    assert len(df_merged) == len(df_left), "Размер df_merged изменился после left join!"
    
    # 6. Отчёт: какие ключи не нашли / не использовали
    if cols_map:  # если есть что добавлять
        any_added_col = next(iter(cols_map.values()))
        not_found = df_merged.loc[df_merged[any_added_col].isna(), left_on].dropna().unique().tolist()
        not_used = df_right.loc[~df_right[right_on].isin(df_left[left_on]), right_on].dropna().unique().tolist()
    else:
        not_found = []
        not_used = []
    
    return df_merged, not_found, not_used

def load_csv(file_name, data_dir, delimiter=',', encoding='utf-8', df_name='my_dataframe'):
    """
    Загружает CSV-файл через CSVLoader.
    Располагать в той же библиотеке, где определён CSVLoader.
    """
    file_path = Path(data_dir, file_name)
    loader = CSVLoader(file_path, delimiter=delimiter, encoding=encoding, df_name=df_name)
    return loader.load_data()

# Сохраняем словарь в JSON и упаковываем его в ZIP-файл <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def save_dict_to_json_zip(dict_data, directory_path, file_name, time_in_name=True):
    import zipfile
    #import datetime
    print(f"Вспомогательная функция для упаковывания словаря/JSON в .zip файл.")
    os.makedirs(directory_path, exist_ok=True)

    if time_in_name:
        now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = f"{file_name}_{now_str}"
    else:
        base_name = file_name

    json_inside_name = f"{base_name}.json"
    zip_full_name = f"{base_name}.zip"

    zip_file_path = os.path.join(directory_path, zip_full_name)

    # Поддержка передачи как словаря (dict), так и готовой JSON-строки (str)
    if isinstance(dict_data, str):json_str = dict_data
    else:json_str = json.dumps(dict_data, indent=4, ensure_ascii=False)

    # Записываем байты сразу в zip-архив
    with zipfile.ZipFile(zip_file_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(json_inside_name, json_str.encode("utf-8"))
        print(f"💾 Архив со Словарём сохранён в файл: {zip_file_path}")

# Cохраняем словарь в JSON и упаковываем его в ZIP-файл в двух папках: временной и логовой <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def save_dict_data_log_work_file_zip(dict_data, file_name, directory_data_temp_files, directory_data_log_files,):
    print(f"Сохранение словаря в рабочую/временную папку и лог-папку: {file_name}")
    if dict_data:
        save_dict_to_json_zip(dict_data, directory_data_temp_files,file_name, time_in_name=False,)
        save_dict_to_json_zip(dict_data, directory_data_log_files, file_name, time_in_name=True)

# Чтение JSON из ZIP-архива или напрямую из JSON-файла <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def read_json_from_zip_or_file(zip_path, json_path, filename_extension):
    import zipfile
    import tempfile
    # 1. Читаем байты JSON из ZIP-архива или напрямую из JSON-файла
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "r") as zf:
            raw_bytes = zf.read(filename_extension)
    elif os.path.exists(json_path):
        with open(json_path, "rb") as f:
            raw_bytes = f.read()
    else:
        raise FileNotFoundError(
            f"Файл {filename_extension} или {zip_filename} не найден в директории."
        )

    # 2. Передаем байты JSON во временный файл, чтобы detect_encoding смогла их прочитать
    with tempfile.NamedTemporaryFile(delete=False, suffix=".json") as temp_file:
        temp_file.write(raw_bytes)
        temp_path = temp_file.name

    try: en_coding = detect_encoding(temp_path)
    finally:
        if os.path.exists(temp_path): os.remove(temp_path)          # Удаляем временный файл после определения

    data = json.loads(raw_bytes.decode(en_coding))                  # 3. Декодируем и загружаем JSON

    return data