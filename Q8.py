#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 05:42:50 2022

@author: thakur
"""

a = int(input("Enter first point: "))
b = int(input("Enter Second point: "))
if(a > 0 and b > 0):
	print("Ist Quadrant")
elif(a < 0 and b > 0):
	print("IInd Quadrant")
elif(a < 0 and b < 0):
	print("IIIrd Quadrant")
elif(a > 0 and b < 0):
	print("IVth Quadrant")
else:
	print("Origin")