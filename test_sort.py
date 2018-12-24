import random


def test_sort(sort_function):
    tests = [
        [9, 1, 2, 3, 4],
        [26, 54, 93, 17, 77, 31, 44, 55, 20],
        random.sample(range(0, 100), 20),
        random.sample(range(0, 10000), 20),
        random.sample(range(0, 10000), 30),
    ]

    for index, test in enumerate(tests):
        print('-' * 20)
        print(f'TEST {index}')
        print(f'input: {test}')
        python_sort = sorted(test)
        result = sort_function(test)
        try:
            assert python_sort == result
        except AssertionError:
            print(f'*** FAIL!: {result}')
            break
        print(f'result: {result}')
