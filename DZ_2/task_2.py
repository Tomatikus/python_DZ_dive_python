# Задача 2
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

from fractions import Fraction

frac1_str = input("Введите первую дробь через '/' :")
frac2_str = input("Введите вторую дробь через '/' :")

# Преобразуем дроби из строк в числа
numerator1, denominator1 = map(int, frac1_str.split("/"))
numerator2, denominator2 = map(int, frac2_str.split("/"))

def process_fractions(frac1_str, frac2_str):

    # Вычисляем сумму дробей
    sum_frac_numerator = numerator1 * denominator2 + numerator2 * denominator1
    sum_frac_denominator = denominator1 * denominator2
    sum_frac = (sum_frac_numerator, sum_frac_denominator)

    # Вычисляем произведение дробей
    prod_frac_num = numerator1 * numerator2
    prod_frac_denominator = denominator1 * denominator2
    prod_frac = (prod_frac_num, prod_frac_denominator)

    return sum_frac, prod_frac


check_num1 = Fraction(numerator1, denominator1)
check_num2 = Fraction(numerator2, denominator2)

sum_frac, prod_frac = process_fractions(frac1_str, frac2_str)

print(f"Сумма дробей: {sum_frac[0]}/{sum_frac[1]}")
print(f"Произведение дробей: {prod_frac[0]}/{prod_frac[1]}")
print(f"""Через Fraction:
      Сумма: {check_num1 + check_num2}
      Произведение: {check_num1 * check_num2}
      """)
