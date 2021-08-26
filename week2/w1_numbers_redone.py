#!/usr/bin/env python3

def sum_to_k(lst, k):

    i = 0
    try:
        while lst[i] + lst[i + 1] != k:
            i = i + 1
        return True
    except:
        return False


def main():
    lst = sorted([2, 4, 6, 8, 10, 12])
    k = 16
    print(sum_to_k(lst, k))

if __name__ == '__main__':
    main()
