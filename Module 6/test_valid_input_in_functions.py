import unittest
from validate_input_in_functions import score_input


class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertTrue(score_input("hello") == {'hello': 0})
        self.assertTrue(score_input("fred") == {'fred': 0})

        
if __name__ == '__main__':
    test_score_input_test_name()
