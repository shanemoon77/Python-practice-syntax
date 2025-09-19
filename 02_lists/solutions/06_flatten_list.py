#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:23:46 2025

@author: mungeunjae
"""

grid = [[1,2,3],[4,5],[6]]
a = [grid[i][j] for i in range(3) 
                for j in( range(3) if i == 0 
                else range(2) if i == 1 
                else range(1))]
                
print(a)

def route(i):
    if i == 0:
        return range(3)
    if i == 1:
        return range(2)
    if i == 2:
        return range(1)
    
b = [grid[i][j] for i in range(3)
                for j in route(i)]