import random


def test_sort(sort_function):
    tests = [
        [9, 1, 2, 3, 4],
        [54, 26, 93, 17, 77, 31, 44, 55, 20],
        random.sample(range(0, 10000), 20),
    ]

    for index, test in enumerate(tests):
        print(f'Testing {index}: {test}')
        python_sort = sorted(test)
        assert python_sort == sort_function(test)
