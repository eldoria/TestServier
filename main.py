import sys
from SparseArray import SparseArray

strings = ["ab", "abcd", "bc", "ab"]
queries = ["ab", "bd", "abcd"]


def main():
    if len(sys.argv) == 1:
        print(SparseArray.matching_strings(strings, queries))
    elif len(sys.argv) == 2:
        print(SparseArray.matching_strings(strings, get_args(1)))
    elif len(sys.argv) == 3:
        print(SparseArray.matching_strings(get_args(1), get_args(2)))


def get_args(index):
    return sys.argv[index].split(',')


if __name__ == '__main__':
    main()

