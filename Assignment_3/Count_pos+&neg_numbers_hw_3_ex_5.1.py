#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:32:35 2018

@author: francisabari
"""
def main():
    i = int( input ("Enter an interger, the input ends if it is 0: "))
    count_pos = 0
    count_neg = 0
    total = 0
    if (i != 0):
        while (i != 0):
            if (i > 0):
                count_pos += 1
            elif (i < 0):
                count_neg += 1
            total += i
            i = int( input ("Enter an interger, the input ends if it is 0: "))
            count = count_pos + count_neg
            average = total / count

        print ("The number of positives is", count_pos)
        print ("The number of negatives is", count_neg)
        print ("The total is", total)
        print ("The average is", float(average))
    else:
        print ("You didn't enter any number.")

main()
            
            