#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:41:38 2022

@author: thakur
"""

number = int(input ("Enter the number of which the user wants to print the multiplication table: "))           
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)    