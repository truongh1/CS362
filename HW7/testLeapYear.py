import unittest
import leapYear

class TestCase(unittest.TestCase):
    # 2021 is not a leap year
    def test_case1(self):
        self.assertEqual(leapYear.isLeapYear(2021), False)

    # 2020 is a leap year
    def test_case2(self):
        self.assertEqual(leapYear.isLeapYear(2020), True)

    # check for negative
    def test_case3(self):
        self.assertRaises(ValueError, leapYear.isLeapYear, -1920)

    #check for string
    def test_case4(self):
        self.assertEqual(TypeError, leapYear.isLeapYear, "anufansaajf")

    if __name__ == '__main__':
        unittest.main()