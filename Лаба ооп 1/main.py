import doctest

class Miata:

    def __init__(self, max_speed: float, capacity: int):
        """
        :param max_speed: Максимальная скорость транспортного средства.
        :param capacity: Вместимость транспортного средства.

        Примеры:
        >>> miata = Miata(120, 2)
        >>> miata.max_speed
        120
        >>> miata.capacity
        2
        """
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом.")

        self.max_speed = max_speed
        self.capacity = capacity

    def move(self, distance: float) -> float:
        """
        Рассчитывает время на преодоление заданной дистанции.

        :param distance: Дистанция, которую нужно преодолеть.
        :return: Время в часах.

        Примеры:
        >>> miata = Miata(120, 2)
        >>> miata.move(240)
        2.0
        """
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Дистанция должна быть положительным числом.")
        return distance / self.max_speed


class Tree:

    def __init__(self, height: float, age: int):
        """
        :param height: Высота дерева.
        :param age: Возраст дерева.

        Примеры:
        >>> tree = Tree(10.5, 5)
        >>> tree.height
        10.5
        >>> tree.age
        5
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.height = height
        self.age = age

    def photosynthesize(self) -> str:
        """
        Процесс фотосинтеза у дерева.

        :return: Сообщение о фотосинтезе.

        Примеры:
        >>> tree = Tree(10.5, 5)
        >>> tree.photosynthesize()
        'Дерево выполняет фотосинтез.'
        """
        return "Дерево выполняет фотосинтез."


class Telescope:

    def __init__(self, aperture: float, focal_length: float):
        """
        :param aperture: Диаметр апертуры телескопа (в миллиметрах).
        :param focal_length: Фокусное расстояние телескопа (в миллиметрах).

        Примеры:
        >>> telescope = Telescope(120, 600)
        >>> telescope.aperture
        120
        >>> telescope.focal_length
        600
        """
        if not isinstance(aperture, (int, float)) or aperture <= 0:
            raise ValueError("Апертура должна быть положительным числом.")
        if not isinstance(focal_length, (int, float)) or focal_length <= 0:
            raise ValueError("Фокусное расстояние должно быть положительным числом.")

        self.aperture = aperture
        self.focal_length = focal_length

    def magnification(self, eyepiece_focal_length: float) -> float:
        """
        Рассчитывает увеличение телескопа с заданным окуляром.

        :param eyepiece_focal_length: Фокусное расстояние окуляра (в миллиметрах).
        :return: Увеличение телескопа.

        Примеры:
        >>> telescope = Telescope(120, 600)
        >>> telescope.magnification(20)
        30.0
        """
        if not isinstance(eyepiece_focal_length, (int, float)) or eyepiece_focal_length <= 0:
            raise ValueError("Фокусное расстояние окуляра должно быть положительным числом.")
        return self.focal_length / eyepiece_focal_length

    def light_gathering_power(self) -> float:
        """
        Рассчитывает светособирающую способность телескопа относительно человеческого глаза (диаметр зрачка 7 мм).

        :return: Относительная светособирающая способность.

        Примеры:
        >>> telescope = Telescope(120, 600)
        >>> telescope.light_gathering_power()
        293.8775510204
        """
        pupil_diameter = 7  # диаметр зрачка в миллиметрах
        return round((self.aperture / pupil_diameter) ** 2, 10)

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
