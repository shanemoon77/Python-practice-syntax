#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:29:55 2025

@author: mungeunjae
"""

rows = [("name","score"), ("alice", 91), ("bob", 83), ("carol", 100)]

for (name, score) in rows:
    print(f"{name:<12} {score:^12}")
