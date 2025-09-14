#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:31:51 2025

@author: mungeunjae
"""

doc = """
   apple

   banana
 cherry   
"""

fruits = doc.split()

for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")