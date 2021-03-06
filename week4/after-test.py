import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    tests = [] # list of the results of the tests
    
    ll = LinkedList()

    # Check that it works for an empty list    
    tests.append(ll.after("") == None)  # Each test should be True

    # Check that the item doesn't exist before it is added    
    for item in items:
        tests.append(ll.after(item) == None)
        ll.add(item)
    
    items.reverse()
    for i in range(len(items) - 1):
        # print(ll.after(items[i]), items[i+1])
        tests.append(ll.after(items[i]) == items[i+1])
        
    print("All Good" if all(tests) else str(tests))

if __name__ == "__main__":
    main()