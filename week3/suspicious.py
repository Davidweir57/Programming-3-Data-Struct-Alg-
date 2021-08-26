#!/usr/bin/env python3

import sys

def main():

    students = {line.strip() for line in open(sys.argv[1], "r")}
    delinqs = {line.strip() for line in open(sys.argv[2], "r")}

    shared = sorted(list(students & delinqs))

    for name in shared:
        print("{}. {}".format((shared.index(name) + 1), name))

if __name__ == '__main__':
    main()
