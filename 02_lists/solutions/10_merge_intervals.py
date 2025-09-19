#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:27:24 2025

@author: mungeunjae
"""
#%% my solution.
intervals = [[1,3],[2,6],[8,10],[15,18]]



def there_is_overlap(a, b):
    # ❌ Problem in current approach:
    # - Expands both intervals into range() and only checks if "numbers overlap".
    # - In practice, a simple mathematical condition is faster and clearer.
    for i in a:
        if i in b:       
            return True
        else:
            pass
        


i = 0
while i < len(intervals) - 1:
    first = intervals[i]
    second = intervals[i+1]
    a = range(first[0], first[-1] + 1)
    b = range(second[0], second[-1] + 1)
    
    if there_is_overlap(a,b):
        # - Only compares i and i+1 (adjacent intervals).
        # - Longer chains of overlaps may be missed in certain inputs.
        # - Also uses second[-1] blindly as the new endpoint, which can shrink the interval.
        new = [first[0], second[-1]]
        del intervals[i+1]
        del intervals[i]
        intervals.insert(0,new)
        
        i = 0
        continue 
    else:
        i +=1
    

    
print(intervals)

#%% gpt's recommened
def merge_intervals(intervals):
    """
     Standard algorithm explanation:
    1. Sort intervals by start point.
    2. Compare current interval (s, e) with the next interval (ns, ne):
       - If ns <= e: the intervals overlap → update e = max(e, ne).
       - Otherwise: no overlap → add current interval to result and move on.
    3. Add the last interval to the result.
    → Time complexity: O(n log n) due to sorting, merge loop itself is O(n).
    → Advantage: Handles all cases robustly, works on arbitrary inputs.
    """
    if not intervals: return []
    intervals = sorted(intervals, key=lambda x: x[0])# Sort by start
    merged = []
    s, e = intervals[0]
    for ns, ne in intervals[1:]:
        if ns <= e:# Overlap
            e = max(e, ne) # ✅ Always take the maximum end point
        else: # ✅ Always take the maximum end point
            merged.append([s, e])
            s, e = ns, ne
    merged.append([s, e])
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
merge_intervals(intervals)