#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 05:18:09 2018

@author: francisabari
"""
subTotal,gratuityRate = input("Enter the subtotal and gratuity rate: ").split(" ")

subTotal = float(subTotal)

gratuityRate = float(gratuityRate)

gratuity = subTotal * (gratuityRate / 100)

total = subTotal + gratuity

print ("The gratuity is {:0.2f} and the total is {:0.2f}".format(gratuity, total))
