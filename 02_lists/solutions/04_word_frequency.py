#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:21:44 2025

@author: mungeunjae
"""

strings = "Apple banana apple orange, banana kiwi mango apple pear peach."
fruits = strings.split()
lowers = []
for fruit in fruits:
    a = fruit.lower()
    lowers.append(a)

entries = set(lowers)
counts = {}
for entrie in entries:
    if entrie in lowers:
        counts[entrie] = lowers.count(entrie)
    else:
        pass
print(counts)