#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:20:48 2018

@author: francisabari
"""

a,b,c,d,e,f =eval(input("Enter a, b, c, d, e, f:"))
discriminant = a * d - b * c
if discriminant == 0:
    print("The equation has no solution.")
    
else:
    x = (e * d - b * f)/discriminant
    y = (a * f - e * c)/discriminant
    print("x is", x, "and y is", y)
    
    