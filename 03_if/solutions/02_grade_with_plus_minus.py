#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 19:41:04 2025

@author: mungeunjae
"""

def grade_with_plus_minus(score):
    grade = ''
    a = int(str(score)[1])
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    if a >= 7:
        grade += '+'
    elif a >= 5:
        grade += '0'
    else: 
        grade += '-'
    if score == 100:
        grade = 'A+'
    return grade

grade_with_plus_minus(99)