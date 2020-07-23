import sys
import os
from SparseArray import SparseArray


def main():
    if len(sys.argv) == 1:
        print(SparseArray.matching_strings(split(os.environ['STRINGS']), split(os.environ['QUERIES'])))
    elif len(sys.argv) == 2:
        print(SparseArray.matching_strings(split(os.environ['STRINGS']), split(sys.argv[1])))
    elif len(sys.argv) == 3:
        print(SparseArray.matching_strings(split(sys.argv[1]), split(sys.argv[2])))


def split(string):
    return string.split(',')


if __name__ == '__main__':
    main()

