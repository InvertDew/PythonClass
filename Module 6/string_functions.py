#!/usr/bin/env python3
import time

"""
Program: string_functions.py
Author: Justin Oglesby
Last date modified: 6/18/2020
"""


def multiply_string(message, n):
    """
    :param message: incoming string
    :param n: number of times to duplicate message
    :returns: message concatanted to itself n times
    """
    return message * n


if __name__ == '__main__':
    print(multiply_string("Hello", 3))
    time.sleep(30)