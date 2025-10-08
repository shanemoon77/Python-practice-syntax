#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 07:43:42 2025

@author: mungeunjae
"""

import string

def invastigators(pw):
    a =  len(pw) >= 8
    uppers = any(ch.isupper() for ch in pw)
    lowers = any(ch.islower() for ch in pw)
    specials = any(ch in string.punctuation for ch in pw)
    nums = any(ch.isdigit() for ch in pw)
    bulian_lists = [a, uppers, lowers, specials, nums]
    
    return bulian_lists
    
def validate_password(pw):
    bulian_lists = invastigators(pw)
    a = sum(bulian_lists)
    weak_patterns = ['password', '123456', '123456789', 
                     'guest', 'qwerty', '12345678', 
                     '111111', '12345',  
                     '123123', '1234567', '1234', 
                     '1234567890', '000000', '555555' , 
                     '666666' , '123321' , '654321', 
                     '7777777', '123' ]
    
    
    for x in weak_patterns:
        b = pw.find(x)
        if b == -1:
            pass
        else:
            return 'Weak'
    if a == 5:
        return'Strong'
    elif a >= 3: 
        return 'Moderate'
    else:
        return 'Weak'
print(validate_password('Ez!Isss5'))   