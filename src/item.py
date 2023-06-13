import csv
import os



class InstantiateCSVError(Exception):
    pass


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине."""
        super().__init__()
        self.pay = None
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Выводит имя товара"""
        return f"{self.name}"

    def __add__(self, other):
        """Суммирует цены товаров"""
        if issubclass(self.__class__, Item):
            return self.quantity + other.quantity
        else:
            var = None

    @property
    def name(self):
        """ Геттер приватнного атрибута name """
        return self.__name

    @name.setter
    def name(self, name):
        """ сеттер name проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(name) > 10:
            raise Exception('Длина наименования товара превышает 10 символов.')
        self.__name = name

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.:return: Общая стоимость товара."""
        self.all_price = self.price * self.quantity
        return self.all_price

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price = int(self.pay_rate * self.price)

    @classmethod
    def instantiate_from_csv(cls, path):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        os.chdir('..')
        try:
            file_csv = os.path.join("src", path)
            with open(file_csv, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for index in reader:
                        item = []
                        item.append(index['name'])
                        item.append(index['price'])
                        item.append(index['quantity'])
                        cls.all.append(item)
                except KeyError:
                    raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')


    @staticmethod
    def string_to_number(number):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(number))


