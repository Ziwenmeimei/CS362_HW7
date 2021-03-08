import unittest
import fizzbuzz

class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(fizzbuzz.fb(3),"Fizz")

    def test2(self):
        self.assertEqual(fizzbuzz.fb(5),"Buzz")

    def test3(self):
        self.assertEqual(fizzbuzz.fb(15),"FizzBuzz")


if __name__ == '__main__':
    unittest.main(verbosity=2)