import unittest
import katas
import math


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(1 , 3), 1 + 3)  

    def test_multiply(self):
        self.assertEqual(katas.multiply(4, 4), 4 * 4)

    def test_power(self):
        self.assertEqual(katas.power(2, 6), math.pow(2, 6))

    def test_factorial(self):
        self.assertEqual(katas.factorial(3), math.factorial(3))

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(9), 21)


if __name__ == '__main__':
    unittest.main()
