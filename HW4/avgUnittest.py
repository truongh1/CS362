import unittest
import avgList

class TestAverage(unittest.TestCase):
    def test_emptyList(self):
        self.assertEqual(avgList.avg([]),2)

    def test_negative(self):
        self.assertEqual(avgList.avg([2,2,-8]), 4)

    def test_result(self):
        self.assertEqual(avgList.avg(2,2,8),4)
