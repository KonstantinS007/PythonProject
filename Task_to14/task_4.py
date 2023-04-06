import pytest

c = 1

def compare_two_numbers(a, b):
    global c
    if a > b:
       c = 0
    return c


def test_compare_two_numbers(a, b):
    assert compare_two_numbers(a, b) == 0
    var = False
    if not var:
       print("Тест успешен")

test_compare_two_numbers(57, 15)
