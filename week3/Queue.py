#
#  Create a queue relying on a Stack. Actually Two Stacks.
#
#  The Stack ADT has three methods:
#     isempty(), push() and pop()
#
from Stack import Stack

class Queue:
    def __init__(self):
        self.enqstack = Stack()
        self.deqstack = Stack()

    def isempty(self):
        return self.enqstack.isempty() and self.deqstack.isempty()

    def enqueue(self, item):
        self.enqstack.push(item)

    def dequeue(self):
        if self.deqstack.isempty() != True:
            return self.deqstack.pop()

        while self.enqstack.isempty() != True:
            self.deqstack.push(self.enqstack.pop())

        return self.deqstack.pop()