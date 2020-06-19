#!/usr/bin/env python3
import time

"""
Program: input_while_exit.py
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
            if num == 1111:
                break
        numbers.append(num)
        num = int(input("Enter a number between 1 and 100 (1111 to finish list): "))
        if num == 1111:
            break
    for n in numbers:
        print(n)
    time.sleep(30)


if __name__ == '__main__':
    main()


#Honestly had to fudge this, I believe my project was working how it needed to before adding the break

