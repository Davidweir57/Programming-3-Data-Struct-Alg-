import sys
from LinkedList import LinkedList
from evil_loopy_lists import detect_loop

def make_ll(line):
    items = line.strip().split()

    ll = LinkedList()
    
    for item in items:
        ll.add(item)
        
    return ll
    
def make_long_list():
    lst = [x for x in range(1, 3000, 10)]
    ll = LinkedList()
    for item in lst:
        ll.add(item)
        
    return ll

def add_head_loop(lst):
    # Add a loop to this list. Normally a bad thing ... here it is just to test the student program
    if lst.head != None: # Need at least one item for a loop
        if lst.head.next == None:
            lst.head.next = lst.head
        else:
            ptr = lst.head
            while ptr.next != None:
                ptr = ptr.next
                
            ptr.next = lst.head
        
def main():
    
    lists = []
    for line in sys.stdin:
        # Create two versions of this LinkedList
        no_loop = make_ll(line) # one normal list
        loop = make_ll(line)    # one with a loop
        add_head_loop(loop)     # ... need to add the loop
        
        # Add these two lists
        lists.append(no_loop)
        lists.append(loop)
        
    # Add a couple of long lists to the tests
    ll = make_long_list()
    lists.append(ll)
    
    ll = make_long_list()
    add_head_loop(ll)
    lists.append(ll)
    
    # add an empty list to the mix
    lists.append(LinkedList())

    # Test the students function against all these lists
    for lst in lists:
        print("Loop" if detect_loop(lst) else "Noop", lst)


if __name__ == "__main__":
    main()