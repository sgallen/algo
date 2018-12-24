#! /usr/bin/python3

from test_sort import test_sort


def bubble_sort(array):
    """Multiple exchanges per pass """
    final_position = len(array) - 1

    while final_position > 0:
        for index in range(final_position):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]

        final_position -= 1

    return array

def main():
    test_sort(bubble_sort)

if __name__ == '__main__':
    main()
