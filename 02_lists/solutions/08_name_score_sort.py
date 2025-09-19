#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:25:34 2025

@author: mungeunjae
"""

items = [('alice',91),('bob',83),('bob',95),('carol',100)]
items.sort(key=lambda x:(x[0],-x[1]))
print(items)