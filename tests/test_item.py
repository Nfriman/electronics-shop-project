from src.item import *


def test_item():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000