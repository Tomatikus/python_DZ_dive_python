# Задача 3 
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все 
# операции поступления и снятия средств в список.


MAX_DEPOSTI_AMOUNT = 5000000
AMOUNT_DEVIDER = 50

class ATM:
    def __init__(self):
        # Старт работы

        self.balance = 0
        self.operation_count = 0

    def deposit(self, amount): 
        # Внесение денег
        
        if amount % AMOUNT_DEVIDER != 0:
            return "Сумма должна быть кратна - 50"
        
        if self.balance > MAX_DEPOSTI_AMOUNT:
            self.balance -= self.balance * 0.1
        self.balance += amount
        self.operation_count += 1
        self.add_interest()
        return self.balance

    def withdraw(self, amount): 
        # Снятие денег
        
        if amount % AMOUNT_DEVIDER != 0:    
            return "Сумма должна быть кратна - 50"
        fee = max(min(amount * 0.015, 600), 30)

        if amount + fee > self.balance:
            return "Insufficient balance"
        
        if self.balance > MAX_DEPOSTI_AMOUNT:
            self.balance -= self.balance * 0.1
        self.balance -= amount + fee
        self.operation_count += 1
        self.add_interest()
        return self.balance

    def add_interest(self):

        if self.operation_count % 3 == 0:
            self.balance += self.balance * 0.03

atm = ATM()
print(atm.deposit(10050))
print(atm.withdraw(150))
print(atm.withdraw(100))
print(atm.deposit(500))
print(atm.withdraw(350)) 
print(atm.withdraw(150))