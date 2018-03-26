#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:42:17 2018

@author: francisabari
"""

class Rectangle:
   def __init__(self,w=1,h=2):
       self.width = w;
       self.height = h;
   def getArea(self):
       return self.width*self.height
   def getPerimeter(self):
       return 2*(self.width+self.height)

w = 4
print ("The width of the rectangle is "+str(w))
h = 40
print ("The width of the rectangle is "+str(h))
r = Rectangle(w,h);
print ("The area of the rectangle is", r.getArea());
print ("The perimeter of the rectangle is",r.getPerimeter());
w = 3.5
print ("The width of the rectangle is "+str(w))
h = 35.7
print ("The width of the rectangle is "+str(h))
r = Rectangle(w,h);
print ("The area of the rectangle is", r.getArea());
print ("The perimeter of the rectangle is",r.getPerimeter());
