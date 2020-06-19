import unittest
from validate_input_in_functions import score_input


class FunctionTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertTrue(score_input("hello") == {'hello': 0})
        self.assertTrue(score_input("fred") == {'fred': 0})

    def test_score_input_test_score_valid(self):
        self.assertTrue(score_input("hello", 33) == {'hello': 33})
        self.assertTrue(score_input("fred", 77) == {'fred': 77})

    def test_score_input_test_score_below_range(self):
        self.assertTrue(score_input("hello", -55) == 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        self.assertTrue(score_input("hello", 155) == 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertTrue(score_input("hello", "&^*D&") == 'Invalid test score, try again!')
        
if __name__ == '__main__':
    test_score_input_test_name()
    test_score_input_test_score_valid()
    test_score_input_test_score_below_range()
    test_score_input_test_score_above_range()
    test_test_score_non_numeric()
