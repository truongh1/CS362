import unittest
import test_palindrome

class Test(unittest.TestCase):

    def test_str(self):
        self.assertEqual(test_palindrome.palindrome("YamaY"), True)  #True means it is a palindrome
        self.assertEqual(test_palindrome.palindrome("Hello World"), True)


if __name__ == '__main__':
    unittest.main()
