#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:03:18 2025

@author: mungeunjae
"""

scores = {
    'class1': {'kim': 90, 'lee': 80, 'park': 70},
    'class2': {'choi': 88, 'jung': 77, 'yoon': 99},
}

numbers = []
def find_score(x):
    if isinstance(x, int):
        numbers.append(x)
    elif isinstance(x, dict):
        for v in x.values():
            find_score(v)
    elif isinstance(x, list):
        for v in x:
            find_score(v)

find_score(scores)
n = len(numbers)
mean = sum(numbers)/n
print(mean)