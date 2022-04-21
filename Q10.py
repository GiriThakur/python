#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 06:27:37 2022

@author: thakur
"""

print("enter three numbers:")
 
a = int(input())
b = int(input())
c = int(input())
 
if a>b and a>c: 
    print(a, " is largest")
elif b>a and b>c: 
    print(b, " is largest")
else: 
    print(c, " is largest")