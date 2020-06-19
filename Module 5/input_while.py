#!/usr/bin/env python3
import time

"""
Program: while_loop.py
Author: Justin Oglesby
Last date modified: 6/14/2020
"""


def main():
    numbers = []
    num = 0
    done = None
    num = int(input("Enter a number between 1 and 100 (1111 to finish list): "))
    while num != 1111:
        while num < 1 or num > 100:
            num = int(input("Please re-enter your number to be between 1 and 100 (1111 to finish list): "))
        numbers.append(num)
        num = int(input("Enter a number between 1 and 100 (1111 to finish list): "))
    for n in numbers:
        print(n)
    time.sleep(30)


if __name__ == '__main__':
    main()


#With the first logic you can only enter one number into list and the program ends
#Had a little bit of a hard time getting the logic to line up where it needed to for the while loops to work correctly

