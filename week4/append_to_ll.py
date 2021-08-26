import sys
from LinkedList import LinkedList

def main():
    # Read data from input
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    ll.append("o")
    if str(ll) != "o ":
        print("Doesn't work for one element")
    ll = LinkedList()

    for item in items:
        ll.add(item)
        
    print(str(ll))
    ll.append("xxx")
    print(str(ll))

    ll = LinkedList()

    # create the list using append 
    for item in items:
        ll.append(item)
    print(str(ll))
    
if __name__ == "__main__":
    main()