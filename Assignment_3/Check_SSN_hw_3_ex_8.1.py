#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:17:55 2018

@author: francisabari
"""

def main():
    ssn = input("Enter a social security number (ddd-dd-dddd): ").strip()
    if checkSSN(ssn):
        print("Valid SSN")  
    else:
        print("Invalid SSN")
def checkSSN(ssn):
    if(len(ssn))!= 11:
        return False
    for i in range(0,3):
        if not ssn[i].isdigit():
            return False
        for i in range(4,6):
            if not ssn[i].isdigit():
                return False
            for i in range(7,len(ssn)):
                if not ssn[i].isdigit():
                    return False
                if ssn[3]!= '-' or ssn[6]!= '-':
                    return False
            return True
if __name__ == '__main__':
    main()
        