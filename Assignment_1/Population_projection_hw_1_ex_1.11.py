#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 14:35:31 2018

@author: francisabari
"""
#population project

print("Population projection");
print("Current population: 312032486");
print("One birth every 7 seconds.");
print("One death every 13 seconds.");
print("One new immigrant every 45 seconds.");
print("Yearly Population projection formula: ");
print("Current population + ((births per year)");
print("                   - (deaths per year)");
print("                   + (new immigrants per year))");
print("                   * year.");
print("Year 1 projection: ");
print(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * 1));
print("Year 2 projection: ");
print(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * 2));
print("Year 3 projection: ");
print(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * 3));
print("Year 4 projection: ");
print(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * 4));
print("Year 5 projection: ");
print(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * 5));