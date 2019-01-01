#! /usr/bin/python3

def gcd(a, b):
    if a == b: return a

    dividend, divisor = (a, b) if a > b else (b, a)

    remainder = dividend % divisor
    while remainder > 0:
        dividend = divisor
        divisor = remainder
        remainder = dividend % divisor

    return divisor
