#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:30:29 2025

@author: mungeunjae
"""

urls = [
        " https://Site.com", 
        "http://site.com ", 
        "site.com", 
        " https://SITE.com"
        ]

a = {u.removeprefix("https://").strip().lower() for u in urls}
print(a)