#! /usr/bin/python3

import random

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

def test_sort():
    tests = [
        [9, 1, 2, 3, 4],
        [54, 26, 93, 17, 77, 31, 44, 55, 20],
        random.sample(range(0, 10000), 20),
    ]

    for index, test in enumerate(tests):
        print(f'Testing {index}: {test}')
        python_sort = sorted(test)
        assert python_sort == bubble_sort(test)

def main():
    test_sort()

if __name__ == '__main__':
    main()
