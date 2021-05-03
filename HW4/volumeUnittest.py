import unittest
import volumeOfCube

class TestVolume(unittest.TestCase):

    def test_int(self):
        self.assertEqual(volumeOfCube.volume(sdmaishf98),3)
    def test_neg(self):
        self.assertRaises(Exception,volumeOfCube.volume,-8)
    def test_ok(self):
        self.assertEqual(volumeOfCube.volume(2),8)

if __name__ == '__main__':
    unittest.main()