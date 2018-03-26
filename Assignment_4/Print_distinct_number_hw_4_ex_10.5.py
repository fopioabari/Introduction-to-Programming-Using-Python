#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:07:36 2018

@author: francisabari
"""

def eliminateDuplicates(lst):
    uniqueList = []
    for num in lst:
        if num not in uniqueList:
            uniqueList.append(num)
    return uniqueList
def main():
    values =(input("Enter ten numbers: "))
    lst = (values.split())
    newlst = eliminateDuplicates(lst)
    print("The distinct numbers are: ", end = '')
    for num in newlst:
        print(num, "", end = '')
    print("")
main()
