#!/usr/bin/env python3

from AVLTree import AVLTree
import sys

# def main():
#     line = sys.stdin.readline()
#     items = line.strip().split()

#     nums = [int(item) for item in items]

#     tree = AVLTree()
#     for num in nums[:-1]:
#         tree.add(num)
#         print(tree.height())

#     print(tree)
#     print(tree.height())

#     for num in nums:
#         if abs(tree.recurse_height(num.left) - tree.recurse_height(num.right)) > 1:
#             return num

# if __name__ == '__main__':
#     main()

#
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
        lst = []
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
        for node in lst:
            if abs(tree.recurse_height(node.left) - tree.recurse_height(node.right)) > 1:
                return node.item
        
    #
    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)
    #
