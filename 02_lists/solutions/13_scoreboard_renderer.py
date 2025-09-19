#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 18:28:19 2025

@author: mungeunjae
"""
#%% my solution
samples = [('alice',91),('bob',83),('carol',100)]

    
def title_printer():
    title = input("Enter the titile: ")  #Problem: interactive input makes it harder to test/automate
    print(f"{title.upper():=^40}")
    a = 'name'
    b = 'score'
    print(f"{a:<30} {b:>10}")
    print('-'*40)
    
def data_printer(datas):
    r_datas = sorted(datas, key=lambda x:-x[1])
    for (name, score) in r_datas:
        print(f"{name:<30} {score:>10}")
        
def mean_printer(datas):
    # Inefficient: builds a separate list of scores just to sum
    scores = []
    for (name, score) in datas:
        scores.append(score)
    total = sum(scores)
    mean = total/len(scores)
    print('-'*40)
    print(f"Total: {total}")
    print(f"Mean: {mean}") #Mean not rounded/pretty-printed
    


def score_renderer(datas):
    #  Problem: tightly coupled — calls all subfunctions with fixed order
    # - Hard to reuse header/body/footer separately
    # - No return values → only prints
    title_printer()
    data_printer(datas)
    mean_printer(datas)

score_renderer(samples)

#%% gpt's recommended

def header(title, width=40):
    """Return a formatted header string (no input prompt)."""
    return f"{title.upper():=^{width}}\n{'Name':<30}{'Score':>10}\n{'-'*width}"

def body(datas, width=40):
    """Return formatted body sorted by score (descending)."""
    r_datas = sorted(datas, key=lambda x: -x[1])
    return "\n".join(f"{name:<30}{score:>10}" for name, score in r_datas)

def footer(datas, width=40):
    """Return formatted totals and averages."""
    total = sum(score for _, score in datas)
    mean = total / len(datas)
    return f"{'-'*width}\n{'Total':<30}{total:>10}\n{'Mean':<30}{mean:>10.2f}"

def score_renderer(datas, title="Scores"):
    """Combine header, body, footer into one string."""
    return "\n".join([header(title), body(datas), footer(datas)])

print(score_renderer(samples))
