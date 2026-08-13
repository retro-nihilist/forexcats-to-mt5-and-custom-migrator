# -------------------------------------------------------------------------------------------------------------------------------------------
# Реализация методов работы с сервером MT5 по API <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

import MT5Manager as mt5m                 # подключаем библиотеку
import pandas as pd                     # Чтение файла с содержимым дата фрейма
import time
import datetime                      # подключаем библиотеку для работы с датами
from datetime import datetime, timezone

# Функция для импорта словаря со значениями <<<<<<<<<<<<<<<<<<<
from read_dict_from_text_file import read_dict_from_text_file  

# Создание словаря Кредов из файла >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
levels_up = 1  # Нужно подняться на 2 уровня вверх
file_relative_path = "credits\\mt5.text"  # Файл в корне проекта
credits_dict_mt5manager = read_dict_from_text_file(levels_up, file_relative_path)
# print(credits_dict_mt5manager)

def mt_5_manager():
    return mt5m

def mt5admin():
    global admin
    admin = mt5m.AdminAPI()                                           # создаем администраторский интерфейс
    return admin

def mt5manager():
    global manager
    manager = mt5m.ManagerAPI()                                       # создаем менеджерский интерфейс
    return manager

def admin_connect(credits_list = credits_dict_mt5manager):
    print("MT5admin connect:",   mt5admin().Connect(credits_list["server_mt5_ip_port"], credits_list["manager_mt5_login"], credits_list["manager_mt5_password"]))
    return admin
    
def manager_connect(credits_list = credits_dict_mt5manager, pump_mode = 0):
    print("MT5manager connect:", mt5manager().Connect(credits_list["server_mt5_ip_port"], credits_list["manager_mt5_login"], credits_list["manager_mt5_password"], pump_mode))
    return manager

def admin_disconnect(admin_connect):
    admin = admin_connect
    result_admin_disconnect = admin.Disconnect()
    print("admin.Disconnect()", result_admin_disconnect)          # отключаемся от сервера
    return admin_disconnect

def manager_disconnect(manager_connect):
    manager = manager_connect
    result_manager_disconnect = manager.Disconnect()
    print("manager.Disconnect()", result_manager_disconnect)  # отключаемся от сервера
    return manager_disconnect

"""
def admin_connect_with_control(admin = None):
    print("Объект mt5admin:", admin)
    try: # Проверяем отсутствие подключения МТ5                            
        admin_disconnect(admin)
        print("Присутствовало не завешенное соединение MT5 администратор")
    except: print("Соединяемся  MT5 администратор; подключаемся к серверу")

    admin = mt5admin()
    return admin"""

def admin_connect_with_control(admin = None):
    #print("Объект mt5admin:", admin)
    try: # Проверяем отсутствие подключения МТ5                            
        admin_disconnect(admin)
        print("Присутствовало не завешенное соединение MT5 администратор")
    except: print("Соединяемся  MT5 администратор; подключаемся к серверу")
    admin = admin_connect()
    return admin


def admin_disconnect_with_control(admin):
    if admin_disconnect(admin) is not None:                                                 # Отключаемся
        print("Успешное разъединение MT5 администратор")
        del admin
        return True
    else:
        print("MT5 администратор Разъединение не удалось")
        return False        


def manager_connect_with_control(manager = None, pump_mode = None):
    print("Объект mt5manager:", manager, "Режим пампинга:", pump_mode)
    try: # Проверяем отсутствие подключения МТ5                            
        manager_disconnect(manager)
        print("Присутствовало не завешенное соединение MT5 менеджер")
    except: print("Соединяемся  MT5 менеджером; подключаемся к серверу")

    manager = mt5manager()
    if  pump_mode == 'POSITIONS':
        print("подключение в режиме пампинга EnPumpModes.PUMP_MODE_POSITIONS)")
        manager = manager_connect(pump_mode = manager.EnPumpModes.PUMP_MODE_POSITIONS)
    elif pump_mode == 'SYMBOLS':
        print("подключение в режиме пампинга EnPumpModes.PUMP_MODE_SYMBOLS)")
        manager = manager_connect(pump_mode = manager.EnPumpModes.PUMP_MODE_SYMBOLS)
    elif pump_mode == 'USERS':
        print("подключение в режиме пампинга EnPumpModes.PUMP_MODE_USERS)")
        manager = manager_connect(pump_mode = manager.EnPumpModes.PUMP_MODE_USERS)
    else:
        print("Режим пампинга не установлен")
        manager = manager_connect()
    return manager

def manager_disconnect_with_control(manager):
    if manager_disconnect(manager) is not None:                                                 # Отключаемся
        print("Успешное разъединение MT5 менеджер")
        del manager
        return True
    else:
        print("Разъединение не удалось MT5 менеджер")
        return False


# Получение информации по торговым инструментам <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
def symbol_array_attributes(symbol_array, attributes, attributes_last_tick):
    import warnings
    # symbol_array - массив символов, полученный из метода SymbolRequestArray()
    symbol_update_data = pd.DataFrame(columns=attributes)

    manager = mt5manager()                                                        # создаем менеджерский интерфейс
    manager = manager_connect(pump_mode = manager.EnPumpModes.PUMP_MODE_SYMBOLS)
    if manager:
        print("manager.SelectedAddAll() = ", manager.SelectedAddAll())
        print("manager.SelectedTotal() = ", manager.SelectedTotal())
        time.sleep(1)                                                                           # Пауза
        for a in symbol_array:                                                                  # Перебираем элементы массива
            symbol_data = {}                                                                    # Пустой словарь для хранения строки
            for attr in attributes:                                                             # Перебираем атрибуты из списка
                symbol_data[attr] = getattr(a, attr, None)                                      # записываем атрибут и значение None, если атрибут отсутствует
                if attr == attributes[0]:                                                       # Если атрибутом является имя символа
                    last_tick = manager.TickLastRaw(getattr(a, attr, None))                     # Создаём объект
                    for atr_last_tick in attributes_last_tick:                                  # Перебираем атрибуты TickLastRaw 

                        

                        symbol_data[atr_last_tick] = getattr(last_tick, atr_last_tick, None)
                        if atr_last_tick == attributes_last_tick[0]:                            # Если Атрибутом является Время получения последней котировки
                            s_last_tick_datetime = getattr(last_tick, atr_last_tick, None)
                            utc_time = datetime.fromtimestamp(s_last_tick_datetime, timezone.utc) if last_tick else None
                                                                                                # Проверяем перед вызовом метода replace()
                            if utc_time is not None:
                                utc_time = utc_time.replace(tzinfo=None)                        # Убираем временную зону
                                utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')               # Преобразуем в строку 'YYYY-MM-DD HH:MM:SS'
                            else:
                                utc_time = None
                            """
                            utc_time = utc_time.replace(tzinfo=None)                    # Убираем временную зону (т.е. "+00:00")
                            utc_time = utc_time.strftime('%Y-%m-%d %H:%M:%S')     # Преобразуем время в строку в формате 'YYYY-MM-DD HH:MM:SS'"""

                            symbol_data[atr_last_tick] = utc_time        # записываем атрибут и значение None, если атрибут отсутствует

            print(symbol_data)
            new_row = pd.DataFrame([symbol_data])

            # symbol_update_data = pd.concat([symbol_update_data, new_row], ignore_index=True)    # Добавляем новую строку в DataFrame с использованием pd.concat()
            """— уже учитывает все необходимые случаи:
            new_row is not None — проверяет, что объект вообще существует;
            not new_row.empty — не пустой DataFrame;
            not new_row.isna().all(axis=None) — не вся строка из NaN."""
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=FutureWarning, message="The behavior of DataFrame concatenation.*")
                if new_row is not None and not new_row.empty and not new_row.isna().all(axis=None): symbol_update_data = pd.concat([symbol_update_data, new_row], ignore_index=True)
                else:
                    print("❌ ERROR: new_row is None or empty or all NaN")

            del new_row
            del last_tick
        manager.SelectedDeleteAll()                                                             # Удаление всех символов из списка выбранных
    print("manager.Disconnect() = ", manager.Disconnect())
    return symbol_update_data
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для проведения балансовой операции <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def balance_deal(user_login, balance_transactions, deal_action, comment, Description_action):   # Функция для обработки балансовой транзакции
    print(f"Функция 💰 Балансовой Сделки: {Description_action}")
    iter = 0
    seconds_delay = 0.01
    deal_id = -1
    error_mt5 = "NOT error"
    while (deal_id < 1) | (error_mt5 == "(-1, <EnMTAPIRetcode.MT_RET_ERR_NETWORK: 7>, 'Network error')"):
        if seconds_delay > 400:  
            print(f"❌ ERROR: {Description_action}; Превышено время ожидания [{seconds_delay}] секунд; Выход из цикла. ❌")
            break                           # Прерываем цикл после 60 секунд
        if iter > 0:
            print(f"ЗАдержка перед .DealPerform(deal){Description_action} [{seconds_delay}] секунд")
            time.sleep(seconds_delay)
            seconds_delay *= 2

        balance_result = manager.DealerBalance(user_login, balance_transactions, deal_action, comment)
        print(f"🎭 {user_login}; balance_result = {balance_result}")

        if balance_result == False:
            error_mt5 = mt5m.LastError()                                              #OPEN IN DIALS 
            print(f"❌ ERROR: {Description_action};",  mt5m.LastError())
        else:
            #pos_id  = deal.PositionID                                               # Фиксируем номер позиции на стороне MT5
            deal_id = balance_result                                                    # фиксируем номер СДЕЛКИ на стороне MT5
            print(f"✅ SUCCESS: {Description_action};", deal_id)
            #del deal
        iter +=1
    return balance_result
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для проведения балансовой операции <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def process_deal(user_login, balance_transactions, deal_action, comment):                       # Функция для обработки балансовой транзакции.
    return manager.DealerBalance(user_login, balance_transactions, deal_action, comment)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""# Функция Для массового пополнения / снятия методом коррекции с указанием даты <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def balance_0 (acc_set, summ0, date0, Description_action,  deal_action = mt5m.MTDeal.EnDealAction.DEAL_CORRECTION):
    # acc_set   -   Список счетов;
    #summ0      -   Сумма пополнения;
    #date0      -   Дата, которая устанавливается в транзакцию (после совершения оной)

    error_balance_0_list = []
    error_update_0_list = []
    balance_0_list = []

    print(f"Количество аккаунтов для нулевого пополнения на [{summ0}]: {len(acc_set)}")

    manager = manager_connect()
    if manager:
        for a in acc_set:
            user = mt5m.MTUser(manager)
            user.Login = a
            comment = str(summ0)

            deal_id = process_deal(user.Login, summ0, deal_action, comment, Description_action)
            
            if deal_id:
                deal = manager.DealRequest(deal_id)
                deal.Time = date0                           # Время 2023 06 01 00 00 00
                deal.TimeMsc = date0 *1000
                update_result = manager.DealUpdate(deal)

                if update_result > 1:
                    print(f"{a}, Ошибка при обновлении сделки: {mt5m.LastError()}")
                    error_update_0_list.append(a)
                else:
                    balance_0_list.append(a)  # Добавляем логин с успешным пополнением
            else:
                print(f"{a}, Ошибка при создании сделки: {mt5m.LastError()}")
                error_balance_0_list.append(a)  # Добавляем логин с неудачным пополнением

            del user  # Освобождаем ресурсы для пользователя

    else: print(f"{a}, ERROR manager.Connect()): {mt5m.LastError()}")

    print(f"manager_Disconnect() = {manager.Disconnect()}") 

    print(f"Количество неуспешных ПОПОЛНЕНИЙ [{summ0}]: {len(error_balance_0_list)} \n {error_balance_0_list}")
    print(f"Количество неуспешных ОБНОВЛЕНИЙ [{summ0}]: {len(error_update_0_list)} \n {balance_0_list}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
# Функция Для массового пополнения / снятия методом коррекции с указанием даты <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def balance_0 (acc_set, summ0, date0, Description_action):
    print(f"Функция Для массового пополнения / снятия методом коррекции с указанием даты ")
            # acc_set - Список счетов;
                        #summ0 - Сумма пополнения;
                                #date0 - Дата, которая устанавливается в транзакцию (после совершения оной)
    error_balance_0_list = []
    error_update_0_list = []
    balance_0_list = []
    print(f"Количество аккаунтов для нулевого пополнения на [{summ0}]: {len(acc_set)}")

    manager = manager_connect()
    if manager:

        for a in acc_set:
            user = mt5m.MTUser(manager)
            user.Login = a
            deal_action = mt5m.MTDeal.EnDealAction.DEAL_CORRECTION
            comment = str(summ0)

            deal_id = balance_deal(user.Login, summ0, deal_action, comment, Description_action)
            
            if deal_id:
                deal = manager.DealRequest(deal_id)
                deal.Time = date0                           # Время 2023 06 01 00 00 00
                deal.TimeMsc = date0 *1000
                update_result = manager.DealUpdate(deal)

                if update_result > 1:
                    print(f"{a}, Ошибка при обновлении сделки: {mt5m.LastError()}")
                    error_update_0_list.append(a)
                else:
                    balance_0_list.append(a)  # Добавляем логин с успешным пополнением
            else:
                print(f"❌ {a}, Ошибка при создании сделки: {mt5m.LastError()}")
                error_balance_0_list.append(a)  # Добавляем логин с неудачным пополнением

            del user  # Освобождаем ресурсы для пользователя

    else: print(f"❌ ERROR manager.Connect()): {mt5m.LastError()}")

    print(f"manager_Disconnect() = {manager.Disconnect()}") 

    len_error_balance_0_list = len(error_balance_0_list)
    len_error_update_0_list  = len(error_update_0_list)

    if len_error_balance_0_list > 0 | len_error_update_0_list > 0:
        print(f"❌ Количество неуспешных ПОПОЛНЕНИЙ [{summ0}]: {len_error_balance_0_list} \n {error_balance_0_list}")
        print(f"❌ Количество неуспешных ОБНОВЛЕНИЙ [{summ0}]: {len_error_update_0_list} \n {error_update_0_list}")
    else:
        print(f"✅ SUCCESS: Все операции по ПОПОЛНЕНИЮ прошли успешно")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""# Функция для проведения балансовой операции <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
def process_deal(user_login, balance_transactions, deal_action, comment):                       # Функция для обработки балансовой транзакции.
    return manager.DealerBalance(user_login, balance_transactions, deal_action, comment)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
# Извлечение массива торговых инструментов <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def getting_array_trading_instruments(symbols_list="*"):    # Работает но не понятно почему т.к. не указан параметр pump_mode
    print("[def] Функция получения массива торговых инструментов", "[getting_array_trading_instruments]")
    # mask
    # [in]  Один или несколько символов через запятую. Имя символа должно быть указано полностью, включая путь. Например, Forex\EURUSD.
    # Для получения имени символа используется метод IMTConSymbol::Symbol. Символы также можно указать в виде маски "*" (любое значение) и "!" (исключение). 
    # Например, Forex\*,!Forex\EURUSD — все символы в подгруппе Forex, кроме EURUSD.
    # Максимальная длина маски составляет 512 символа (с признаком конца строки).

    print("<getting_array_trading_instruments>: symbols_list = ", symbols_list)

    if manager_connect():  
        print(f"SymbolTotal = {manager.SymbolTotal()}")                     # Количество Торговых инструментов на сервере
        symbol_array = manager.SymbolRequestArray(symbols_list)             # Запрашиваем массив торговых инструментов
        try:
            print("len_symbol_array = ", len(symbol_array))         # выводим количество элементов в массиве
        except:
            print(f"Невозможно определить длину массива по запросу По запросу <SymbolRequestArray({symbols_list})>")
            print(f"Error: {mt5m.LastError()}")

        print("manager.Disconnect() = ", manager.Disconnect())
    else: print(f"Error: {mt5m.LastError()}")
    return symbol_array
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""
# Извлечение массива торговых инструментов <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
def getting_array_trading_instruments(symbols_list="*"):
    print("<getting_array_trading_instruments>: symbols_list = ", symbols_list)
    if manager_connect():
        print(f"SymbolTotal = {manager.SymbolTotal()}")         # Количество Торговых инструментов на сервере
        symbol_array = manager.SymbolRequestArray(symbols_list) # Запрашиваем массив всех торговых инструментов

        try:
            print("len_symbol_array = ", len(symbol_array))         # выводим количество элементов в массиве
        except:
            print(f"Невозможно определить длину массива по запросу По запросу <SymbolRequestArray({symbols_list})>")
            print(f"Error: {MT5Manager.LastError()}")

        print("manager.Disconnect() = ", manager.Disconnect())
    else: print(f"Error: {MT5Manager.LastError()}")
    return symbol_array"""




# Обновление массива торговых инструментов <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def symbol_update_batch(symbol_array):
    print("Функция обновления массива торговых инструментов, элементов в массиве:", len(symbol_array))
    if admin_connect():

        print("SymbolUpdateBatch = ", admin.SymbolUpdateBatch(symbol_array))

        print("admin.Disconnect() = ", admin.Disconnect())
    else: print(f"Error: {mt5m.LastError()}") 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def last_error_id(error_mt5):
    import re
    match = re.search(r":\s*(\d+)>", error_mt5)  # Ищем число после ":" и перед ">"
    if match:
        extracted_number = int(match.group(1))  # Преобразуем в int
        print(f"LastError_id = {extracted_number}")
        return extracted_number
    else:
        print(f"❌ ERROR: Число не найдено")

# СОЗДАНИЕ позиции <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def creating_position(Description_action, deal, MT5Manager):
    #deal = MT5Manager.MTDeal(manager)
    print(f"Функция Создания позиции: {Description_action}")
    iter = 0
    seconds_delay = 0.01
    deal_id = -1
    error_mt5 = "NOT error"
    error_mt5_short = "NOT error"
    while ((deal_id < 1) or (error_mt5_short == 'Network error')) and (error_mt5_short != 'Position already closed'):
        if seconds_delay > 400:  
            print(f"❌ ERROR: {Description_action}; Превышено время ожидания [{seconds_delay}] секунд; Выход из цикла. ❌")
            break                           # Прерываем цикл после 60 секунд
        if iter > 0:
            print(f"ЗАдержка перед .DealPerform(deal){Description_action} [{seconds_delay}] секунд")
            time.sleep(seconds_delay)
            seconds_delay *= 2
        if not manager.DealPerform(deal):
            error_mt5 = MT5Manager.LastError()
            error_mt5_short = error_mt5[2]                                              
            print(f"⚠️ ERROR: {Description_action};",  error_mt5, error_mt5_short)
        else:
            #pos_id  = deal.PositionID                                               # Фиксируем номер позиции на стороне MT5
            deal_id = deal.Deal                                                     # фиксируем номер СДЕЛКИ на стороне MT5
            print(f"✅ SUCCESS: {Description_action};", deal.Print())
            #del deal
        iter +=1
    return deal, deal_id
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Функция для проверки и исправления позиций <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def positioncheck_and_positionfix(acc_set):
    print(f"[ def ] positioncheck_and_positionfix (Проверка и исправление позиций)")
    pos_check_len_df = pd.DataFrame()
    iter_0   = len(acc_set)
    iter_for = 0
    for i in acc_set:
        iter_for += 1
        pos_check = admin.PositionCheck(i)          # Список итогов проверки корректности позиций клиента 
        pos_check_current   = list(pos_check[0])    # Массив текущих позиций клиента
        pos_check_invalid   = list(pos_check[1])    # позиции, параметры которых не совпадают с фактическими
        pos_check_missed    = list(pos_check[2])    # позиции клиента, которых нет среди фактических позиций / недостающие позиции.
        pos_check_nonexist  = list(pos_check[3])    # помещаются лишние позиции клиента
        #df = pd.DataFrame([{attr: getattr(obj, attr) for attr in dir(obj) if not attr.startswith("__")} for obj in pos_check[0]])
        #imported["pd_set_option"]("объект массива сделок", df, 30)

        pos_fix = admin.PositionFix(i)                  # Корректируем ПОЗИЦИИ на основании СДЕЛОК
        if pos_fix is not False:
            print(f"✅ iter [{iter_for}];   осталось", iter_0 - iter_for, f"; Login [{i}], [PositionFix] выполнена без ошибок")
        else: print(f"❌ ERROR [ PositionFix ]: {imported["mt_5_manager"]().LastError()}")

        pos_check_len_list = []                             # Список для генерирования ДФ с итогами PositionCheck
        pos_check = admin.PositionCheck(i)
        row = {"acc": i, 
                "[current]"     : len(pos_check_current),       # Длинна массива текущих позиций
                "[invalid]"     : len(pos_check_invalid),       # Длинна массива ошибочных позиций
                "[missed]"      : len(pos_check_missed),        # Длинна массива недостающих позиций
                "[nonexist]"    : len(pos_check_nonexist),      # Длинна массива лишних позиций
                "[current_fix]" : len(pos_fix)}                 # Массив позиций клиента после корректировки по истории
        pos_check_len_list.append(row)

        new_row_df = pd.DataFrame(pos_check_len_list)
        pos_check_len_df = pd.concat([pos_check_len_df, new_row_df], ignore_index=True)

    return pos_check_len_df
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def mt5_connect_with_control(admin, manager, return_admin = False, return_manager = False, pump_mode = False):
    print(f"Функция подключения к MT5: return_admin = {return_admin}; return_manager = {return_manager}")
    #admin = None
    #manager = None
    if return_admin   == True: admin = admin_connect_with_control(admin)
    if return_manager == True: manager = manager_connect_with_control(manager, pump_mode = pump_mode)

    if (return_admin == True and admin is None) or (return_manager == True and manager is None):
        print("❌ Ошибка: соединение с MT5.")
        if return_admin   == True and admin   is None: print(f"❌ ERROR: admin = {admin}")
        if return_manager == True and manager is None: print(f"❌ ERROR: manager = {manager}")
        return None, None
    else: return admin, manager

def mt5_disconnect_with_control(admin, manager, return_admin = False, return_manager = False):
    print(f"\n Функция ОТКЛЮЧЕНИЯ от MT5: return_admin = {return_admin}; return_manager = {return_manager}")
    if return_admin == True: 
        if admin_disconnect_with_control(admin): del admin
        else: print("❌ ERROR: разъединение [ mt5admin ] c сервером НЕ удалось.")
    if return_manager == True: 
        if manager_disconnect_with_control(manager): del manager
        else: print("❌ ERROR: разъединение [ mt5manager ] c сервером НЕ удалось.")



# Функция для обработки ошибок MT5 <<
def mt5_error(Description_action):
    import MT5Manager
    error_mt5 = MT5Manager.LastError()
    error_mt5_short = error_mt5[2]                                              
    print(f"❌ ERROR: {Description_action};",  error_mt5, error_mt5_short)