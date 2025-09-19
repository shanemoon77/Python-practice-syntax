#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:27:54 2025

@author: mungeunjae
"""

students=[('alice','A'),('bob','B'),('carol','A'),('dave','B')] 
results = {}
a = []
b = []
for (name, grade) in students:
    if grade == 'A':
        a.append(name)
    if grade == 'B':
        b.append(name)

results['A'] = a
results['B'] = b

print(results)