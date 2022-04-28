#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:51:58 2022

@author: thakur
"""

num = int(input("Enter a number:\t"))
a = list(map(int,str(num)))
b = list(map(lambda x : x ** 3, a))

if sum(b) == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an arsmtrong number")