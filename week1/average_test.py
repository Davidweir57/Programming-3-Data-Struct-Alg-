import sys
from average import calc_average # student's function

#
#   Read a list from stdin
#
line = sys.stdin.readline()

tokens = line.split()

list = []

for token in tokens:
    list.append(int(token))

#
#   Call the function + print result
#
print(calc_average(list))
print(above_average(list))