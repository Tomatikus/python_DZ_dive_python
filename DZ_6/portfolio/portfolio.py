# Задача 2

# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает 
# два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - 
# количество акций каждого символа. prices - словарь, где ключами являются символы акций, а значениями - текущая цена 
# каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен


STOCK_NOT_FOUND = "Stock not found"

def calculate_portfolio_value(stocks, prices):
    
    return sum(stocks[stock] * prices.get(stock, STOCK_NOT_FOUND) for stock in stocks)



# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float 
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля 
# акций. Функция должна вернуть процентную доходность портфеля.


def calculate_portfolio_return(initial_value, current_value):
    
    return ((current_value - initial_value) / initial_value) * 100


# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает 
# два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. Функция 
# должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. Начальная 
# стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить в защищенную переменную на 
# уровне модуля.

def get_most_profitable_stock(stocks, prices):

    profits = {stock: stocks[stock] * prices.get(stock, STOCK_NOT_FOUND) for stock in stocks}
    return max(profits, key=profits.get)