# Дополнительное:
# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

# Словарь с именами друзей и кортежами вещей
friends_dict = {
    "John": ("tent", "flashlight", "food", "water", "clothes"),
    "Mary": ("tent", "food", "water", "map", "compass"),
    "Steve": ("matches", "flashlight", "water", "clothes", "sunscreen"),
    "Lenny": ("Umbrella", "flashlight", "food", "water", "clothes"),
}

# Преобразуем кортежи вещей в множества для удобства работы
friends_sets = {name: set(items) for name, items in friends_dict.items()}

# Вещи, которые взяли все три друга
all_items = set.intersection(*friends_sets.values())

# Вещи, которые уникальны для каждого друга
unique_items = {name: items - set.union(*(s for n, s in friends_sets.items() if n != name)) 
                for name, items in friends_sets.items()}

# Вещи, которые есть у всех друзей, кроме одного
one_missing_items = {name: (set.union(*(s for n, s in friends_sets.items() if n != name)) - items) 
                     for name, items in friends_sets.items()}

print(f'Все други: {all_items},\n Уникальные вещи: {unique_items}, \n Взял один: {one_missing_items}')