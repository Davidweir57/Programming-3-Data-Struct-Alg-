import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(ll.count_even())

if __name__ == "__main__":
    main()