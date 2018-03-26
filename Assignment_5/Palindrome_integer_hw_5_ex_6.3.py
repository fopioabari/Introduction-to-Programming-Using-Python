#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:08:09 2018

@author: francisabari
"""

# Return the reversal of an integer, e.g. reverse(456) returns
# 654
def reverse(number):
    reversed_number = 0
    while number > 0:
        reversed_number *= 10
        reversed_number += number % 10
        number //= 10
    return reversed_number

# Return true if number is a palindrome
def isPalindrome(number):
    return number == reverse(number)


def main():
    num = int(input('Enter a number: '))
    if isPalindrome(num):
        print(str(num) + ' is a palindrome')
    else:
        print(str(num) + ' is not a palindrome')
main()
