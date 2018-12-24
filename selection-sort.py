#! /usr/bin/python3

from test_sort import test_sort


def selection_sort(array):
    """One exchange per pass"""
    final_position = len(array) - 1

    while final_position > 0:
        current_largest = 0

        for index in range(final_position + 1):
            if array[index] > array[current_largest]:
                current_largest = index

        array[current_largest], array[final_position] = array[final_position], array[current_largest]

        final_position -= 1

    return array

def main():
    test_sort(selection_sort)

if __name__ == '__main__':
    main()
