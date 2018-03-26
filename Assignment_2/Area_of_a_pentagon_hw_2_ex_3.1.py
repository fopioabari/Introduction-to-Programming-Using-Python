#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:21:31 2018

@author: francisabari
"""

#Home Work_2_Ex_3.1 (Geometry: area of a pentagon)

#How to calculate area using radius of pentagon 

import math

#first prompt the user for radius of pentagon

radius=eval(input("Enter the length from the center to a vertex:",))

#Then calculate the length of a side of pentagon from above

side = 2 * radius * math.sin(math.pi/5)

#Next, calculate the area of pentagon using side 

area= (3* math.sqrt(3)/2)* side*side

#Lastly print the rounded value of area of pentagon

print("The area of the pentagon is:",format(area,"5.2f"))

