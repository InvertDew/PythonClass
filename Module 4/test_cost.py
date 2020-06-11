import unittest
from nested_if_statements import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertTrue(calculate_price(8, 5, 10)),
        self.assertTrue(calculate_price(8, 5, 15)),
        self.assertTrue(calculate_price(8, 5, 20)),
        self.assertTrue(calculate_price(8, 10, 10)),


if __name__ == '__main__':
    test_price_under_ten()
