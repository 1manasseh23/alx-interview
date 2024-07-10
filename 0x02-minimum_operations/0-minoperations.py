#!/usr/bin/env python3
"""Prototype: def minOperations(n)"""


def minOperations(n):
    """If n is impossible to achieve, return 0"""

    if n <= 1:
        return 0

    # Find the largest power of 2 that is less
    # than or equal to n
    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 *= 2

    # Calculate the remaining operations needed
    remaining = n - power_of_2
    if remaining == 0:
        return power_of_2 // 1
    else:
        return power_of_2 // 1 + minOperations(remaining)
