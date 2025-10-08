#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 15:26:59 2025

@author: mungeunjae
"""
def discount_engine(total, is_member, coupon):
    price = float(total)
    if is_member:
        price = price*0.95
    
    if coupon == '10PCT':
        price = price*0.9
    if total >= 10**4:
        price -= 2000
    
    return price


discount_engine(30000,True,'10PCT')
