#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:07:10 2018

@author: francisabari
"""

def getPentagonalNumber(n):
   return n*(3*n-1)/2;
for x in range(1,101):
    if (x)%10==0:
        print('%6d' % (getPentagonalNumber(x)))
    else:
        print('%6d' % (getPentagonalNumber(x)),end=' ')
        