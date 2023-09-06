from task_3 import Matrix

mat1 = Matrix([[1, 2], [4, 5]])
mat2 = Matrix([[2, 1], [3, 4]])
# matrix3 = Matrix([[1,2,3], [5, 4]])

print(mat1)
print()
print(mat2)
print()
# print(matrix3) # Выведет ошибку: raise ValueError("Количество строк должно быть равным")
print(mat1 == mat2)
print()
print(mat1 * mat2)
print()
print(mat1 + mat2)

