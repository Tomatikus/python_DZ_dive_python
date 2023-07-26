# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке 
# не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

numbers = [1, 2, 3, 1, 2, 4, 5]
result = []

UNIQ_TICK = 1
for nums in numbers:
    if nums not in result and numbers.count(nums) > UNIQ_TICK:
        result.append(nums)
print(result)