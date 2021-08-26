from student import is_maximal

def test(lst):
    bst = BST()

    # Add each element in the lst to the tree
    for n in lst:
        bst.add(n)

    # Print the list and whether or not the resulting tree is maximal
    print("bst.is_maximal(" + str(lst) + ") is " + str(is_maximal(bst)))