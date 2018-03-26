#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:45:04 2018

@author: francisabari
"""

def main():
    sin= input("Enter the number:").strip()
    integers= [eval(x) for x in sin.split()]
    
    dictionary = {} 
    
    for number in integers:
        if number in dictionary:
            dictionary[number] +=1
        
    else:
        dictionary[number] = 1
        
        maxOccurence = max(dictionary.values())
        
        pairs = list(dictionary.items())
        
        reverse = [[x, y] for (x, y) in pairs]
        
        print("The numbers with the most occurrence are ",end = "")
        
        for (num, ocurnce) in reverse:
            if ocurnce == maxOccurence:
                print(num,end = " ")
main()
    