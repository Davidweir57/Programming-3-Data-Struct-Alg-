#!/usr/bin/env python3

import sys

s = sys.argv[1]

if len(s) % 2 != 0:
    print(s[0] + s[len(s) - 1])
else:
    print(s[int(len(s) / 2):])