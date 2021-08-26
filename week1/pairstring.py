#!/usr/bin/env python3

import sys

s = sys.argv[1]
char = [c for c in s]

for i in range(0, len(char) - 1, 1):
    print(char[i] + char[i + 1])