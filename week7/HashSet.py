#!/usr/bin/env python3

# from LinkedList import LinkedList

# class HashSet:
#     def __init__(self, capacity=10):
#         # Create a list to use as the hash table
#         self.table = [None] * capacity

#     def add(self, item):
        
#         # Find the hash code
#         h = hash(item)
#         index = h % len(self.table)
#         col_check = False

#         # Check is it empty
#         if self.table[index] == None:
#             self.table[index] = LinkedList() # Need a new linked list for this entry
#             col_check = True

#         if item not in self.table[index]:
#             # Only add it if not already there (this is a set)
#             self.table[index].add(item)

#         if col_check == False:
#             return (index, self.table[index].head.item)
#         else:
#             return None

#     def average_bucket_length(self):
#         count, total, index = 0, 0, 0

#         for item in self.table:
#             if self.table[index] != None:
#                 count = count + 1
#                 total = total + len(self.table[index])
#             index = index + 1
#         return total / count

#     def min_max_bucket_length(self):
#         max_, min_, index = 0, 0, 0

#         for item in self.table:

#             if self.table[index] != None:
#                 length = len(self.table[index])

#                 if max_ == 0:
#                     max_ = length

#                 elif max_ < length:
#                     max_ = length

#                 if min_ == 0:
#                     min_ = length

#                 elif min_ > length:
#                     min_ = length
#             index = index + 1
#         return (min_, max_)

#     def __iter__(self):
#         index = 0

#         for item in self.table:
#             if self.table[index] != None:
#                 curr = self.table[index].head
#                 while curr != None:
#                     yield curr.item
#                     curr = curr.next
#             index = index + 1

"""
    This hash table uses a special method to calculate a hash of a string so that the effect of hashing strings may be analysed.
"""
from LinkedList import LinkedList

def str_hash(s):
    """ Return a normal hash, unless it is a string. """
    if not isinstance(s, str):
        return hash(s) # not a string => use the normal hash function
    else:
        # Just use the first character of the string. (Not a good hash!)
        h, i, = 0, 0
        j = len(s) - 1
        while i < len(s):
            h += ord(s[i]) * 31 ** j # Get the ASCII value of the first char of the string as the hash
            j = j - 1
            i = i + 1
        return h

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity
        

    def add(self, item):
        # Find the hash code
        h = str_hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)

    def __str__(self):
        """ Print out the hash table """
        s = ""
        for i in range(len(self.table)):
            s += "table[" + str(i) + "]"
            if self.table[i] != None:
                s += " Head " + str(self.table[i])
            s += "\n"

        return s