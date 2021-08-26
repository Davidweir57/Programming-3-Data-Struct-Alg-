import sys
from BST import BST

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST()
    for num in nums:
        tree.add(num)

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()
