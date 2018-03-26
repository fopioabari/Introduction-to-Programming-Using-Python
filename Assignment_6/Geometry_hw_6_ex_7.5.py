#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:48:12 2018

@author: francisabari
"""

import math;

class RegularPolygon:

   def __init__(self, n=3, side=1, x=0, y=0):
       self.__n = n;
       self.__side = side;
       self.__x = x;
       self.__y = y;
   def getN(self):
       return self.__n;
   def getSide(self):
       return self.__side;
   def getX(self):       
       return self.__x;
   def getY(self):
       return self.__y;
   def setN(self, n):
       self.__n = n;
   def setSide(self, side):
       self.__side = side;
   def setX(self, x):
       self.__x = x;
   def setY(self, y):
       self.__y = y;
   def getArea(self):
       return (self.__n * pow(self.__side,2)) / (4 * math.tan(math.pi/self.__n));
   def getPerimeter(self):
       return self.__n * self.__side;

polygon1 = RegularPolygon();      
print("\n Polygon 1: \n Area: " + str(polygon1.getArea()) 
+ " \n Perimeter: " + str(polygon1.getPerimeter()) + " \n");

polygon2 = RegularPolygon(6, 4);      
print("\n Polygon 2: \n Area: " + str(polygon2.getArea()) 
+ " \n Perimeter: " + str(polygon2.getPerimeter()) + " \n");

polygon3 = RegularPolygon(10, 4, 5.6, 7.8);      
print("\n Polygon 3: \n Area: " + str(polygon3.getArea()) 
+ " \n Perimeter: " + str(polygon3.getPerimeter()) + " \n");