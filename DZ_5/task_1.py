# Задача 1
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх 
# элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path): # Функция разделения пути к файлу на элементы
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension

# Пример использования функции
absolute_path = "/home/user/documents/example.txt"
path, filename, extension = split_file_path(absolute_path)
print("Path:", path)
print("Filename:", filename)
print("Extension:", extension)