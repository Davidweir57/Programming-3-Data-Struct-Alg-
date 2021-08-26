#!/usr/bin/env python3

class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)

    def r_count(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.r_count(ptr.left) + self.r_count(ptr.right)
            
    def count(self): return self.r_count(self.root)

    def r_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + max(self.r_height(ptr.left), self.r_height(ptr.right))

    def height(self): return self.r_height(self.root)

    def in_order(self):
        self.r_inorder(self.root)
        print()

    def r_inorder(self, ptr):
        if ptr:
            self.r_inorder(ptr.left)
            print(str(ptr.item) + " ", end="")
            self.r_inorder(ptr.right)

    def pre_order(self):
        self.r_preorder(self.root)
        print()

    def r_preorder(self, ptr):
        if ptr:
            print(ptr.item, end=" ")
            self.r_preorder(ptr.left)
            self.r_preorder(ptr.right)

    def post_order(self):
        self.r_postorder(self.root)
        print()

    def r_postorder(self, ptr):
        if ptr:
            self.r_postorder(ptr.left)
            self.r_postorder(ptr.right)
            print(ptr.item, end=" ")

    def __iter__(self):
        self.lst = []
        self.r_iter(self.root)
        yield " ".join(self.lst)

    def r_iter(self, ptr):
        if ptr:
            if ptr.left:
                self.r_iter(ptr.left)

            if ptr.right:
                self.r_iter(ptr.right)

        self.lst.append(str(ptr.item))