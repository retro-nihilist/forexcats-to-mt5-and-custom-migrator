# Этот файл будет содержать всю логику загрузки конфигурации: путей к директориям, библиотекам и динамическим функциям

import os
import sys

def load_config():
    current_dir = os.getcwd()  # Определяем путь к текущему файлу (где выполняется код)
    parent_dir = os.path.dirname(current_dir)  # Переход на уровень выше
    print(f"Рабочая директория проекта {parent_dir}")
    
    config_path = os.path.join(parent_dir, "directory_config.txt")  # Путь к файлу конфигурации
    directories = {}  # Словарь с путями
    
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.split("#")[0].strip()  # Убираем комментарии и пробелы
                if "=" in line:
                    key, value = map(str.strip, line.split("=", 1))
                    directories[key] = os.path.join(parent_dir, value.strip("'\""))  # Формируем абсолютный путь
    else:
        print(f"❌ ERROR: Файл конфигурации '{config_path}' не найден.")
    
    for key, path in directories.items():
        print(f"📂 {key}: {path}")  # Вывод всех загруженных директорий
    
    return directories

def setup_libraries(directories):
    libraries_path = os.path.join(directories.get("directory_libraries_path", ""))
    sys.path.append(libraries_path)
    
    if libraries_path in sys.path:
        print(f"✅ Каталог {libraries_path} успешно добавлен в sys.path")
    else:
        print(f"❌ Ошибка: {libraries_path} не найден в sys.path")

    return libraries_path

def import_dynamic_functions(libraries_path):
    file_imports = "dynamic_import_functions.py"
    file_imports_path = os.path.join(libraries_path, file_imports)
    
    if os.path.exists(file_imports_path):
        import importlib
        importlib.invalidate_caches()
        from dynamic_import_functions import import_functions, print_import_function_info
        print(f"\n ✅ Импорт [{file_imports}] успешен.")
        return import_functions, print_import_function_info
    else:
        print(f"\n ERROR: Файл '{file_imports}' не найден по пути {file_imports_path}, импорт не выполнен.\n")
        return None, None
