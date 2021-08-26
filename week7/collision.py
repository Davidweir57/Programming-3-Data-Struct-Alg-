#!/usr/bin/env python3

from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)
        col_check = False

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry
            col_check = True

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

        if col_check == False:
            return (index, self.table[index].head.item)
        else:
            return None