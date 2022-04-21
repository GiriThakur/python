#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 04:12:16 2022

@author: thakur
"""

# Python3 program for the above approach

# Function to check if the triangle
# is equilateral or isosceles or scalene
X=int(input())
y=int(input())
z=int(input())
if x == y == z: 
    print("Equilateral Triangle")
    elif x == y or y == z or z == x:
      
         print("Isosceles Triangle") 
         else: 
            print("Scalene Triangle")


