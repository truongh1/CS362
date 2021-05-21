import pytest
import test_year

def test_case1():
    assert test_year.isLeapYear(2020) == True

def test_case2():
    assert test_year.isLeapYear(2021) == False

def test_case3():
    with pytest.raises(ValueError) as e:
        test_year.isLeapYear(-1920)
    assert str(e.value) == "Cannot be a negative year"

def test_case4():
    with pytest.raises(TypeError) as e:
        test_year.isLeapYear("hello")
    assert str(e.value) == "Cannot be a string!"
