# Задача 1
# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transform(matrix:dict):
    return [list(row) for row in zip(*matrix)]

matrix = [[1, 2, 3], [4, 5, 6]]

print(transform(matrix))