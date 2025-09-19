#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:22:55 2025

@author: mungeunjae
"""

r_counts = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))
keys = list(r_counts.keys())
third_key = keys[2]
results = []
results.append(keys[0])
results.append(keys[1])

equls = []
for n , v in r_counts.items():
    if r_counts[third_key] == v:
        equls.append(n)
equls.sort()

results += equls

print(results)
