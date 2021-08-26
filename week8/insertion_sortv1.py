def insertion_sort(lst):
    comp, swap = 0, 0
    # At each pass ensure that that section is sorted.
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        comp = comp + 1
        while i > 0 and lst[i] < lst[i-1]:
            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
            swap = swap + 1
            if i != 0:
                comp = comp + 1
    return (comp, swap)

