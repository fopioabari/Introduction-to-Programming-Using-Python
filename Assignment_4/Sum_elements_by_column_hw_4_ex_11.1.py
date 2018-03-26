#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:11:07 2018

@author: francisabari
"""
def sumColumn(arr,columnIndex):
   sm = 0
   for j in range(len(arr)):
       sm = sm+float(arr[j][columnIndex])
   return sm

if __name__=='__main__':
   arr = []
   for i in range(3):
       a = input('Enter a 3 by 4 matrix row for row {0} :'.format(i))
       a = a.split()
       arr.append(a)
   print('Sum of the elements for column {0} is {1}'.format(0,sumColumn(arr,0)))
   print('Sum of the elements for column {0} is {1}'.format(1,sumColumn(arr,1)))
   print('Sum of the elements for column {0} is {1}'.format(2,sumColumn(arr,2)))
   print('Sum of the elements for column {0} is {1}'.format(3,sumColumn(arr,3)))
     
       