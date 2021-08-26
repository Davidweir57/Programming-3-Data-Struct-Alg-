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

    print("Print the elements of the tree in order:")
    tree.in_order()

    print("Print the elements of the tree in pre order:")
    tree.pre_order()

    print("Print the elements of the tree post order:")
    tree.post_order()

if __name__ == "__main__":
    main()