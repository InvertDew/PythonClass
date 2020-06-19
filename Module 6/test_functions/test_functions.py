import unittest
from string_functions import multiply_string


class FunctionTestCase(unittest.TestCase):
    def test_multiple_string (self):
        self.assertTrue(multiply_string("Hello", 3) == "HelloHelloHello")

if __name__ == '__main__':
    test_multiple_string()
