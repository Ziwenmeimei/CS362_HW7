import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.isLeap(400),"Leap year")

    def test2(self):
        self.assertEqual(leapyear.isLeap(100),"Not leap year")

    def test3(self):
        self.assertEqual(leapyear.isLeap(8),"Leap year")

if __name__ == '__main__':
    unittest.main(verbosity=2)