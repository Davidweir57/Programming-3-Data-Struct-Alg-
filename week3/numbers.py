#!/usr/bin/env python3

import sys

def get_odd_list():

    lst = []

    for n in sys.stdin:
        num = n.strip()

        if num == "-1":
            break
        elif int(num) % 2 != 0:
            lst.append(int(num))

    return lst

# def main():
#     # call the get_odd_list function and print the result
#     odds = get_odd_list()
#     print(odds)

# if __name__ == "__main__":
#     main()