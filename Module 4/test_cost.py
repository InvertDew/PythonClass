import unittest
from nested_if_statements import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        print(type(float(calculate_price(8, 5, 10))))
        print(10 > float(calculate_price(8, 5, 10)))
        self.assertTrue(10.00 > calculate_price(8, 5, 10)),
        self.assertTrue(10.00 > calculate_price(8, 5, 15)),
        self.assertTrue(10.00 > calculate_price(8, 5, 20)),
        self.assertTrue(10.00 > calculate_price(8, 10, 10)),


if __name__ == '__main__':
    test_price_under_ten()
