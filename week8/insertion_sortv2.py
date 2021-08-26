def insertion_sort(lst):
    comp, swap = 0, 0
    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        swap = swap + 1
        comp = comp + 1
        while i > 0 and tobeinserted < lst[i-1]:
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
            if i != 0:
                comp = comp + 1
            swap = swap + 1
        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        swap = swap + 1
    return (comp, swap)