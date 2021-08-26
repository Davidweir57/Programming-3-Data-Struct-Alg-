#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#
def partition(lst, lo, hi):

    global comp, move

    median = ((hi + lo) // 2)

    lst[lo], lst[median] = lst[median], lst[lo]
    move += 3
    part = lo
    while lo < hi:
        comp += 1
        while lst[lo] <= lst[part] and lo < hi:
            comp += 1
            lo += 1
        
        comp += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            comp += 1
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            move += 3

    # Swap part into position
    comp += 1
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        move += 3
    
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    global comp, move
    comp, move = 0, 0
    rec_qsort(lst, 0, len(lst) - 1)
    return (comp, move)

