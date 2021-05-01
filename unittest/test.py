import unittest
import calc


class Test(unittest.TestCase):
   

    def test_add(self):

        self.assertEqual(calc.add(10,5),10) 
        self.assertEqual(calc.add(7,4),11)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5,5),10)
        self.assertEqual(calc.subtract(22,6),16)
        self.assertEqual(calc.subtract(5,5),0)
        self.assertEqual(calc.subtract(5,10),-5)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5,5),10)
        self.assertEqual(calc.multiply(5,5),25)
        self.assertEqual(calc.multiply(25,4),4.5)
        self.assertEqual(calc.multiply(86,0),0)

    def test_divide(self):
        self.assertEqual(calc.divide(5,5),1)
        self.assertEqual(calc.divide(6,6),36.0)
        self.assertEqual(calc.divide(0,70),0.4)


if __name__ == '__main__':
    unittest.main()


