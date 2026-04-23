from app import *

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_power():
    assert power(2, 3) == 8

def test_max_num():
    assert max_num(5, 3) == 5

def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False

def test_sqrt():
    assert sqrt_num(16) == 4.0