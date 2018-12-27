#! /usr/bin/python3

from test_sort import test_sort


def merge_sort(array):
    length = len(array)

    # Base case
    if length <= 1:
        return array

    # Recurse
    mid_point = length//2
    left_array, right_array = array[:mid_point], array[mid_point:]
    left_result = merge_sort(left_array)
    right_result = merge_sort(right_array)

    # Merge left and right result
    merge = []
    left_index = 0
    right_index = 0

    while left_index < len(left_result) and right_index < len(right_result):
        left_item = left_result[left_index]
        right_item = right_result[right_index]
        if left_item <= right_item:
            merge.append(left_item)
            left_index += 1
        else:
            merge.append(right_item)
            right_index += 1

    while left_index < len(left_result):
        left_item = left_result[left_index]
        merge.append(left_item)
        left_index += 1

    while right_index < len(right_result):
        right_item = right_result[right_index]
        merge.append(right_item)
        right_index += 1

    return merge

def main():
    test_sort(merge_sort)

if __name__ == '__main__':
    main()
