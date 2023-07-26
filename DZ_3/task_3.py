# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


from itertools import combinations

def generate_combinations(items, max_weight):
    '''Аргументы: items - словарь (список) вещей с указанием веса
       max_weight - максимальный вес который можно поднять в рюкзаке
       Возвращает: list - список вещей, которые могут войти в рюкзак
    '''   
    items_list = list(items.items())
    all_combinations = []
    
    for r in range(2, len(items_list) + 1):
        for combination in combinations(items_list, r):
            total_weight = sum(weight for _, weight in combination)
            if total_weight <= max_weight:
                all_combinations.append((total_weight, [item for item, _ in combination]))

    # Сортировка комбинаций по общему весу в порядке убывания
    all_combinations.sort(key=lambda x: x[0], reverse=True)

    return all_combinations

items = {
    "Палатка": 4, "Вода": 3, "Еда": 2, "аптечка": 0.5, 
    "носки": 0.1, "фонарик": 0.2, "спальный мешок": 2, "карта": 0.2, "компас": 1, 
    "ножи": 0.7, "котелок": 2, "мини плита": 3, "дождевик": 0.2
}
max_weight = 15
combinations = generate_combinations(items, max_weight)

# Отображаем 10 лучших комбинаций
for i, (total_weight, items) in enumerate(combinations[:10], start=1):
    print(f"{i}. Общий вес вещей: {total_weight} кг, Комплектация рюкзака: {items}")