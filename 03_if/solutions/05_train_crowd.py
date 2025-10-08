#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 07:42:36 2025

@author: mungeunjae
"""

def train_crowd(level, time):
    steps = ['여유', '보통', '혼잡', '매우혼잡']
    i = 0
    
    
    if level >= 8:
        i = 2
    elif level >= 5:
        i = 1
    else:
        i = 0    
    if (time >=7 and time <= 9) or (time >= 18 and time <= 20):
        i += 1
    else:
        pass
    
    return steps[i]

train_crowd(3,2)
train_crowd(8,18)