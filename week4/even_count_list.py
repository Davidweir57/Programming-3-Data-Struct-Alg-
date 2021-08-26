#!/usr/bin/env python3

def even_count(lst):

    count = 0

    while not lst.is_empty():
        if lst.remove() % 2 == 0:
            count = count + 1
    return count
