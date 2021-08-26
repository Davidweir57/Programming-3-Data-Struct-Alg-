from Queue import Queue

def split(q):
    """ A split function which will split a queue into two.
        The function returns a tuple containing the two queues.
    """
    q1, q2 = Queue(), Queue()

    for e in range(len(q) // 2):
        q1.enqueue(q.dequeue())
    
    while not q.isempty():
        q2.enqueue(q.dequeue())
    
    return q1, q2

def merge(q1, q2, q):
    """ this function will merge q1 and q2 into q.
        Assuming that q1 and q2 are sorted, this function will
        return q such that q contains the combined elements of q1 and q2 and
        q will also be sorted.
        
        The function returns nothing. The result will be contained in the queue parameter.
    """
    while not q1.isempty() and not q2.isempty():
        if q1.first() < q2.first():
            q.enqueue(q1.dequeue())
        else:
            q.enqueue(q2.dequeue())
    
    while not q2.isempty():
        q.enqueue(q2.dequeue())

    while not q1.isempty():
        q.enqueue(q1.dequeue())
    
    return q

# def main():
#     l2 = [0, 10, 20, 30, 40,]
#     l1 = [50, 60, 70, 80, 90]
#     q1, q2, q3 = Queue(), Queue(), Queue()

#     for e in l1:
#         q1.enqueue(e)
#     for e in l2:
#         q2.enqueue(e)

#     result = merge(q1, q2, q3)
#     while not result.isempty():
#         print(result.dequeue())

# if __name__ == "__main__":
#     main()