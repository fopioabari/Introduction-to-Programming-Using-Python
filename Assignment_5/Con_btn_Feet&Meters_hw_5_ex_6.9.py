#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:54:57 2018

@author: francisabari
"""

def footToMeter(foot):
   return foot*0.305

def meterToFoot(meter):
   return meter/0.305
mtr = 20
print ("Feet \t\t Meters \t| \t Meters \t Feet")
for f in range(1,11):
    print("%1.1f \t\t %1.3f  \t| \t %1.1f \t\t %1.3f" % (f,footToMeter(f),mtr,meterToFoot(mtr)))
    if (f % 2 == 0):
       mtr += 4;
    else:
       mtr += 6;
       
       