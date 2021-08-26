#!/usr/bin/env python3

# Write a program which reads numbers until a -1 
# is encountered and only print out numbers 
# which have previously occurred in the input. 

def main():

    print("Enter numbers (-1 to end): ", end="") # prompt user to input integers

    nums = int(input()) # read integers from input
    seen, previous = set(), []

    while nums != -1:

        if nums in seen:
            previous.append(nums)
        else:
            seen.add(nums)

        nums = int(input())

    # below is formatting
    for e in previous:
        print(str(e) + " ", end="")
    print()

if __name__ == '__main__':
    main()