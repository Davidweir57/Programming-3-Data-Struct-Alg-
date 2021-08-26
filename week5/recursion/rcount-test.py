import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    # call the students function
    print(ll.count())   # Empty list, count should return 0
    
    for item in items:
        ll.add(item)
    
    # call the students function
    print(ll.count())
    
    # check that the first item removed from the list is the same as the last one added
    same = ll.remove() == items.pop()
    
    # call the students function again ... should be one shorter.
    print(ll.count())
    
    while not ll.is_empty() and len(items) > 0:
        same = same and ll.remove() == items.pop()
        
    if not same or not ll.is_empty() or len(items) != 0:
        print("the list has been modified!");

if __name__ == "__main__":
    main()