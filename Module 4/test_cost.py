import unittest
from nested_if_statements import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertTrue(calculate_price(8, 5, 10))


if __name__ == '__main__':
    test_price_under_ten()
