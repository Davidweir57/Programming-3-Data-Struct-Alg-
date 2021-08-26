#!/usr/bin/env python3
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

def is_avl(bst):
    root = bst.root
    bst.root = bst.root.left
    left = bst.height()

    bst.root = root
    bst.root = bst.root.right
    right = bst.height()

    if abs(left - left) > 1:
        return False
    return True

def rotation_type(bst):
    ptr = bst.root
    rtype = ""

    while ptr:
        if ptr.left == None and ptr.right == None:
            return rtype

        if ptr.left == None:
            rtype = rtype + "r"
            ptr = ptr.right
        else:
            rtype = rtype + "l"
            ptr = ptr.left

    return rtype

#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    """ Add this item to its correct position on the tree """
    # This is a non recursive add method. A recursive method would be cleaner.
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        child_tree = tree.root
        lst, lst2 = [], []
        while child_tree != None:
            lst.append(child_tree)
            parent = child_tree
            if item < child_tree.item: # If smaller ... 
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        # Ignore the case where the item is equal.
        lst.reverse()
        for node in lst:
            if abs(tree.recurse_height(node.left) - tree.recurse_height(node.right)) > 1:
                return node.item
        
    #
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #
