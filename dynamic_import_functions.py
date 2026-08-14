# dynamic import of functions
"""
Динамически импортирует указанные функции из заданных файлов.
    функция принимает путь к модулю как первый элемент списка в значении словаря.

:param modules: Словарь, где ключ — имя файла (без .py), значение — список импортируемых функций.
:return: Словарь {имя_функции: ссылка_на_функцию}
"""
import os
import sys
import importlib
from typing import Dict, List

def import_functions(modules: Dict[str, List[str]]):

    imported_functions = {}
    
    for module_name, values in modules.items():
        if not values:
            print(f"❌ ERROR: Не указан путь к модулю для '{module_name}'")
            continue
        
        module_path = values[0]  # Первый элемент списка - путь к модулю
        functions = values[1:]  # Остальные элементы - функции
        
        full_module_path = os.path.join(module_path, f"{module_name}.py")
        
        if os.path.exists(full_module_path):
            sys.path.append(module_path)  # Добавляем путь к модулю
            importlib.invalidate_caches()  # Сбрасываем кэш
            
            module = importlib.import_module(module_name)  # Динамический импорт
            importlib.reload(module)  # Перезагружаем, если уже импортирован
            
            for func in functions:
                if hasattr(module, func):
                    imported_functions[func] = getattr(module, func)
                    #print(f"Функция '{func}' найдена в модуле '{module_name}'")
                else:
                    print(f"\n❌ WARNING: Функция '{func}' не найдена в модуле '{module_name}'\n")
            
            print(f"Импорт из '{module_name}' успешен: {functions}")
        else:
            print(f"❌ ERROR: Файл '{full_module_path}' не найден, импорт не выполнен.")

      
    return imported_functions


def  print_import_function_info(modules_to_import, imported):
    import inspect
    print(f"\n Импортированные функции и их параметры:") 
    #Функция для вывода информации о параметрах функций
    def print_function_info(module_name, function_name, function):
        signature = inspect.signature(function)
        params = [str(param) for param in signature.parameters.values()]
        print(f"Функция '{function_name}' из модуля '{module_name}' ожидает параметры: {', '.join(params)}")

    # Вывод информации о параметрах импортированных функций
    for module_name, functions in modules_to_import.items():
        for function_name in functions[1:]:
            if function_name in imported:
                function = imported[function_name]
                print_function_info(module_name, function_name, function)

"""Как использовать:
Теперь функция принимает путь к модулю как первый элемент списка в значении словаря. Пример использования:

modules_to_import = {
    "imports": ["c:/unique_data/rep_fo_metatrader_server", "manager_connect", "manager_disconnect", "pd_read_sql", "move_column"],
    "utils": ["c:/some_other_path", "helper_function", "another_helper"]
}

imported = import_functions(modules_to_import)

# Теперь можно вызывать функции через словарь:
result = imported["manager_connect"]()

"""