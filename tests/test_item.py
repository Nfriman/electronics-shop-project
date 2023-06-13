import pytest

from src.item import *


def test_item():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'

    item3 = Item('Xiaomi', 20000, 10)
    assert item1 + item3 == 30

    item1.name = 'комп'
    assert item1.name == 'комп'

    item2 = Item.all[0]
    assert item2.name == 'комп'

    assert Item.string_to_number('5') == 5

    # Item.instantiate_from_csv()
    #assert len(Item.all) == 7
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path="нет такого файла")

    # @staticmethod string_to_number
    try:
        item1.name = "ZZZZZZZZZZZZZZZZ"
    except Exception as e:
        assert str(e) == "Длина наименования товара превышает 10 символов."

