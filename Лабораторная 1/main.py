# TODO Написать 3 класса с документацией и аннотацией типов


class Cookie:
    def __init__(self, width_volume: float, height_volume: float):
        """
        Создание и подготовка к работе объекта "Печенька"
        :param width_volume: Ширина переньки, в см
        :param height_volume: Высота печеньки, в см
        Примеры:
        >>> cookie = Cookie(5, 5)  # инициализация экземпляра класса
        """
        if not isinstance(width_volume, (int, float)):
            raise TypeError("Ширина печеньки должна быть типа int или float")
        if not isinstance(height_volume, (int, float)):
            raise TypeError("Высота печеньки должна быть типа int или float")
        if width_volume <= 0:
            raise ValueError("Ширина печеньки должна быть положительным числом")
        self.width_volume = width_volume
        if height_volume <= 0:
            raise ValueError("Ширина печеньки должна быть положительным числом")
        self.height_volume = height_volume

    def cookie_is_cooked(self) -> bool:
        """
        Функция, которая позволяет проверить готовность печеньки
        :return: Готова ли печенька
        Примеры:
        >>> cookie = Cookie(5, 5)
        >>> cookie.cookie_is_cooked()
        """
        ...

    def add_filling_to_cookie(self, filling: float) -> None:
        """
        Добавление начинки в печеньку.
        :param filling: объем добавляемой начинки, в мл
        :raise ValueError: Если начинки слишком много для печеньки -возвращаем ошибку
        Примеры:
        >>> cookie = Cookie(5, 5)
        >>> cookie.add_filling_to_cookie(10)
        """
        if not isinstance(filling, (int, float)):
            raise TypeError("Добавляемая начинка должна быть типа int или float")
        if filling < 0:
            raise ValueError("Добавляемая начинка должна быть положительным числом")
        ...

    def dip_cookie_in_tea(self, immersion_depth: float) -> None:
        """
        Мокнуть печеньку в чай.
        :param immersion_depth: Глубина погружения печеньки
        :raise ValueError: Если глубина погружения не в том типе данных или указано отрицательное значение
        Примеры:
        >>> cookie = Cookie(5, 5)
        >>> cookie.dip_cookie_in_tea(200)
        """
        if not isinstance(immersion_depth, (int, float)):
            raise TypeError("Глубина погружения должна быть типа int или float")
        if immersion_depth < 0:
            raise ValueError("Глубина погружения должна быть положительным числом")
        ...


class Grape:
    def __init__(self, number_of_berries: int, branch_weight: float):
        """
        Создание и подготовка к работе объекта "Виноград"
        :param number_of_berries: Число ягод на ветке, в шт
        :param branch_weight: Вес ветки, в граммах
        Примеры:
        >>> grape = Grape(23, 500)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_berries, int):
            raise TypeError("Количество ягод должно быть int")
        if not isinstance(branch_weight, (int, float)):
            raise TypeError("Вес винограда должен быть типа int или float")
        if number_of_berries <= 0:
            raise ValueError("Количество ягод долно быть положительным числом")
        self.number_of_berries = number_of_berries
        if branch_weight <= 0:
            raise ValueError("Вес ягод должен быть положительным числом")
        self.branch_weight = branch_weight

    def is_berries_fresh(self) -> bool:
        """
        Функция, которая позволяет проверить свежесть ягод
        :return: Ягоды не протухли
        Примеры:
        >>> grape = Grape(23, 500)
        >>> grape.is_berries_fresh()
        """
        ...

    def get_number_of_bones(self) -> int:
        """
        Узнать количество косточек.
        :return: Киолличество косточек
        Примеры:
        >>> grape = Grape(23, 500)
        >>> grape.get_number_of_bones()
        """
        ...

    def add_berries(self, number_of_berries: float) -> None:
        """
        Добавить еще ягод.
        :param number_of_berries: количество дополнительных ягод
        :raise ValueError: Если колличество ягод не в том типе данных или указано отрицательное значение
        Примеры:
        >>> grape = Grape(23, 500)
        >>> grape.add_berries(50)
        """
        if not isinstance(number_of_berries, (int, float)):
            raise TypeError("Глубина погружения должна быть типа int или float")
        if number_of_berries < 0:
            raise ValueError("Глубина погружения должна быть положительным числом")
        ...


class Elf:
    def __init__(self, weight_volume: float, height_volume: float):
        """
        Создание и подготовка к работе объекта "Эльф"
        :param weight_volume: Вес эльфа, в кг
        :param height_volume: Высота эльфа, в см
        Примеры:
        >>> elf = Elf(60, 170)  # инициализация экземпляра класса
        """
        if not isinstance(weight_volume, (int, float)):
            raise TypeError("Вес эльфа должна быть типа int или float")
        if not isinstance(height_volume, (int, float)):
            raise TypeError("Высота эльфа должна быть типа int или float")
        if weight_volume <= 0:
            raise ValueError("Вес эльфа должен быть положительным числом")
        self.weight_volume = weight_volume
        if height_volume <= 0:
            raise ValueError("Высота эльфа должна быть положительным числом")
        self.height_volume = height_volume

    def elf_has_sharp_ears(self) -> bool:
        """
        Функция, которая позволяет узнать остроухий ли эльф
        :return: Острые ли уши
        Примеры:
        >>> elf = Elf(60, 170)
        >>> elf.elf_has_sharp_ears()
        """
        ...

    def jump(self, jump_height: float) -> None:
        """
        Эльф прыгает на указанную высоту.
        :param jump_height: высота прыжка, в см
        :raise ValueError: Если высота прыжка не в том типе данных или указано отрицательное значение
        Примеры:
        >>> cookie = Cookie(5, 5)
        >>> cookie.add_filling_to_cookie(10)
        """
        if not isinstance(jump_height, (int, float)):
            raise TypeError("Высота прыжка должна быть типа int или float")
        if jump_height < 0:
            raise ValueError("Высота прыжка должна быть положительным числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()

