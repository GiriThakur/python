#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 03:38:01 2022

@author: thakur
"""
X_name, X_age=input("Enter name & Enter Your Age : ").split(" ")
Y_name, Y_age=input("Enter name & Enter Your Age : ").split(" ")


if Y_age < X_age:
    print (f"{Y_name} is Younger than {X_name}") 
else:
    print (f"{X_name} is Youngest than {Y_name}")
       