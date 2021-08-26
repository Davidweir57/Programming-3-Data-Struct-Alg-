#!/usr/bin/env python3

def sum_to_k(lst, k):

    i = 0
    j = len(lst) - 1

    while (i < j) and (i != j):
        add = lst[i] + lst[j]
        if add < k:
            i = i + 1
        elif add > k:
            j = j - 1
        else:
            return True
    return False
