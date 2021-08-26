from Stack import Stack
import sys

def reverse_input(stack):

    for line in sys.stdin:
        stack.push(line.strip())

    while stack.is_empty() != True:
        print(stack.pop())

from Stack import Stack
from reverse_input import reverse_input

def main():
    stack = Stack()
    reverse_input(stack)

if __name__ == '__main__':
    main()
