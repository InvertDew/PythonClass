#!/usr/bin/env python3

"""
Program: basic_for_loop.py
Author: Justin Oglesby
Last date modified: 6/14/2020
"""


def main():
    numbers = [5.00, 8.00, 12.00, 15.00, 17.00, 20.00, 21.00, 23.00, 25.00, 28.00]
    for x in numbers: 
        print(x)
    print("")
    odd_nums = []
    for y in range(33, 100):
        if (y % 2) != 0:
            odd_nums.append(y)
    odd_nums.sort(reverse=True)
    for n in odd_nums:
        print(n)

if __name__ == '__main__':
    main()
