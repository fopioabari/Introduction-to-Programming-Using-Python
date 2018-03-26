#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:21:31 2018

@author: francisabari
"""

import math

radius=eval(input("Enter the length from the center to a vertex:",))

side = 2 * radius * math.sin(math.pi/5)

area= (3* math.sqrt(3)/2)* side*side

print("The area of the pentagon is:",format(area,"5.2f"))
