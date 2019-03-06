import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponent(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_factorial(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
    def test_integer_division(self):
        result = rpn.calculate("3 2 //")
        self.assertEqual(1, result)
    def test_percentage(self):
        result = rpn.calculate("72 + 5%")
        self.assertEqual(75.6, result)
    def test_bitwise_and(self):
        result = rpn.calculate("5 & 7")
        self.assertEqual(5, result)
    def test_bitwise_or(self):
        result = rpn.calculate("5 | 7")
        self.assertEqual(7, result)
    def test_bitwise_not(self):
        result = rpn.calculate("~ 5")
        self.assertEqual(-6, result)