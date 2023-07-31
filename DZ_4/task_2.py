# Задача 2
# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение 
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. 
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def new_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result [str(value)] = key
    return(result)

print(new_dict(a=[1,2,3], b=4, c='5'))