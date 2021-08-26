#!/usr/bin/env python3

import sys

#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

# Note, these functions are called methods "A method is a function that is stored as a class attribute"
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

    def count(self):
        count = 0
        pointer = self.head

        while pointer != None:
            count = count + 1
            pointer = pointer.next

        return count

    def is_empty(self):
        return self.head == None

    def __str__(self):
        tmp = ""
        ptr = self.head

        while ptr != None:
            tmp += " " + ptr.item
            # tmp = tmp + " " + pointer.item for twirling lists (rotate)
            # tmp = tmp + pointer.item + " " for append 
            ptr = ptr.next

        return tmp

    def contains(self, item):
        pointer = self.head

        while pointer != None:

            if pointer.item == item:
                return True

            pointer = pointer.next

        return False

    def after(self, item):
        pointer = self.head

        while pointer != None:
            if pointer.item == item:
                return pointer.next.item
            pointer = pointer.next

        return None

    def before(self, item):
        pointer = self.head

        if pointer != None:
            while pointer.next != None:
                if pointer.next.item == item:
                    return pointer.item
                pointer = pointer.next
        return None

    def append(self, value):
        newNode = Node(value)

        if self.is_empty():
            self.head = newNode
        else:
            pointer = self.head
            if pointer:
                while pointer.next != None:
                    pointer = pointer.next
                pointer.next = newNode
            else:
                self.head = newNode

    def rotate(self):
        pointer = self.head
        self.append(pointer.item)
        self.remove()