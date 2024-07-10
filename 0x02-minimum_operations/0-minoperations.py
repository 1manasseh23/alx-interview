#!/usr/bin/python3
"""Prototype: def minOperations(n)"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n 'H' characters in the file.

    :param n: Number of 'H' characters to achieve
    :return: Fewest number of operations needed
    or 0 if impossible
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
