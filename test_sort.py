import random
import time


def test_sort(sort_function):
    tests = [
        # [9, 1, 2, 3, 4],
        # [26, 54, 93, 17, 77, 31, 44, 55, 20],
        # random.sample(range(0, 100), 20),
        # random.sample(range(0, 10000), 20),
        random.sample(range(0, 10000000), 100000),
    ]

    for index, test in enumerate(tests):
        print('-' * 20)
        print(f'TEST {index}')
        # print(f'input: {test}')
        # Use Python's sorted as comparison.
        python_sort = sorted(test)

        start_time = time.time()
        result = sort_function(test)
        end_time = time.time()
        print(end_time - start_time)

        try:
            assert python_sort == result
        except AssertionError:
            print(f'*** FAIL!: {result}')
            break
        # print(f'result: {result}')
