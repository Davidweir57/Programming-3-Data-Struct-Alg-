def partition(lst, lo, hi):
    if len(lst) == 0:
        return 0

    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
    
    print(lst)

    return hi

def main():
    lst = [12, 5, 15, 8, 18, 4]
    # lst = [14, 16, 19, 7, 20, 10]
    print(partition(lst, 0, len(lst) - 1))

if __name__ == "__main__":
    main()