#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:06:22 2018

@author: francisabari
"""

def main():
    num = eval(input("Enter an integer:"))
    print("Sum of digits in", num, "is:", sumDigits(num))
    
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return(n%10) + sumDigits(n//10)
        
main()


        