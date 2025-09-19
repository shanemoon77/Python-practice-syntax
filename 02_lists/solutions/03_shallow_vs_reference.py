#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:19:00 2025

@author: mungeunjae
"""

a = [[1,2],[3,4]]

c = a.copy()  # Shallow copy: only the outer list is new, inner lists are still shared with the original [:]
a[0] = [99,1]
print(c)
print(a)  # Changing the outer element works fine; since a[0] now points to a new list, a and c no longer share the first inner list

a[0][0] = 11  # Now modifying the first inner list does NOT affect c, because a[0] is a completely new object
print(c)
print(a)

a[1][0] = 99  # But the second inner list is still shared, so both a and c reflect this change
print(a)
print(c)

import copy

d = copy.deepcopy(a)

print(a)
a[0][0] = 99 
print(a)
print(d)  # deepcopy creates a completely independent copy, so d stays unchanged