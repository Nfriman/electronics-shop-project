import csv
import os


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине."""
        self.pay = None
        self.__name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    @property
    def name(self):
        ''' Геттер приватнного атрибута name'''
        return self.__name

    @name.setter
    def name(self, name):
        """ сеттер name проверяет, что длина наименования товара не больше 10 симвовов"""
        if len(name) > 10:
            raise  Exception("Длина наименования товара превышает 10 символов.")
        self.__name = name

    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.:return: Общая стоимость товара."""
        self.all_price = self.price * self.quantity
        return self.all_price

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара."""
        self.price = int(self.pay_rate*self.price)

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        os.chdir('..')
        file_csv = os.path.join("src", "items.csv")
        with open(file_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.all.append(row)

    @staticmethod
    def string_to_number(number):
        """статический метод, возвращающий число из числа-строки"""
        return int(float(number))




