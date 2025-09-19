#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:14:55 2025

@author: mungeunjae
"""

squares = [x**2 for x in range(1,21)]

print(squares)  #Using comprehension

results = []
for x in range(1,21):
    square = x**2
    results.append(square)
print(results)  #Using comprehension is more siple.
