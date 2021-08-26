import sys

def set_intersection(s1, s2):
    return s1.intersection(s2)

# # Function to make a set from a string of tokens
# def make_set(line):
#     line = line.strip()
#     tokens = line.split()
#     return set(tokens)

# def main():
#     # Read each set
#     line1 = sys.stdin.readline()
#     set1 = make_set(line1)
    
#     line2 = sys.stdin.readline()
#     set2 = make_set(line2)

#     # call the student's function ...
#     intersection = set_intersection(set1, set2)
    
#     # ... and print the result
#     # First convert to a list and sort to be sure that the order will always be the same
#     list_intersection = list(intersection)
#     list_intersection.sort()
#     print(list_intersection);

# if __name__ == "__main__":
#     main()