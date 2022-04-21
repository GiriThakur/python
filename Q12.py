#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 06:35:03 2022

@author: thakur
"""

num = int(input("Enter the number: "))
f = 1
for i in range (1, num+1):
    f = f*i

#printing the output
print ("Factorial of the number %d is %d" %(num, f))