from urllib.parse import quote
import pandas as pd

# Функция для импорта словаря со значениями <<<<<<<<<<<<<<<<<<<
from read_dict_from_text_file import read_dict_from_text_file  

# Создание словаря Кредов из файла >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
levels_up = 1  # Нужно подняться на 2 уровня вверх
file_relative_path = "credits\\sql.text"  # Файл в корне проекта
credits_dict_sql = read_dict_from_text_file(levels_up, file_relative_path)
# print(credits_dict_mt5manager)

db_config = credits_dict_sql

connection_string = f"mysql+pymysql://{quote(db_config['user'])}:{quote(db_config['password'])}@{db_config['host']}/{db_config['database']}"
#print(connection_string)

"""
#pip install SQLAlchemy PyMySQL pandas предпочитает работать с соединениями через SQLAlchemy или sqlite3
#from sqlalchemy import create_engine
# Создание движка подключения через SQLAlchemy"""
from sqlalchemy import create_engine
def create_engine_def():
    engine = create_engine(connection_string)
    return engine
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Создание ДФ из SQL запроса <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def pd_read_sql(query, params=None):
    engine = create_engine_def()
    return pd.read_sql(query, engine, params=params)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>