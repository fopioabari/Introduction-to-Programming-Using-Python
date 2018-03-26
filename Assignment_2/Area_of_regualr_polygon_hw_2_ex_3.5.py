#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:31:58 2018

@author: francisabari
"""
#Home Work_2_Ex_3.5 (Geometry:area of a regular polygon)

#How to calculate the area of pentagon using side

import math

#Get number of sides and length of side from user

number = eval(input("Enter the number of sides:"))
side = eval(input("Enter the side:"))

#Compute the area using length of side

area = number *side *side/ math.tan(math.pi /number) /4

#Display the area of polygon 

print("The area of the polygon is " + format(area, "<10.2f"))