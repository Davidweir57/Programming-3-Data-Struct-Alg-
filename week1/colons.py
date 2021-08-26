#!/usr/bin/env python3

import sys

s = ":"

for e in sys.argv[1:]:
    s = s + e + ":"

print(s)