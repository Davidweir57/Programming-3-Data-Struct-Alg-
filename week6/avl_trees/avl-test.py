import sys
from bst2 import BST

def is_avl(bst):
    left = bst.root.left
    right = bst.root.right

    if abs(bst.height(left) - bst.height(right)) > 1:
        return False
    return True

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]

    tree = BST(nums)
    print(tree.height())

    if tree.height() > 3:
        print("error ... your tree is too tall")
    else:
        print(tree.is_avl())

if __name__ == "__main__":
    main()
