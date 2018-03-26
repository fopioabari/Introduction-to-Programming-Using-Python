#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:16:33 2018

@author: francisabari
"""

import math

class GeometricObject :
   def __init__(self):
       self.color= input("Enter color:")
       self.filled = 0 
  
   def getColor(self):
       return self.color
  
   def getFilled(self):
       return self.filled
  
   def setColor(self,color):
       self.color = color
      
   def setFilled(self, filled):
       self.filled = filled
      
class Triangle(GeometricObject):
    
   def __init__(self):
       super().__init__()
       self.side1 = 1.0
       self.side2 = 1.0
       self.side3 = 1.0
   
   def setSides(self,side1,side2,side3):
       self.side1 = float(input("Enter side1:"))
       self.side2 = float(input("Enter side2:"))
       self.side3 = float(input("Enter side3:"))    
   
   def getArea(self):
       s = (self.side1+self.side2+self.side3)/2
       area = math.sqrt( s* (s-self.side1) * (s-self.side2) * (s-self.side3))
       return area

   def getPerimeter(self):
       return (self.side1+self.side2+self.side3)
  
   def __str__(self):
       output = (" Triangle: side1 = " + str(self.side1) \
                 + " side2 = " + str(self.side2) \
                 + " side3 = " + str(self.side3) \
                 +"\n color = "+self.color) 
       output = output+" \n Filled: "
       if(self.filled == 0):
           output = output+ "False"
       else:
           output = output+"True"
       return output
   
Tria1 = Triangle()
print(Tria1, " \n Area: ",Tria1.getArea(), "   \n Perimeter: ",Tria1.getPerimeter())

Tria2 = Triangle()
Tria2.setSides(3,4,5)
print(Tria2, " \n Area: ",Tria2.getArea(), "   \n Perimeter: ",Tria2.getPerimeter())



