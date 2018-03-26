#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:33:12 2018

@author: francisabari
"""

def displaySortedNumber(num1, num2, num3):
    print ("The sorted numbers are "),
    if num1>num2:
        num1, num2 = num2, num1;
    if num2>num3:
        num2, num3 = num3, num2;
    if num1>num2:
        num1, num2 = num2, num1;
    print (num1, num2, num3)

num1, num2,num3 = map(float, input('Enter three numbers: ').split(','))
displaySortedNumber(num1, num2, num3);
       