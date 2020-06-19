import unittest
from string_functions import multiply_string


class FunctionTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertTrue(multiply_string("Hello", 3) == "HelloHelloHello")
        self.assertTrue(multiply_string("Hello", 1) == "Hello")
        self.assertTrue(multiply_string("I", 5) == "IIIII")

        
if __name__ == '__main__':
    test_multiple_string()
