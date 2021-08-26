#!/usr/bin/env python3

def detect_loop(lst):
    pointer = lst.head

    while pointer:
        if pointer.next is None:
            return False
        if pointer.next == lst.head:
            return True
        pointer = pointer.next

    return False