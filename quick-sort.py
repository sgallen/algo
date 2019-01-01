#! /usr/bin/python3

import random

from test_sort import test_sort


def quick_sort(array):
    if len(array) < 2: return array

    def qs(start, end):
        # base case
        if start >= end: return

        pivot = end

        while pivot > start:
            if array[pivot] < array[pivot - 1]:
                # swap items
                array[pivot], array[pivot - 1] = array[pivot - 1], array[pivot]
                pivot -= 1
            else:
                # move test to start position and bring the start
                # item to the test position i.e. pivot - 1
                array[start], array[pivot - 1] = array[pivot - 1], array[start]
                start += 1

        # pivot now in the correct position, so we recurse
        qs(0, pivot - 1)
        qs(pivot + 1, end)

    qs(0, len(array) - 1)

    return array

def quick_sort2(array):
    if len(array) < 2: return array

    def qs(start, end):
        # Base case
        if start >= end: return
        
        pivot_value = array[random.randint(start, end)]
        left, right = start, end

        while left <= right:
            # Find value greater than pivot
            while array[left] < pivot_value:
                left += 1

            # Find value less than pivot
            while array[right] > pivot_value:
                right -= 1

            # Have our pointers crossed over?
            if left <= right:
                # Swap the found values and move the pointers toward each
                # other to prepare the next round.
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        # Recurse
        qs(start, right)
        qs(left, end)
    
    qs(0, len(array) - 1)
    return array

def quick_sort3(array):
    if len(array) < 2: return array

    def qs(start, end):
        # Base case
        if start >= end: return
        
        pivot_value = array[start]
        pivot = start
        left, right = start + 1, end

        while left <= right:
            # Find value greater than pivot
            while array[left] < pivot_value:
                left += 1
                if left > end: break

            # Find value less than pivot
            while array[right] > pivot_value:
                right -= 1

            # Have our pointers crossed over?
            if left <= right:
                # Swap the found values and move the pointers toward each
                # other to prepare the next round.
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1

        array[pivot], array[right] = array[right], array[pivot]
        pivot = right

        # Recurse
        qs(start, pivot - 1)
        qs(pivot + 1, end)
    
    qs(0, len(array) - 1)
    return array

def main():
    # test_sort(quick_sort)
    test_sort(quick_sort2)
    # test_sort(quick_sort3)

if __name__ == '__main__':
    main()
