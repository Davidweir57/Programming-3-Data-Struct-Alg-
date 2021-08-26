import sys
from LinkedList import LinkedList

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    # A list to store the results of the tests
    tests = []
    
    ll = LinkedList()

    # Check that it works for an empty list    
    tests.append(ll.before("") == None)  # Each test should be True

    # Check that the item doesn't exist before it is added    
    for item in items:
        tests.append(ll.before(item) == None)
        ll.add(item)
    
    items.reverse()
    for i in range(len(items) - 1):
        # print(ll.before(items[i + 1]), items[i])
        tests.append(ll.before(items[i + 1]) == items[i])
        
    print("All Good" if all(tests) else str(tests))

if __name__ == "__main__":
    main()