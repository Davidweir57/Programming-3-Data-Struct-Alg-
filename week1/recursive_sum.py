#!/usr/bin/env python3

def sumto(a, b):
    if a >= b:
        return 0
    else:
        return a + sumto(a + 1, b)
