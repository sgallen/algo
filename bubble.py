#! /usr/bin/python3

from test_sort import test_sort


def bubble_sort(array):
    """Make multiple passes through the array, comparing
    each item to the next and transposing when necessary.
    """
    final_position = len(array) - 1
    print(f'Final position (initial): {final_position}')
    while final_position != 0:
        for index in range(0, final_position):
            if index == final_position: continue
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
        final_position -= 1
        print(f'Final position (while iteration): {final_position}')
        print(array)
    return array

def main():
    test_sort(bubble_sort)

if __name__ == '__main__':
    main()
