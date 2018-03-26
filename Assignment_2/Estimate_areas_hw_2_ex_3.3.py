#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:26:37 2018

@author: francisabari
"""

import math

Atlantax, Atlantay=51.51, -0.16
Orlandox, Orlandoy=28.54, -81.38 
Savannahx, Savannahy=32.08, -81.1
Charlottex, Charlottey=35.23, -80.84 

#distance between Atlanta and Savannah on earth's surface
dAS=6371.01* math.acos(math.sin(math.radians(Atlantax))
    *math.sin(math.radians(Savannahx))
    +math.cos(math.radians(Atlantax))
    *math.cos(math.radians(Savannahx))
    *math.cos(math.radians(Atlantay-Savannahy)));

#distance between Atlanta and Charlotte on earth's surface
dAC=6371.01* math.acos(math.sin(math.radians(Atlantax))
    *math.sin(math.radians(Charlottex))
    +math.cos(math.radians(Atlantax))
    *math.cos(math.radians(Charlottex))
    *math.cos(math.radians(Atlantay-Charlottey)));

#distance between Savannah and Charlotte on earth's surface
dSC=6371.01* math.acos(math.sin(math.radians(Savannahx))
    *math.sin(math.radians(Charlottex))
    +math.cos(math.radians(Savannahx))
    *math.cos(math.radians(Charlottex))
    *math.cos(math.radians(Savannahy-Charlottey)));

#distance between Atlanta and Orlando on earth's surface
dAO=6371.01* math.acos(math.sin(math.radians(Atlantax))
    *math.sin(math.radians(Orlandox))
    +math.cos(math.radians(Atlantax))
    *math.cos(math.radians(Orlandox))
    *math.cos(math.radians(Atlantay-Orlandoy)));

#distance between Savannah and Orlando on earth's surface
dSO=6371.01* math.acos(math.sin(math.radians(Savannahx))
    *math.sin(math.radians(Orlandox))
    +math.cos(math.radians(Savannahx))
    *math.cos(math.radians(Orlandox))
    *math.cos(math.radians(Savannahy-Orlandoy)));

#Area of triangle between Atlanta, Savannah and Charlotte

s= (dAS + dAC + dSC) / 2;
area1= (s * (s-dAS) * (s-dAC) * (s-dSC)) **0.5

#Area of triangle between Atlanta, Savannah and Orlando

s= (dAS + dAO + dSO) / 2;
area2= (s * (s-dAS) * (s-dAO) * (s-dSO)) **0.5
#total area of polygon made by four cities is sum of area
#of two triangles made by the same cities.

area=area1+area2 

print("The estimate area enclosed by 4 cities is " + str(round(area,2)),"sq.km.")

