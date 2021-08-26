import sys
from LinkedList import LinkedList

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()

    # Create the linked list
    ll = LinkedList()

    # add the items to the linked list
    for item in items:
        ll.add(item)

    # print the linked list
    print(str(ll))
    ll.rotate() # rotate it
    print(str(ll)) # print it again

    # create the list using append 
    for i in range(len(items)-1):
        ll.rotate() # Rotate enough times should get back to the original
    print(str(ll))

if __name__ == "__main__":
    main()