#!/usr/bin/env python3
import time

"""
Program: average_scores.py
Author: Justin Oglesby
Last date modified: 6/10/2020
"""


def average(score_1, score_2, score_3):
    return (score_1 + score_2 + score_3) / 3


def get_info():
    first_name = input("What is your first name : ")
    last_name = input("What is your last name : ")
    age = int(input("What is your age : "))
    score_1 = int(input("What is your first score out of 100 : "))
    score_2 = int(input("What is your second score out of 100 : "))
    score_3 = int(input("What is your third score out of 100 : "))
    user_average = average(score_1, score_2, score_3)
    print(last_name + ',', first_name, 'age:', age, 'average grade: ', round(user_average, 2))

def main():
    get_info()
    time.sleep(30)


if __name__ == '__main__':
    main()
