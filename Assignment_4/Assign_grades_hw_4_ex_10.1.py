#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:56:59 2018

@author: francisabari
"""

def findGrades(lst):  
    best = int(max(lst))
    i = 0
    while i < len(lst):
        scr = int(lst[i])
        if scr >= best - 10:
            print("Student ", i , " score is ", scr, " and grade is A")
        elif scr >= best - 20:
            print("Student ", i , " score is ", scr, " and grade is B")
        elif scr >= best - 30:
            print("Student ", i , " score is ", scr, " and grade is C")
        elif scr >= best - 40:
            print("Student ", i , " score is ", scr, " and grade is D")
        else:
            print("Student ", i , " score is ", scr, " and grade is F")
        i += 1
def main():
    scores =(input("Enter scores: "))
    lst = (scores.split())
    findGrades(lst)
main()

