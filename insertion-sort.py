#! /usr/bin/python3

from test_sort import test_sort


def insertion_sort(array):
    """Build up sorted sub-array

    Assume 0th element is the seed sub-array that is sorted.
    """
    extent = 0
    final_index = len(array) - 1
    while extent < final_index:
        test_value = array[extent + 1]
        test_index = extent

        while test_index >= 0:
            if test_value >= array[test_index]:
                break
            array[test_index + 1] = array[test_index]
            test_index -= 1
        array[test_index + 1] = test_value

        extent += 1

    return array

def main():
    test_sort(insertion_sort)

if __name__ == '__main__':
    main()
