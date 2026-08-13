# Установка SWOP в открытую позицию по ID сделки IN
    # account_id    login mt5 пользователя, служит для логирования в отправке запроса не задействован;
    # deals_swap    размер SWOP;
    # deal_id       id сделки на стороне МТ5;
    # manager       объект соединения mt5manager c mt5server;
    # MT5Manager    создание объекта МТ5

def update_swop_open_position(account_id,  deals_swap,  deal_id, manager, MT5Manager, print_on = False):

    import time

    print(f"def установки SWOP в ОТКРЫТУЮ позицию; счёт {account_id}, MT5 сделка {deal_id}")
    """account_id  = row["account_id"]
    deals_swap  = row["deals_swap"]
    deal_id     = row["open_deals_id"]"""

    # модуль принудительной остановки выполнения кода <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    on_break = "N"
    #on_break    = str(input(f"deals_swap = {deals_swap}, deal_i = {deal_id}, Ввдите значение on_break ="))
    if (on_break == "Y") | ( on_break == "y"):
        print(f"Введено значение on_break = {on_break} => STOP перебора ДФ и обновления SWOP")
        return
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    error_txt = "Нет Ошибки"                                                                            # Сбрасываем переменную ошибки МТ5
    deal      = manager.DealRequest(deal_id)

    if (deal is not None) and (deal != False):
        if print_on == True: print(f"SUCCESS: объект сделки {deal_id} СУЩЕСТВУЕТ")
        pos_id = deal.PositionID                                                                        # Фиксируем номер позиции на стороне MT5
        if print_on == True and pos_id > 0: print(f"SUCCESS: сделке {deal_id} соответствует позиция {pos_id}")
        try:                                                                                            # модуль повторного запроса позиции по iD сделки IN  
            seconds_delay = 0                                                                           # Принудительная задержка для получения информации о позиции
            pos = False
            while pos == False:
                if seconds_delay > 6:
                    error_txt = f"❌ ERROR: SWOP позиции [{pos_id}] по mt5 сделке [{deal_id}] не обновлён; Превышено время ожидания [{seconds_delay}] секунд; Выход из цикла."
                    if print_on == True: print(error_txt)
                    break                                                                               # Прерываем цикл
                if  seconds_delay > 0:                                                                  # Выводим текущую ошибку, повлекшую неудачу
                    if print_on == True: print(f"❌ ERROR: SWOP {deals_swap} не установлен в позицию {pos_id}, {MT5Manager.LastError()} следующая попытка через {seconds_delay} секунд.")
                time.sleep(seconds_delay)
                pos = manager.PositionGetByTicket(pos_id)                                               # Создаём объект позиции
                seconds_delay += 0.01
                seconds_delay *= 2
                                                    
            if pos:                                                                                     # объект существующей позиции создан
                if print_on == True: print(f"SUCCESS: объект Открытой позиции по мт5 сделке {deal_id} создан")
                pos_storage = pos.Storage
                if pos.Storage > 0:                                                                     # Проверка Отсутствия установленного SWOP
                    if print_on == True: print(f"SWOP позиции [{pos_id}] по mt5 сделке [{deal_id}] отличен от Нуля и равен [{pos_storage}]")

                pos.Storage = deals_swap                                                                # Устанавливаем SWOP в объект позиции
                if deals_swap == pos.Storage:
                    if print_on == True: print(f"✅ SUCCESS: SWOP [{deals_swap}] установлен в ОБЪЕКТ позиции [{pos_id}] по сделке mt5  [{deal_id}")

                    if not manager.PositionUpdate(pos):                                                 # Если SWOP не обновлён
                        error_txt = f"❌ ERROR: manager_connect.PositionUpdate({pos_id}); SWOP {deals_swap} НЕ установлен; {MT5Manager.LastError()}"
                        if print_on == True: print(error_txt)
                        raise Exception("❌ ERROR: SWOP. Position update failed")
                    else:
                        print(f"✅ SUCCESS: SWOP позиции [{pos_id}] по mt5 сделке [{deal_id}] ОБНОВЛЁН [{pos.Storage}]")
                else:
                    if print_on == True: print(f"❌ ERROR: SWOP {deals_swap} НЕ установлен в объект позиции [{pos_id}] по mt5 сделке [{deal_id}")
            else:
                error_txt = f"❌ ERROR: manager_connect.PositionGetByTicket({pos_id}); объект позиции не создан"
                if print_on == True: print(error_txt)

        except Exception as exception_error:
                error_txt = f"❌ ERROR: {exception_error}, SWOP {deals_swap} не установлен в позицию {pos_id}, {MT5Manager.LastError()}; Объект сделки .DealRequest({deal_id}) Не Создан"
                if print_on == True: print(error_txt)
    else:  
        error_txt = f"❌ ERROR:.DealRequest({deal_id}), {MT5Manager.LastError()}"
        if print_on == True: print(error_txt)
    
    try: del deal
    except: print (f"❌ ERROR: счёт {account_id},  Объект  mt5 сделки {deal_id} не был создан")
    try: del pos
    except: print (f"❌ ERROR: счёт {account_id},  Объект ПОЗИЦИИ mt5 сделки {deal_id} не был создан")
        
    return error_txt

# Тесты:
