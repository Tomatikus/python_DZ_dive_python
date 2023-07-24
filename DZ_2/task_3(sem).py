#Задача 5(6 по семинару)

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# // После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# // При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
#ДЗ //

print('1. Пополнить счет.\n2. Cнять деньги со счета.\n3. Узнать баланс счета\n4. Закончить операции со счетом')

start_flag: bool = True

CASH: int = 0
LUXURY = 5000000
LUXURY_TAX = 0.9

COMMISSION = 0.015
COMMISSION_MAX = 600
COMMISSION_MIN = 30

operation_tax = 50
operation_count = 3
bonus_operation = 1.03

while start_flag:

    command: int = int(input("Действие: "))

    match command:
        case 1:
            if CASH >= LUXURY:
                CASH * LUXURY_TAX
            if operation_count % bonus_operation == 0:
                CASH *= bonus_operation
                print("Бонус за 3 операции")
            money = int(input("Введите сумму пополнения: "))
            if money % operation_tax == 0 and money > 0:
                CASH += money
            else:
                print("Неккоретный воод денег")
        case 2:
            if CASH >= LUXURY:
                CASH *= LUXURY_TAX
            
            if operation_count % bonus_operation == 0:
                CASH *= bonus_operation
                print("Бонус за 3 операции")

            money = int(input("Введите сумму снятия: "))
            if money * COMMISSION < CASH or money + COMMISSION_MIN < CASH:

                COMMISSION = money * COMMISSION
                if COMMISSION < COMMISSION_MIN:
                    COMMISSION = COMMISSION_MIN

                elif COMMISSION > COMMISSION_MAX:
                    COMMISSION = COMMISSION_MAX
                CASH = CASH - COMMISSION - money

                print("Остаток на счете: ", CASH)
            else:
                print("Недостаточно средств на счете")        
        case 3:
            print("Ваш баланс: ", CASH)  

        case 4:
            start_flag: bool = False

        case _:
            print("Введены некорректные данные")
