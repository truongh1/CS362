import pytest
import test_palindrome

def test_str1():
    assert test_palindrome.palindrome("racecar") == True # True means it is a palindrome -> This should return a success

def test_str2():
    assert test_palindrome.palindrome("Hello World!") == False   # False means it is not a palindrome -> this should return a success
