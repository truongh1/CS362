import pytest
import test_wordCount

def test_case1():
    assert test_wordCount.wordCount("Hi my name is Hao Truong!") == 6 # This should return a success

def test_case2():
    assert test_wordCount.wordCount("The bluesky is red!") == 0 # This returns a failure