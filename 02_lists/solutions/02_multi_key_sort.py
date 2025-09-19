#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:16:37 2025

@author: mungeunjae
"""

words = ['banana','fig','apple','cherry']
orders = []
for word in words:
    a = len(word)
    orders.append(a)

b =list(zip(words, orders))

b.sort(key=lambda x:(x[1], x[0]) ) 

c = [x for (x,y)in b]
print(c)