import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    bool = str(ll.duplicates())[0]
    print(bool, end="")  # Only print the first letter of the result (F for false, T for true)
    for item in items:
        ll.add(item)
        bool = str(ll.duplicates())[0] # Only print the first letter of the result
        print(bool, end="")
        
    print()

if __name__ == "__main__":
    main()