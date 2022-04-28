#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:45:05 2022

@author: thakur
"""

n =int(input("Enter the range of numbers :"))

for i in range(1, n+1):
    for k in range(1, i+1):
        print("*", end="")
    print()
    
for i in range(n):
    for j in range(n - i):
        print('*', end='')
    print()