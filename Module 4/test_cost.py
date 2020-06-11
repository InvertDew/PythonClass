import unittest
from nested_if_statements import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertTrue(10.00 > calculate_price(8, 5, 10)),
        self.assertTrue(10.00 > calculate_price(8, 5, 15)),
        self.assertTrue(10.00 > calculate_price(8, 5, 20)),
        self.assertTrue(10.00 > calculate_price(8, 10, 10)),

    def test_price_under_between_ten_thirty(self):
        self.assertTrue(10 <= calculate_price(10, 5, 10) < 30)
        self.assertTrue(10 <= calculate_price(15, 10, 15) < 30)
        self.assertTrue(10 <= calculate_price(20, 10, 20) < 30)
        self.assertTrue(10 <= calculate_price(29, 10, 10) < 30)

    def test_price_under_between_thirty_fifty(self):
        self.assertTrue(30 <= calculate_price(30, 5, 10) < 50)
        self.assertTrue(30 <= calculate_price(35, 10, 15) < 50)
        self.assertTrue(30 <= calculate_price(45, 10, 20) < 50)

if __name__ == '__main__':
    test_price_under_ten()
    test_price_under_between_ten_thirty()
    test_price_under_between_thirty_fifty()