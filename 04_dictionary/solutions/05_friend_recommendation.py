#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 15:07:50 2025

@author: mungeunjae
"""

friends = {
    'alice': {'bob', 'claire', 'dan'},
    'bob': {'alice', 'emily', 'frank'},
    'claire': {'alice', 'george'}
}


def recommend_friends(name,x):
    a = set()
    for k, v in x.items():
        if k == name:
            continue
       
        if name in v:
            a |= v
    a.discard(name)
    a -= x.get(name,set())
    return a

                
                
recommend_friends('alice', friends)       
    