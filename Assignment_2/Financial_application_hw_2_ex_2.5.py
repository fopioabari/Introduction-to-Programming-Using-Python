#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:18:09 2018

@author: francisabari
"""

#Home Work_2_Ex_2.5 (Financial application)

#first prompt the user and read subtotal and gratuity rate as strings

subTotal,gratuityRate = input("Enter the subtotal and gratuity rate: ").split(" ")

#Then convert the sub total into float
subTotal = float(subTotal)

#Next convert the gratuity rate into float
gratuityRate = float(gratuityRate)

#compute the gratuity
gratuity = subTotal * (gratuityRate / 100)

#compute the total
total = subTotal + gratuity

#Lastly display the output
print ("The gratuity is {:0.2f} and the total is {:0.2f}".format(gratuity, total))

