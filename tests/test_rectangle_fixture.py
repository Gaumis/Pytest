import pytest
import  source.shapes as shapes

#refer test_rectangle.py file, where you had to create rectangle object every time for functional test.
@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def wried_rectangle():
    return shapes.Rectangle(5,6)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 2 * (10+20)

def test_not_equal(my_rectangle, wried_rectangle):
    assert my_rectangle != wried_rectangle