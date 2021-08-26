#!/usr/bin/env python3

def above_average(lst):
    avg = sum(list) / len(lst)
    return [e for e in lst if e > avg]