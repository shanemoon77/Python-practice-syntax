#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:30:57 2025

@author: mungeunjae
"""

log = "[2025-07-08 15:49:16] INFO: user=kim action=login"

a = log.split(']')
date = a[0].replace('[', '')
b = a[1].split(':')
level = b[0].strip()
message = b[1].strip()

print(date)
print(level)
print(message)