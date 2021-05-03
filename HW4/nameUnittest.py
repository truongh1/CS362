import unittest
import nameGen

class TestName(unittest.TestCase):
    def test(self):
        self.assertEqual(nameGen.name("Hao", "Truong"), "Hao Truong")
        self.assertEqual(nameGen.name("sauea6d", "kajsu"),"")
        self.assertEqual(nameGen.name("Hao", "Truong"), "jajajas")