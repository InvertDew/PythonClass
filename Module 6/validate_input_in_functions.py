#!/usr/bin/env python3
import time

"""
Program: validate_input_in_functions.py
Author: Justin Oglesby
Last date modified: 6/18/2020
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    :param test_name: incoming string
    :param n: test_score: optional integer representing test score
    :param test_score optional invalid message
    :returns: object with test_name and test_score
    """
    if test_score < 0 or test_score > 100:
        return invalid_message
    print('Test name:', test_name)
    return { test_name: test_score }


if __name__ == '__main__':
    print(score_input("test"))
    time.sleep(30)