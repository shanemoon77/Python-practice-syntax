#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:32:16 2025

@author: mungeunjae
"""

def render_report(title, items):
    print(f"{title:=^40}")
    results = []
    for (name, score) in items:
        print(f"{name:<20} {score:>10}")
        results.append(score)
    total_score = sum(results)
    n = len(items)
    print(f"\ntotal score: 100")
    mean = total_score/n
    print(f"mean: {mean}")
        
    
        
items= [
    ("Alice", 87),
    ("Bob", 92),
    ("Charlie", 76),
    ("Diana", 98),
    ("Evan", 65),
    ("Fiona", 88),
]   
render_report('Mid-exiam', items)
