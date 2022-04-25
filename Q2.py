#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:08:27 2022

@author: thakur
"""

mark=int(input("Enter  Numeric grade :"))
if (mark<70):
    print('F') 
elif (mark >69) and  (mark<80):
        print('C') 
elif (mark >79) and (mark<90):
        print('B')
elif (mark>89):
        print('A')
else:
        print("Enter Valid grade")