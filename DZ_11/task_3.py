# Задача 3. Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    '''
    Класс Матрица.
    '''
    def __init__(self,matrix):
        'определяем матрицу и проверяем на корректность'
        if len({len(row) for row in matrix}) != 1:
            raise ValueError("Количество строк должно быть равным")
        self.matrix = matrix
    
    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
    
    def __eq__(self, other):
        "Сравнение матриц"
        return self.matrix == other.matrix
    
    def __add__(self,other):
        "Сложение матриц"
        # This code is implementing the addition of two matrices.
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Размер матриц должен быть идентичен")
        
        result = [
            [self.matrix[i][j] + other.matrix[i][j] 
            for j in range(len(self.matrix[0]))]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)
    
    def __mul__(self, other):
        "Умножение двух матриц"
        # This code is implementing the multiplication of two matrices.
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк втротой матрицы")
        result = [
            [
                sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                for j in range(len(other.matrix[0]))
            ]
            for i in range(len(self.matrix))
        ]
        return Matrix(result)