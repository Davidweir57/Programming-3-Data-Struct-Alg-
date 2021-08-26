import sys
from BST import BST

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums[:-1])

    lst = tree.add(nums[-1])
    print(lst)

if __name__ == "__main__":
    main()