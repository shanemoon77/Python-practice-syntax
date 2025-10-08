#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 19:41:43 2025

@author: mungeunjae
"""

def validate_date_simple(date_str):
    years = date_str[:4]
    months = date_str[5:7]
    days = date_str[-2:]
    leap_year = False
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        return False
    if not (years.isdigit() and months.isdigit() and days.isdigit()):
        return False
    y, m, d = int(years), int(months), int(days)
   
    if is_leap_year(y) == '윤년':
        leap_year = True
    else:
        pass
    
    if leap_year:
        if m == 2:
            if d in range(1,30):
                return True
            else:
                return False
        elif m in [4, 6, 9, 11]:
            if d in range(1,31):
                return True
            else:
                return False
        else:
            if d in range(1,32):
                return True
            else:
                return False
    else:
        if m == 2:
            if d in range(1,29):
                return True
            else:
                return False
        elif m in [4, 6, 9, 11]:
            if d in range(1,31):
                return True
            else:
                return False
        else:
            if d in range(1,32):
                return True
            else:
                return False
            
    
validate_date_simple('2002-02-27')