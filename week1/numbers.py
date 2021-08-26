#!/usr/bin/env python3

def sum_to_k(lst, k):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] + lst[j] == k:
                print(lst[i], lst[j])
            j = j + 1
        i = i + 1

# def main():
#     lst = [1, 6, 7, 8, 9, 10, 2, 3, 4, 5]
#     k = 13
#     print(sum_to_k(lst, k))

# if __name__ == '__main__':
#     main()
