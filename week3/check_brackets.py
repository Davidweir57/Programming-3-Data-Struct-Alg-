class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, other):
        self.l.append(other)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def check_brackets(line):

    stack = Stack()

    openbr = ["(", "[", "{"]
    closebr = [")", "]", "}"]

    for char in line:

        if char in openbr:
            stack.push(char)

        elif char in closebr:
            pos = closebr.index(char)
            if stack.is_empty() == True:
                return False
            elif openbr[pos] == stack.pop():
                continue

    return stack.is_empty()

def main():
    print(check_brackets("()"))
    print(check_brackets(")("))
    print(check_brackets("hello(goo(d)bye)"))
    print(check_brackets("hello(goo(d)bye))"))
    print(check_brackets("d(h((e(l))))o)d"))
    print(check_brackets("(d(h((e(l)l))o)d"))

if __name__ == '__main__':
    main()

