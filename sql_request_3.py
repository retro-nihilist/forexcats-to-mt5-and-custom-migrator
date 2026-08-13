# Новая версия, указывается файл с кредами для доступа к  SQL базе
    # Предполагается, указывать полное имя файла относительно корня проэкта
    # Предполагается указывать количество уровней н которые нужно поднятся относительно текущего файла

# levels_up -- Нужно подняться на заданное количество  уровней вверх

from urllib.parse import quote
import pandas as pd
from urllib.parse import quote_plus

"""
#pip install SQLAlchemy PyMySQL pandas предпочитает работать с соединениями через SQLAlchemy или sqlite3
#from sqlalchemy import create_engine
# Создание движка подключения через SQLAlchemy"""
from sqlalchemy import create_engine

# Функция для импорта словаря со значениями <<<<<<<<<<<<<<<<<<<
from read_dict_from_text_file import read_dict_from_text_file  

# Создание словаря Кредов из файла >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
def created_dict_sql_from_file(file_relative_path, levels_up):
    credits_dict_sql = read_dict_from_text_file(levels_up, file_relative_path)
    db_config = credits_dict_sql
    connection_string = f"mysql+pymysql://{quote(db_config['user'])}:{quote(db_config['password'])}@{db_config['host']}/{db_config['database']}"
    #print(connection_string)
    return connection_string


def create_engine_def(file_relative_path, levels_up):
    connection_string = created_dict_sql_from_file(file_relative_path, levels_up)
    engine = create_engine(connection_string)
    return engine"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Создание ДФ из SQL запроса <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def pd_read_sql(query, file_relative_path, levels_up, params=None):
    credits_dict_sql = read_dict_from_text_file(levels_up, file_relative_path)
    db_config = credits_dict_sql

    user = quote_plus(db_config['user'])
    password = quote_plus(db_config['password'])
    host = db_config['host']
    database = db_config['database']


    connection_string = f"mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8mb4"
    engine = create_engine(connection_string)


    return pd.read_sql(query, engine, params=params)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

