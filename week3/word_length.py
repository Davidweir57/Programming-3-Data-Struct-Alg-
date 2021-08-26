import sys

def get_counts_dict(lst):

    d = {}

    for word in lst:
        if len(word) in d:
            d[len(word)] = d[len(word)] + 1
        else:
            d[len(word)] = 1

    return d

# def main():
#     # read the list of words from stdin
#     line = sys.stdin.readline()
#     line = line.strip()
#     words = line.split()

#     # call the student's function
#     counts = get_counts_dict(words)
#     print(type(counts))

#     lengths = counts.keys()
#     for length in sorted(lengths):
#         print(str(length) + ": " + str(counts[length]))

# if __name__ == "__main__":
#     main()
