#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:26:38 2025

@author: mungeunjae
"""

chars = ['a', 'b', 'c', 'd']

s = ",".join(chars)
print(s)

a = "Life is too short."

b = a.split()
print(b)

c = a.replace('Life', 'Your leg')
print(c)


class NotInteger(Exception):
    def __str__(self):
        return "There is some noninteger value."

b = "123.2145125.125"
a = b.split('.')
results = []

try:
   for i in a:
       if i.isdigit():
           results.append(int(i))
       else:
           raise NotInteger
       

except NotInteger as e:
    print(e)

else:
    print(results)