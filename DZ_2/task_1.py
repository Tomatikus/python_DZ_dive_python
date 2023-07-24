# Задача 1
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX_DICT = { 10: 'A', 11: 'B', 
        12: 'C', 13: 'D', 
        14: 'E', 15: 'F'
}

HEX_DIV = 16

num = int(input("Введите число: "))

progres_num = num
result = " "

while progres_num > 0:
    result += HEX_DICT.get(progres_num % HEX_DIV, str(progres_num % HEX_DIV))
    progres_num //= HEX_DIV
result = result[::-1]

print(result, hex(num))