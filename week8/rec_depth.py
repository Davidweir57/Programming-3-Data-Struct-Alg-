import sys
from qsort_RecDepth import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
    
    orig = list(items)

    result = qsort(items)
    if items != sorted(ori:
        print("The list isg) not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()