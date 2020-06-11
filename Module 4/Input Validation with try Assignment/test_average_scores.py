import unittest
from average_scores import average

class FunctionTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90,80, 78)

if __name__ == '__main__':
    test_average_exception()

