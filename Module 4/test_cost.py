import unittest
from nested_if_statements import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertTrue(10.00 > calculate_price(8, 5, 10)),
        self.assertTrue(10.00 > calculate_price(8, 5, 15)),
        self.assertTrue(10.00 > calculate_price(8, 5, 20)),
        self.assertTrue(10.00 > calculate_price(8, 10, 10)),

    def test_price_under_between_thirty_fifty(self):
        print(calculate_price(10, 5, 10))
        self.assertTrue(10 <= calculate_price(10, 5, 10) < 30)
        self.assertTrue(10 <= calculate_price(15, 10, 15) < 30)
        self.assertTrue(10 <= calculate_price(20, 10, 20) < 30)
        self.assertTrue(10 <= calculate_price(29, 10, 10) < 30)

if __name__ == '__main__':
    test_price_under_ten()
    test_price_under_between_thirty_fifty()
