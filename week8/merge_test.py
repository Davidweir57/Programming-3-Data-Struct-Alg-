from Queue import Queue
import student

def mergesort(q):
    if len(q) < 2:
        return

    # Split q into two smaller queues
    q1, q2 = student.split(q) # The split function will be supplied by the student
    # Note that the original queue should now be empty

    # recursively sort these smaller queues
    mergesort(q1)
    mergesort(q2)

    # Now, merge these together back into the original q
    student.merge(q1, q2, q)

import random
#
#   Make a queue from a lst
#
def make_q(lst):
    q = Queue()
    for x in lst:
        q.enqueue(x)
    return q

def issorted(q):
    last = q.dequeue()
    while not q.isempty():
        if last > q.first():
            return False # Two elements out of order
        lst = q.dequeue()

    return True # We got here and so all elemets must have been in order.

def main():
    lst = [10 * x for x in range(101)]
    random.shuffle(lst)
    q = make_q(lst)

    mergesort(q) # This uses the student's merge function to sort q

    if issorted(q):
        print("Test passed")
    else:
        print("Your merge function didn't work.")

if __name__ == "__main__":
    main()