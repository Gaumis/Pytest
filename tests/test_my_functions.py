import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(10, 5)
    assert result == 15

def test_add_negative_number():
    result = my_functions.add(10, -5)
    assert result == 5

def test_add_both_negative_number():
    result = my_functions.add(-10, -5)
    assert  result == 15

def test_add_strings():
    result = my_functions.add("I like ", "you")
    assert result == "I like you"

def test_divide():
    result = my_functions.divide(10,5)
    assert result == 3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10,0)
