import unittest
import fizzBuzz

class TestFizzBuzz(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(fizzBuzz.fizzBuzz(4), '4')

    def test_case2(self):
        self.assertEqual(fizzBuzz.fizzBuzz(3), "Fizz")

    def test_case3(self):
        self.assertEqual(fizzBuzz.fizzBuzz(20), "Buzz")

    def test_case4(self):
        self.assertEqual(fizzBuzz.fizzBuzz(15), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()