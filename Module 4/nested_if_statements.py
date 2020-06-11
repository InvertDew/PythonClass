#!/usr/bin/env python3
import time

"""
Program: nested_if_statements.py
Author: Justin Oglesby
Last date modified: 6/10/2020
"""


def calculate_price(price, cash_coupon, percent_coupon):
    shipping = calculate_shipping(price)
    grand_total = 0
    if cash_coupon == "NA":
        cash_coupon = 0
    else:
        cash_coupon = int(cash_coupon)
    if percent_coupon == "NA":
        percent_coupon = 0
    else:
        percent_coupon = int(percent_coupon)
    grand_total = price - cash_coupon
    grand_total = grand_total - ((percent_coupon / 100) * grand_total)
    return "%.2f" % grand_total


def calculate_shipping(price):
    shipping = 0
    if price < 10:
        shipping = 5.95
    elif 10 <= price < 30:
        shipping = 7.95
    elif 30 <= price < 50:
        shipping = 11.95
    else:
        shipping = 0
    return shipping


def main():
    bad_coupon = True
    bad_discount = True
    bad_amount = True
    cash_coupon = 0
    discount_percent = 0
    coupons = ["5", "10", "NA"]
    discounts = ["10", "15", "20", "NA"]
    while bad_amount:
        try:
            amount = float(input("What is your purchase amount : "))
            bad_amount = None
        except ValueError:
            print("Invalid input, please enter a number")
    while bad_coupon:
        try:
            cash_coupon = input("What is your cash coupon amount(5, 10, NA) : ")
            coupon_set = set(coupons)
            if cash_coupon in coupon_set:
                bad_coupon = None
        except ValueError:
            print("Invalid input, please enter a number")
    while bad_discount:
        try:
            discount_percent = input("What is your discount percentage(10, 15, 20, NA) : ")
            discount_set = set(discounts)
            if discount_percent in discount_set:
                bad_discount = None
        except ValueError:
            print("Invalid input, please enter a percentage")
    grand_total = calculate_price(amount, cash_coupon, discount_percent)
    print(grand_total)
    time.sleep(30)


if __name__ == '__main__':
    main()
