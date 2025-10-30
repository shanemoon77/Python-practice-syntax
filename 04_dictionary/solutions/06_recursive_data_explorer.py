#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:08:35 2025

@author: mungeunjae
"""

data = {
    'user': {
        'info': {'name': 'Alice', 'age': 25},
        'hobbies': ['reading', 'gaming']
    },
    'meta': {'active': True, 'score': 98}
}
strings = []

def find_strings(x):
    if isinstance(x, str):
        strings.append(x)
    elif isinstance(x, dict):
        for v in x.values():
            find_strings(v)
    elif isinstance(x, list):
        for v in x:
            find_strings(v)
            
find_strings(data)