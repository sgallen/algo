#! /usr/bin/python3

def fibonacci_rec(position):
    """Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Return: 
        Value in series at position.

    fibonacci(3) => 2
    fibonacci(6) => 8

    Operates in O(a^n), where a is the golden ratio.
    Note: 
        This is highly inefficient because we're recalculating
        previously calculated values.
    """
    if position < 2:
        return position

    return fibonacci_rec(position - 1) + fibonacci_rec(position - 2)
    

def fibonacci_n(position, series=[0, 1]):
    """Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Return: 
        Value in series at position.

    fibonacci(3) => 2
    fibonacci(6) => 8

    Operates in O(n)
    Note:
        This implementation is leveraging the fact that series
        is shared between subsequent calls to the function i.e.
        partial lists are not continuously being calculated.
    """

    # Initialize series
    # Could avoid this by try/excepting IndexError on list lookups.
    while len(series) < position + 1:
        series.append(0)
    
    if position < 2:
        return position
    else:
        primary_trail = position - 1
        secondary_trail = position - 2

        if not series[primary_trail]:
            series[primary_trail] = fibonacci_n(primary_trail)
        if not series[secondary_trail]:
            series[secondary_trail] = fibonacci_n(secondary_trail)

        series[position] = series[primary_trail] + series[secondary_trail]
    return series[position]


def fibonacci_dp(position):
    """Series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Return: 
        Value in series at position.

    fibonacci(3) => 2
    fibonacci(6) => 8

    Operates in O(n)
    Note:
        The upgrade from fibonacci_n is that this implementation
        has O(1) space complexity. Downside is that repeated calls
        to function won't benefit from previous work.

        Additionally, there's no opportunity to blow the call stack
        as we're not leveraging recursion.
    """
    if position < 2:
        return position

    secondary_trail, primary_trail = 0, 1
    for _ in range(position - 1):
        # The lowest value position can be here is 2.
        # In that case we want to iterate once.
        value = secondary_trail + primary_trail
        secondary_trail = primary_trail
        primary_trail = value 
    
    return value
