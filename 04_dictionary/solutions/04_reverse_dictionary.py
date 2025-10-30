#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:06:44 2025

@author: mungeunjae
"""

fruit_colors = {
    'apple': 'red',
    'banana': 'yellow',
    'grape': 'purple'
}
reverse_f = {v:k for k, v in fruit_colors.items()}

print(reverse_f)