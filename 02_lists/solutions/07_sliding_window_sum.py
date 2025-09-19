#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:24:51 2025

@author: mungeunjae
"""

arr = [1,2,3,4,5,6]


windowsums = []
i = 0
k = 2
while i < len(arr) -k:                     
    a = arr[i:i+3]        
    windowsums.append(sum(a))  
    i += 1      
print(windowsums)     