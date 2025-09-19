#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:27:35 2025

@author: mungeunjae
"""
#%% my solutiona
nums=[2,7,11,15]
t = 9
#  Problem in naive approach:
#  Uses two nested loops → O(n^2) time.
#  Works for small input but not efficient.
for num in nums:
    need = t - num
    if need in nums:
        a = {num: need}
        print(a)
    else:
        pass

#%% gpt's recommended
# Two-Sum Problem (Efficient O(n) Version)

def two_sum(nums, target):
    """
      Standard algorithm (dictionary lookup):
    - Iterate once over nums.
    - For each num, check if (target - num) already exists in a hash map.
    - If yes → found the pair.
    - Otherwise → store num:index in the map.
    → Time: O(n), Space: O(n).
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

print(two_sum([2,7,11,15], 9))