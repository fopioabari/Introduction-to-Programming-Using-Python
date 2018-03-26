#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:31:58 2018

@author: francisabari
"""

import math

number = eval(input("Enter the number of sides:"))
side = eval(input("Enter the side:"))
area = number *side *side/ math.tan(math.pi /number) /4
print("The area of the polygon is " + format(area, "<10.2f"))
