#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 07:45:06 2025

@author: mungeunjae
"""

def traffic_light(color, is_emergency):
    if is_emergency == True:
        return 'Go'
    else: 
        pass
    if color.lower() == 'red':
        return 'Stop'
    elif color.lower() == 'yellow':
        return 'Wait'
    else:
        return 'Go'
    
traffic_light('red', True)