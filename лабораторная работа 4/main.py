if __name__ == "__main__":
    # Write your solution here

    class Dog:
        """ Базовый класс собаки. """
        def __init__(self, name: str, age: int, weight: float, coat_color: str) -> None:
            """
                   Создание и подготовка к работе объекта "Собака"
                   :param name: Имя собаки
                   :param age: Сколько полных лет собаки, в годах
                   :param weight: Вес собаки, в кг
                   :param coat_color: Цвет шерсти
                   Примеры:
                   >>> some_dog = Dog("Paul", 2, 12, "ginger")  # инициализация экземпляра класса
            """
            self._name = name
            self._age = age
            self._weight = weight
            self._coat_color = coat_color

        def __str__(self) -> str:
            return f"Кличка собаки: {self._name}, " \
                   f"возраст: {self._age}, " \
                   f"вес: {self._weight}, " \
                   f"цвет шерсти: {self._coat_color}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(" \
                   f"name={self._name!r}, " \
                   f"age={self._age}, " \
                   f"age={self._weight}, " \
                   f"coat_color={self._coat_color!r}" \
                   f")"

        def eat(self) -> None:
            """
                Функция - собака ест
                Примеры:
                >>> some_dog = Dog("Paul", 2, 12, "ginger")
                >>> some_dog.eat()
            """
            print("Собака ест")

        def bark(self, volume: str) -> None:
            """
                Функция - собака гавкает сказанной громкостью
                :param volume: громкость лая, субьективая оценка
                Примеры:
                >>> some_dog = Dog("Paul", 2, 12, "ginger")
                >>> some_dog.bark()
            """
            print(f"Собака {volume} лает")

        def jump(self, height: float) -> None:
            """
                Функция - собака прыгает на указанную величину
                :param height: высота прыжка, в метрах
                Примеры:
                >>> some_dog = Dog("Paul", 2, 12, "ginger")
                >>> some_dog.jump(1.5)
            """
            print(f"Собака прыгает на {height} метров")

        def get_name(self) -> str:
            """
                Функция - переопределенный сеттер для свойства name
                :return: Имя собаки
                Примеры:
                >>> some_dog = Dog("Paul", 2, 12, "ginger")
                >>> some_dog._name
            """
            return f"Имя собаки: {self._name}"


    class Pitbull(Dog):
        """ Дочерний класс собаки - собака породы Питбуль. """
        def __init__(self, name: str, age: int, weight: float, coat_color: str, banned_in_current_country: bool) -> None:
            """
                  Создание и подготовка к работе объекта "Собака"
                  :param name: Имя собаки
                  :param age: Сколько полных лет собаки, в годах
                  :param weight: Вес собаки, в кг
                  :param coat_color: Цвет шерсти
                  :param banned_in_current_country: запрещена ли собака в текущей стране, bool
                  Примеры:
                  >>> some_pitbull = Pitbull("Paul", 2, 12, "ginger", False)  # инициализация экземпляра класса
            """
            super().__init__(name, age, weight, coat_color)
            self._banned_in_current_country = banned_in_current_country

        def __str__(self) -> str:
            return f"Кличка собаки: {self._name}, " \
                   f"возраст: {self._age}, " \
                   f"вес: {self._weight}, " \
                   f"цвет шерсти: {self._coat_color}, " \
                   f"запрещена в текущей стране: {self._banned_in_current_country}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(" \
                   f"name={self._name!r}, " \
                   f"age={self._age}, " \
                   f"age={self._weight}, " \
                   f"coat_color={self._coat_color!r}, " \
                   f"banned_in_current_country={self._banned_in_current_country}" \
                   f")"


    pass
