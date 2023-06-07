from src.keyboard import *

def test_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert repr(kb) == "KeyBoard('Dark Project KD87A', 9600, 5)"

    kb2 = KeyBoard('samsung_key', 10000, 10)
    kb2.change_lang()
    assert kb + kb2 == 15

    assert str(kb.language) == "EN"
    assert str(kb2.language) == 'RU'

