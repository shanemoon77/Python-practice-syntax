#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:28:30 2025

@author: mungeunjae
"""
#%% my solutions 
from pathlib import Path

def read_text(path):
    path = Path(path)
    texts = path.read_text() # No encoding specified; may break with non-UTF8 files
    contents = texts.splitlines()
    return contents

def time_line(path):
    contents = read_text(path)
    timelines = []
    for i in range(len(contents)): # Index-based loop; direct iteration is simpler and safer
       a = contents[i].split(']')# Assumes ']' is present; would raise if format is malformed
       b = a[0]
       c = b.split()
       d = c[1]   # Assumes there is at least 2 tokens; fragile parsing
       e = d.split(':')
       hour = e[0]
       timelines.append(hour)
    return timelines

def level(path):
    contents = read_text(path)
    levels = []
    errorlogs = []
    for i in range(len(contents)):
        a = contents[i]
        b = a.split(']')
        c = b[1]    # ⚠️ Assumes ']' exists and right side present
        d = c.split()
        e = d[0]
        levels.append(e)
        
        
        if e == 'ERROR':
            errorlogs.append(contents[i])
        else:
            pass
    print(errorlogs)  #  Prints inside helper; mixes data collection with I/O
    return levels     #  Returns only levels; errorlogs not returned to caller

    
        
def log_renderer(path):
    timelines = time_line(path)
    print("ERROR log lists:\n")
    levels = level(path) # Expects levels only, but error logs were printed earlier (poor cohesion)
    levelcounts = {}
    for l in levels:
        levelcounts[l] = levels.count(l)# O(n^2): repeated .count over the same list
    timelinecounts = {}
    for timeline in timelines:
        timelinecounts[timeline] = timelines.count(timeline)  # O(n^2) again
        
    print(f"\nLevel Count:\n{levelcounts}")
    print(f"\nTime line Count:\n{timelinecounts}")
        
    

path = Path('log.txt')

log_renderer(path)
#%%gpt's recommended

from pathlib import Path
from collections import Counter

def read_text(path):
    """
    Read a text file and return a list of lines.
    Uses UTF-8 by default and ignores undecodable bytes gracefully.
    """
    return Path(path).read_text(encoding="utf-8", errors="replace").splitlines()

def parse_line(line):
    """
    Parse one log line of the form:
      [YYYY-MM-DD HH:MM:SS] LEVEL message...
    Returns (hour, level, line) or None if parsing fails.

    Robustness notes:
    - We split on ']' once to separate timestamp block from the rest.
    - We extract HH from 'YYYY-MM-DD HH:MM:SS'.
    - We take the first token after ']' as LEVEL.
    """
    # Fast sanity check
    if ']' not in line or '[' not in line:
        return None
    left, right = line.split(']', 1)         # left: "[YYYY-MM-DD HH:MM:SS"
    left = left.lstrip('[').strip()          # "YYYY-MM-DD HH:MM:SS"
    parts = left.split()
    if len(parts) < 2:
        return None
    hhmmss = parts[1]                         # "HH:MM:SS"
    hour = hhmmss.split(':')[0]               # "HH"

    tokens = right.strip().split()
    if not tokens:
        return None
    level = tokens[0]                         # "INFO"/"WARN"/"ERROR"/"DEBUG"/...

    return hour, level, line

def time_line(path):
    """
    Return a list of hour strings (e.g., '09', '10', ...) extracted from each log line.
    """
    hours = []
    for line in read_text(path):
        parsed = parse_line(line)
        if parsed is None:
            continue
        hour, _, _ = parsed
        hours.append(hour)
    return hours

def level(path):
    """
    Return (levels, errorlogs):
      - levels: list of LEVEL strings per line
      - errorlogs: list of raw lines where LEVEL == 'ERROR'
    No printing here; this function only collects/returns data.
    """
    levels = []
    errorlogs = []
    for line in read_text(path):
        parsed = parse_line(line)
        if parsed is None:
            continue
        _, lvl, raw = parsed
        levels.append(lvl)
        if lvl == 'ERROR':
            errorlogs.append(raw)
    return levels, errorlogs

def log_renderer(path, recent_error_n=None):
    """
    Print:
      - ERROR logs (optionally limited to the most recent N)
      - Level counts (using Counter)
      - Timeline(hour) counts (using Counter)
    """
    timelines = time_line(path)
    levels, errorlogs = level(path)

    print("ERROR log list:\n")
    # If you want only the last N errors:
    errors_to_show = errorlogs if recent_error_n is None else errorlogs[-recent_error_n:]
    for line in errors_to_show:
        print(line)

    level_counts = Counter(levels)        # O(n) counting
    timeline_counts = Counter(timelines)  # O(n) counting

    print(f"\nLevel Count:\n{dict(level_counts)}")
    print(f"\nTimeline Count:\n{dict(timeline_counts)}")