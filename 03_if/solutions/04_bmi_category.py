#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 07:41:41 2025

@author: mungeunjae
"""

def bmi_category(weight, height):
    bmi = weight/height**2
    if bmi >= 25:
        return 'obesity'
    elif bmi < 18.5:
        return 'underweight'
    else:
        return 'normal'

bmi_category(64,1.77)