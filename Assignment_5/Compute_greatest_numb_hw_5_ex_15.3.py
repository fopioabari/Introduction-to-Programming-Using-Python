#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:13:40 2018

@author: francisabari
"""
def main():
    num1, num2 = eval(input("Enter two integers:"))
    print("GCD of", num1, "and", num2,"is:", gcd(num1, num2))
    
def gcd(m, n):
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n)    
main()
  