#!/usr/bin/env python3

def make_list(lst):

    if lst == []:
        return []

    sort_lst = sorted(lst)
    mid = len(sort_lst) // 2

    return [sort_lst[mid]] + make_list(sort_lst[:mid]) + make_list(sort_lst[mid + 1:])

def is_maximal(bst):
    total_nodes = bst.count()

    count = 1

    height = 0
    while count < total_nodes:
        count = count + 2 ** (height + 1)
        height = height + 1

    if count == total_nodes and height == bst.height() - 1:
        return True

    return False
