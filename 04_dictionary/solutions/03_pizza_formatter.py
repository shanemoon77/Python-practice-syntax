#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:06:01 2025

@author: mungeunjae
"""

pizza = {
    'crust': 'thin',
    'toppings': ['pepperoni', 'mushrooms', 'extra cheese']
}
  

for k,v in pizza.items():
    strings = ''
    if k == 'crust':
        strings += f"You ordered a {v}-crust pizza with"
    else:
        for i in v[:-1]:
            strings += i + ', '
        strings +='and ' + v[-1]
    print(strings)
    