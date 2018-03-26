#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:20:37 2018

@author: francisabari
"""

file_name = input("Enter a file name:")
removed_word = input("Enter the string to be removed:")
lt = []
f= open(file_name,'r')
for line in f.readlines():
   line = line.replace(removed_word,"")
   lt.append(line)
f.close()
f= open(file_name,'w')
for line in lt:
   f.write(line)
f.close()
print("Done")

