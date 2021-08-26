#!/usr/bin/env python3

def maximum(l):

    if len(l) == 1:
        return l[0]
    elif l[0] < l[1]:
        l.pop(0)
    else:
        l.pop(1)

    return maximum(l)
