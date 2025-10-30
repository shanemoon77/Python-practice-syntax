#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:36:35 2025

@author: mungeunjae
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
python_users = []
for k, v in favorite_languages.items():
    if v == 'python':
        python_users.append(k.title())
    else:
        pass
    
print(python_users)