# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.


class NameCheker:
    def __set_name__(self, owner, name):
        self._name = "_" + name # так тоже можно записать: "self._name = f"_{name}""

    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Имя должно начинаться с заглавной буквы и содержать только буквы.")
        setattr(instance, self._name, value)