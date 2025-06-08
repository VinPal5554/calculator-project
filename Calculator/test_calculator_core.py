import pytest
import calculator_core as calc

def test_add():
    assert calc.add(3, 2) == 5
    assert calc.add(-1, -1) == -2

def test_subtract():
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(0, 5) == -5

def test_multiply():
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 100) == 0

def test_divide():
    assert calc.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_exponentiate():
    assert calc.exponentiate(2, 3) == 8

def test_modulus():
    assert calc.modulus(10, 3) == 1

def test_floor_divide():
    assert calc.floor_divide(7, 2) == 3
    with pytest.raises(ValueError):
        calc.floor_divide(7, 0)