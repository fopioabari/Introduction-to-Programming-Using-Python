#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:45:23 2018

@author: francisabari
"""

import math
a = input("Enter the 'a' value: ")
b = input("Enter the 'b' value: ")
c = input("Enter the 'c' value: ")

a = float(a)
b = float(b)
c = float(c)

D = b**2 - 4*a*c
if D>0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("The roots are ",round(x1, 6), "and ", round(x2, 5))

elif D==0:
    x = -b/(2*a)
    print("The root is ",round(x))

else:
    print("The equation has no real roots")
    