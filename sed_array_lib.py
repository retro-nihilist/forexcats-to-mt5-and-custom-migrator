# def positions_in_array(array, values_to_find): Функция поиска позиций заданных значений в массиве
    #   :param array: Двумерный массив, в котором выполняется поиск
    #   :param values_to_find: Список значений для поиска
    #   :return: Словарь {значение: [(строка, позиция в строке), ...]}"""

# def get_column_values(array, column_index): Извлекает значения из указанной колонки структурированного массива
    #   """Извлекает значения из указанной колонки структурированного массива.
    #   Parameters:
    #       array (numpy.ndarray): Исходный массив.
    #       column_index (int): Индекс колонки (начиная с 0).
    #   Returns:
    #       numpy.ndarray: Значения указанной колонки."""

# def np_set_printoptions(name, array, num, thres_hold=10): Функция для настройки отображения массива
    #   name        Заголовок
    #   array       Сам массив 
    #   num         Номер колонки значения которой выводятся
    #   thres_hold  Количество отображаемых строк

# def sum_columns_by_indices(array, indices): Функция подсчёта суммы по колонкам МАССИВА переданным списком
    #   :param array: Одномерный массив NumPy или список кортежей
    #   :param indices: Список индексов колонок, значения которых нужно суммировать
    #   :return: Словарь с суммами по колонкам и общая сумма

# def array_to_dataframe_with_multiline_headers: 
# Преобразует структурированный numpy-массив в pandas DataFrame Заголовки (первая строка) и его формат данных (вторая строка)
    #   :param array: Одномерный массив NumPy или список кортежей
    #   :param indices: Список индексов колонок, значения которых нужно суммировать
    #   :return: Словарь с суммами по колонкам и общая сумма

# array_to_dataframe(array):
# Преобразует структурированный numpy-массив в pandas DataFrame Заголовки (первая строка)
    #   :param array: Одномерный массив NumPy или список кортежей
    #   :param indices: Список индексов колонок, значения которых нужно суммировать
    #   :return: Словарь с суммами по колонкам и общая сумма

#Преобразует список объектов (не имеющих __dict__) в pandas DataFrame

#Функция добавления новых колонок с пустыми значениями и изменения положения эnих колонок

import numpy as np

# Функция поиска позиций заданных значений в массиве <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def positions_in_array(array, values_to_find):
    """Поиск позиций заданных значений в массиве.
    :param array: Двумерный массив, в котором выполняется поиск
    :param values_to_find: Список значений для поиска
    :return: Словарь {значение: [(строка, позиция в строке), ...]}"""
    result = {value: [] for value in values_to_find}  # Инициализируем словарь с пустыми списками
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element in values_to_find:
                result[element].append((i, j))  # Добавляем (строка, позиция) в список соответствующего значения
    return result
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Извлекает значения из указанной колонки структурированного массива <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def get_column_values(array, column_index):
    """Извлекает значения из указанной колонки структурированного массива.
    Parameters:
        array (numpy.ndarray): Исходный массив.
        column_index (int): Индекс колонки (начиная с 0).
    Returns:
        numpy.ndarray: Значения указанной колонки."""
    if not array.dtype.names:
        raise ValueError("Массив не имеет структурированных данных.")
    
    field_name = array.dtype.names[column_index]
    return array[field_name]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для настройки отображения массива <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def np_set_printoptions(name, array, num, thres_hold=10):                       # Устанавливаем опции отображения для всей библиотеки NumPy
    np.set_printoptions(threshold=thres_hold)
    if isinstance(array, np.ndarray):                                           # Вывод названия и содержимого массива
        print(f"{name} {len(array) if array.size > 0 else 0}:\n", array)

        elements = [deal[num] for deal in array]
        elements = list(map(int, elements))
        print("first_elements = ", elements)

    else:
        print(f"{name} не является массивом NumPy. Значение: {array}")          # Если array не массив, выводим сообщение
        elements = 0
    return elements
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция подсчёта суммы по колонкам МАССИВА переданным списком <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def sum_columns_by_indices(array, indices):
    """
    Вычисляет сумму значений для указанных колонок в массиве или списке кортежей и общую сумму.
    :param array: Одномерный массив NumPy или список кортежей
    :param indices: Список индексов колонок, значения которых нужно суммировать
    :return: Словарь с суммами по колонкам и общая сумма
    """
    column_sums = {}
    total_sum = 0

    for index in indices:                                    # Проходим по индексам колонок
        column_sum = sum(row[index] for row in array)        # Суммируем значения по данному индексу в строках
        column_sums[index] = column_sum
        total_sum += column_sum

    return {"column_sums": column_sums, "total_sum": total_sum}
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Преобразует структурированный numpy-массив в pandas DataFrame Заголовки (первая строка) и его формат данных (вторая строка) <<<<<<<<<<<<<
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def array_to_dataframe_with_multiline_headers(array):

    import pandas as pd
    from IPython.display import display
    """
    Преобразует структурированный numpy-массив в pandas DataFrame.
    Заголовки столбцов включают имя параметра (первая строка) и его формат данных (вторая строка).
    :param array: numpy.ndarray со структурированным dtype
    :return: pandas.DataFrame
    """
    if not isinstance(array, np.ndarray) or not array.dtype.names:
        raise ValueError("Ожидается структурированный numpy.ndarray")
    
    # Формируем заголовки с переносами строк
    columns_with_multiline = [
        f"{field}<br>({str(array.dtype[field])})" for field in array.dtype.names
    ]
    df = pd.DataFrame(array.tolist(), columns=columns_with_multiline)
    
    #return df

    #df = array_to_dataframe_with_multiline_headers(deal_array)
    # Настройка для многострочных заголовков
    styled_df = df.style.set_table_styles([{'selector': 'th', 'props': [('white-space', 'pre-wrap'), ('text-align', 'center')]}])
    #display(df)
    return styled_df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Преобразует структурированный numpy-массив в pandas DataFrame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def array_to_dataframe(array):
    import pandas as pd
    from IPython.display import display
    """
    Преобразует структурированный numpy-массив в pandas DataFrame.
    Заголовки столбцов включают имя параметра (первая строка) и его формат данных (вторая строка).
    :param array: numpy.ndarray со структурированным dtype
    :return: pandas.DataFrame
    """
    if not isinstance(array, np.ndarray) or not array.dtype.names:
        raise ValueError("Ожидается структурированный numpy.ndarray")
    
    # Формируем заголовки с переносами строк
    columns_with_multiline = [f"{field} ({str(array.dtype[field])})" for field in array.dtype.names]
    
    df = pd.DataFrame(array.tolist(), columns=columns_with_multiline)
    
    return df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Преобразует список объектов (не имеющих __dict__) в pandas DataFrame <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````
def objects_to_dataframe(objects_list, pd):
    print("def objects_to_dataframe(objects_list) Преобразует список объектов (не имеющих __dict__) в pandas DataFrame.")
    """
    :param objects_list: список однотипных объектов
    :return: pandas.DataFrame"""
    if not objects_list: raise ValueError("Список объектов пуст.")
    total_objects = dir(objects_list[0])
    print(f"Получили список колонок (имён атрибутва): {total_objects}")
    attributes = [attr for attr in total_objects if not attr.startswith("__")]                      # Получаем все возможные атрибуты из первого объекта, исключая служебные
    df = pd.DataFrame([{attr: getattr(obj, attr) for attr in attributes} for obj in objects_list])  # Формируем DataFrame
    return df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция добавления новых колонок с пустыми значениями и изменения положения эnих колонок <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def move_column(df, list_col_name, add_list_col_name=False, new_position=0, new_position_step=0):
    print(" \n Функция добавления новых колонок с пустыми значениями и изменения положения этих колонок",
          f" \n list_col_name = {list_col_name}, new_position = {new_position}")
    
    # Добавляем новые колонки, если требуется
    if add_list_col_name: 
        for col in list_col_name:
            if col not in df.columns:  # Проверяем, что колонки еще не существуют
                df[col] = None
    
    # Создаем список колонок для перестановки
    columns = list(df.columns)
    for i, col in enumerate(list_col_name):
        if col in columns:  # Проверяем, что колонка есть в DataFrame
            columns.remove(col)  # Удаляем колонку из текущей позиции
            insert_position = new_position + i * new_position_step  # Вычисляем новую позицию
            columns.insert(insert_position, col)  # Вставляем колонку на новую позицию
            print(f"Перемещена колонка '{col}' на позицию {insert_position}")

    return df[columns]
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Исследуем атрибуты элемента массива <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   
def array_element_attributes(array, e):
    attributes = dir(array[e])
    if attributes:
        for a in attributes:
            try:
                value = getattr(array[e], a)
                print(f"{a}: {value}")
            except AttributeError:
                # Если атрибут не существует или не может быть извлечен, выводим сообщение
                print(f"{a}: Атрибут не существует или недоступен")
    else: print(f"не удалось извлечь элемент {e} массива")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>