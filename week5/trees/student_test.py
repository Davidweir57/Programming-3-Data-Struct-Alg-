from BST import BST
from student import make_list

import random

def main():
    random.seed(0)
    
    for length in [1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 50, 100]:
        # Make a random lst
        lst = random.sample(range(length), length)

        # Use the students function to arramge the list
        new_list = make_list(lst) # get the student's lst
        print(new_list)

        # Make sure they have the same elements
        if sorted(lst) != sorted(new_list):
            print("You have somehow changed the elements of the list. You are only supposed to change the order.")
        else:
            # Create a BST
            tree = BST()
            # and add in the elements from the list
            for element in new_list:
                tree.add(element)
            # Show the lst
            print(lst)
            # And some data ... the height, the count and whether or not balanced.
            # print(tree.max_height(), tree.count(), tree.is_balanced())

if __name__ == "__main__":
    main()