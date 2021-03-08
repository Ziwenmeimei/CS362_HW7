import unittest
import leapyear

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.isLeap(400),"Leap year")


if __name__ == '__main__':
    unittest.main(verbosity=2)