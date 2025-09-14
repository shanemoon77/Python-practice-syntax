#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:31:19 2025

@author: mungeunjae
"""

text = "reach me at aa@bb.cc and admin@mail.com; not_an_email@"
text.find('aa')
a = text[12:20]
text.find('admin')
b = text[25:39]

result = [a, b]
print(result)