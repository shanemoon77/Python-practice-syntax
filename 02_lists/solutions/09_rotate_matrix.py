#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:26:24 2025

@author: mungeunjae
"""

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
colum_1 = []
colum_2 = []
colum_3 = []
for row in mat:
    colum_1.append(row[0])
    colum_2.append(row[1])
    colum_3.append(row[2])

mat_clock = [colum_1, colum_2, colum_3]

for i in range(3):
    mat_clock[i].reverse()
print(mat_clock)

# I think using np is more better to treating this (of course). but keep it written this way. casuse it's list practice.
