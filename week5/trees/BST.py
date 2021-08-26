#
#   Complete the recursive_count method shown below which will count all the elements in the tree
#
#   Remember what it has to do. The method needs to count the current element as well as all the
# elements of its left subtree and all the elements of its right subtree.
#
#   It can be accomplished in one return statement.
#
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    def count(self, lo, hi):
        # r_count outputs the total number of elements in a tree
        # return self.r_count(self.root)

        # r_rangecount returns numbers of elements between 2 numbers
        return self.r_rangecount(self.root, lo, hi)

    def height(self):
        return self.rheight(self.root)

    def rheight(self, ptr):
        if ptr == None:
            return 0
        else:
            return max(self.rheight(ptr.right) + 1, self.rheight(ptr.left) + 1)
                
    def r_count(self, ptr):
        # r_count outputs the total number of elements in a tree
        if ptr == None:  # Base Case
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)

    def r_rangecount(self, ptr, lo, hi):
        if ptr == None:
            return 0
        if ptr.item >= lo and ptr.item <= hi:
            return 1 + self.r_rangecount(ptr.left, lo, hi) + self.r_rangecount(ptr.right, lo, hi)
        else:
            return self.r_rangecount(ptr.left, lo, hi) + self.r_rangecount(ptr.right, lo, hi)
    
    def total(self):
        return self.r_total(self.root)

    def r_total(self, ptr):
        if ptr == None:
            return 0
        else:
            return ptr.item + self.r_total(ptr.left) + self.r_total(ptr.right)

    def is_present(self, check):
        return self.r_ispresent(self.root, check)

    def r_ispresent(self, ptr, check):
        if ptr == None:
            return False

        elif ptr.item == check:
            return True
        else:
            return self.r_ispresent(ptr.right, check) or self.r_ispresent(ptr.left, check)

        return False

    def count_leaves(self):
        return self.rcount_leaves(self.root)

    def rcount_leaves(self, ptr):
        if ptr == None:
            return 0

        elif (ptr.left == None) and (ptr.right == None):
            return 1

        else:
            return self.rcount_leaves(ptr.right) + self.rcount_leaves(ptr.left)

# def main():
#     # quick test case
#     bst = BST()
#     for ele in [2, 7, 4, 8, 5]:
#         bst.add(ele)
#     print(bst.count_leaves())

# if __name__ == '__main__':
#     main()