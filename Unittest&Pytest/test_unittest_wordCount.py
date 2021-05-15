import unittest
import test_wordCount

class Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(test_wordCount.wordCount("Hello My name is Hao"), 5) #This should return a success

    def test_case2(self):
        self.assertEqual(test_wordCount.wordCount("Hahaha This is so funny!"),7) # This should return a failure

if __name__ == '__main__':
    unittest.main()