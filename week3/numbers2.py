#!/usr/bin/env python3

import sys

def get_evenodd_list():

    oddlst, evenlst = [], []

    for n in sys.stdin:
        num = n.strip()

        if num == "-1":
            break
        elif int(num) % 2 != 0:
            oddlst.append(int(num))
        else:
            evenlst.append(int(num))

    return oddlst, evenlst

# def main():
#     # call the get_odd_list function and print the result
#     odds, evens = get_evenodd_list()
#     print(odds)
#     print(evens)

# if __name__ == "__main__":
#     main()
