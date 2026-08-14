# Функция для чтения словаря из текстового файла
    # levels_up - Указывает Насколько уровней нужно подняться что бы попасть в корневой каталог
    # file_relative_path - Относительный путь к текстовому файлу 

import os

def read_dict_from_text_file(levels_up, file_relative_path):
    """Читает текстовый файл, содержащий словарь (в виде строки), убирая переносы строк."""
    current_dir = os.path.dirname(os.path.abspath(__file__))

    root_dir = current_dir
    for _ in range(levels_up):
        root_dir = os.path.dirname(root_dir)

    file_path = os.path.join(root_dir, file_relative_path)
    #print(f"Читаем файл: {file_path}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Читаем построчно

    dict_str = "".join(line.strip() for line in lines)  # Убираем пробелы и переносы строк
    #print(f"Объединённая строка словаря: {dict_str}")

    try:
        dict_data = eval(dict_str)  # Преобразуем строку в словарь
        if not isinstance(dict_data, dict):
            raise ValueError("Файл не содержит корректный словарь.")
    except Exception as e:
        raise ValueError(f"Ошибка преобразования строки в словарь: {e}")

    return dict_data