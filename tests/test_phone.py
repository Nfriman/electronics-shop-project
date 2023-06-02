from src.phone import *

def test_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    assert phone1 + phone1 == 10

    try:
        phone1.number_of_sim = 0
    except Exception as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."

    item1 = Item('mi5', 10000, 10)
    assert phone1 + item1 == 15

