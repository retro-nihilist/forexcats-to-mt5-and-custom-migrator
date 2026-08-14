# project_paths.py
from pathlib import Path
import os
import sys


class ProjectConfig:
    """
    Класс для управления структурой директорий проекта.
    Централизует создание и проверку всех необходимых путей.
    """

    def __init__(self, file_dir: str = None, is_test_mode: bool = True):
        """
        Инициализация путей проекта.

        :param file_dir: os.getcwd() — текущая директория скрипта
        :param is_test_mode: режим работы (влияет только на комментарии/логи пока)
        """
        self.is_test_mode = is_test_mode

        # --- Основные уровни проекта ---
        self.file_dir = Path(file_dir or os.getcwd())
        self.sub_project_dir = self.file_dir.parent
        self.project_dir = self.sub_project_dir.parent          # fc_to_mt5_migrations/own_platform
        self.parent_dir = self.project_dir.parent               # fc_to_mt5_migrations

        # --- Директории ---
        self._ensure_all_directories()

        # Добавляем libraries_py в sys.path
        self.libraries_path = self.parent_dir / "libraries_py"
        self._add_libraries_to_sys_path()

    def _ensure_directory(self, path: Path, description: str = "", name: str = ""):
        """Создаёт директорию, если она не существует."""
        path = Path(path)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"❗📁 [{name or path.name}] создан: {path.absolute()}")
        else:
            print(f"    📁 [{name or path.name}]; {description}: {path.absolute()}")

    def _ensure_all_directories(self):
        """Создаёт/проверяет все необходимые директории проекта."""
        print("Заведомо существующие директории:")
        self._ensure_directory(self.file_dir, "Путь к директории с ipynb/py файлами", "file_dir")
        self._ensure_directory(self.sub_project_dir, "Путь к директории СубПроекта", "sub_project_dir")
        self._ensure_directory(self.project_dir, "Путь к директории Проекта", "project_dir")
        self._ensure_directory(self.parent_dir, "Путь к директории для доступа к библиотекам", "parent_dir")

        print("\nДиректории СубПроекта:")
        print("  Директории Исходных Данных:")

        self.input_log_data = self.project_dir / self.sub_project_dir.name / "input_data" / "input_log_data"
        self.input_temp_data = self.project_dir / self.sub_project_dir.name / "input_data" / "input_temp_data"
        self.input_samples_data = self.project_dir / self.sub_project_dir.name / "input_data" / "input_samples"

        self._ensure_directory(self.input_log_data, "Путь к каталогу с логами исходных файлов", "input_log_data")
        self._ensure_directory(self.input_temp_data, "Путь к каталогу с временными файлами", "input_temp_data")
        self._ensure_directory(self.input_samples_data, "Путь к каталогу с примерами", "input_samples_data")

        print(" Директории Данных полученных в процессе работы скрипта:")

        self.output_log_data = self.project_dir / self.sub_project_dir.name / "output_data" / "output_log_data"
        self.output_temp_data = self.project_dir / self.sub_project_dir.name / "output_data" / "output_temp_data"
        self.directory_data_set = self.project_dir / "data_set"

        self._ensure_directory(self.output_log_data, "Путь к каталогу с логами выходных файлов", "output_log_data")
        self._ensure_directory(self.output_temp_data, "Путь к каталогу с временными файлами", "output_temp_data")
        self._ensure_directory(self.directory_data_set, "Путь к каталогу с Файлами Постоянных Конфигураций", "directory_data_set")

    def _add_libraries_to_sys_path(self):
        """Добавляет папку libraries_py в sys.path."""
        lib_path_str = str(self.libraries_path)
        if lib_path_str not in sys.path:
            sys.path.append(lib_path_str)
            print(f"\n✅ Каталог {lib_path_str} успешно добавлен в sys.path")
        else:
            print(f"\n✅ Каталог {lib_path_str} уже присутствует в sys.path")

    # Удобные свойства для доступа
    @property
    def input_data(self):
        return self.project_dir / self.sub_project_dir.name / "input_data"

    @property
    def output_data(self):
        return self.project_dir / self.sub_project_dir.name / "output_data"

"""
project_paths.py
Описание:
Модуль project_paths.py содержит класс ProjectConfig, который отвечает за централизованное управление структурой директорий проекта. Он автоматически определяет иерархию папок и создаёт все необходимые директории для корректной работы приложения.

Основные возможности

Автоматическое определение уровней проекта:
file_dir — директория текущего скрипта
sub_project_dir — директория субпроекта
project_dir — корневая директория проекта
parent_dir — родительская директория (для общих библиотек)

Автоматическое создание и проверка всех необходимых папок:
input_data/
input_log_data/ — исходные логи
input_temp_data/ — временные входные данные
input_samples/ — примеры и сэмплы

output_data/
output_log_data/ — выходные логи и результаты
output_temp_data/ — временные выходные файлы

data_set/ — файлы постоянных конфигураций и датасетов

Добавление папки libraries_py в sys.path для удобного импорта общих библиотек.
Удобные свойства .input_data и .output_data.


Пример использования
Pythonfrom project_paths import ProjectConfig

config = ProjectConfig()

# Доступ к путям
print(config.input_log_data)
print(config.output_data)
print(config.input_samples_data)

# Использование
log_file = config.output_log_data / "processing_log.txt"
sample = config.input_samples_data / "example.csv"
"""