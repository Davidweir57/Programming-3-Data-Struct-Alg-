#!/usr/bin/env python3

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def rcount(self, ptr):
        if ptr == None:
            return 0
        else:
            return 1 + self.rcount(ptr.next)

    def count(self):
        return self.rcount(self.head)

    def count_even(self):
        return self.even_rcount(self.head)

    def even_rcount(self, ptr):
        if ptr == None:
            return 0
        else:
            if ptr.item % 2 == 0:
                return 1 + self.even_rcount(ptr.next)
            else:
                return self.even_rcount(ptr.next)

    def is_present(self, arg):
        return self.rpresent(self.head, arg)

    def rpresent(self, ptr, arg):
        if ptr != None:
            if ptr.item == arg:
                return True
            return LinkedList.rpresent(self, ptr.next, arg)
        return False

    def largest(self):
        return self.rmax(self.head)

    def rmax(self, ptr):
        if ptr:
            check_next = LinkedList.rmax(self, ptr.next)

            if not ptr.next:
                return ptr.item
            elif ptr.item > check_next:
                return ptr.item
            else:
                return check_next

    def duplicates(self):
        return self.rdup(self.head)

    def rdup(self, ptr):
        if ptr:
            if ptr.next and ptr.item == ptr.next.item:
                return True
            else:
                return self.rdup(ptr.next)
        return False
