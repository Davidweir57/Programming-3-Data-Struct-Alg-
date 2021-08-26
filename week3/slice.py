#!/usr/bin/env python3

def get_sliced_lists(lst):

    final = []
    no_last = lst[:-1]
    no_first_or_last = lst[1:-1]
    reverse = lst[::-1]

    final.append(no_last)
    final.append(no_first_or_last)
    final.append(reverse)
    return final

# def main():
#     # read the list from stdin
#     nums = []
#     num = int(input())
#     while num != -1:
#         nums.append(num)
#         num = int(input())
        
#     # call the student's function with the list of numbers and ...
#     lists = get_sliced_lists(nums)
#     # ... print the result
#     for lst in lists:
#         print(lst)

# if __name__ == "__main__":
#     main()