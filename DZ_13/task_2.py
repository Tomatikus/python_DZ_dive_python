




class Animal:
    def __init__(self, name, age):
        self.name = name.title()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
        name: str,
        age: int = 5,
        color: str = 'черная',
        breed: str = 'колли',
        is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'{self.name} {self.color} {self.breed} домашняя'
        return f'{self.name} {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
        age: int,
        name: str = 'СуперКот',
        number_heads: int = 2) -> None:
        super().__init__(name, age)
        self.name = name
        self.__number_heads = number_heads

    def __str__(self):
        return f'{self.name} -> number_heads: {self.__number_heads},\
        Возраст: {self.age}'


class Fish(Animal):

    def __init__(self, name:str = 'Клоун', age: int = 3, aqua:str = 'морская', size: str = 'маленькая'):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'
        
class Fabric(Animal):
    def __init__(self, animal_type: str, name: str, age: int = 4):
        super().__init__(name, age)
        self.type = animal_type
        self.name = name

    def animal_fabric(animal_type, name):
        if animal_type == 'Fish':
            return Fish(name)
        elif animal_type == 'Dog':
            return Dog(name)
        elif animal_type == 'Kotopes':
            return Kotopes(name)
        


if __name__ == "__main__":
    dog = Dog('Бобик', 3, "рыжий", "спаниель")
    dog2 = Dog('Тузик', 4, "серый", "спаниель", False)
    f1 = Fish("Дори", 1, True, 0.5)
    kt1 = Kotopes(3, "Котопес", 2)
    fab = Fabric('Dog', 'Кузя')
    print(dog)
    print(kt1)
    kt1.birthday()
    print(kt1)
    print(Fabric.animal_fabric('Dog', 'Кузя'))
    print(Fabric.animal_fabric('Fish', 'Зубатка'))
    print(Fabric.animal_fabric('Kotopes', 5))
