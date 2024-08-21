#!/usr/bin/python3
"""
Module for calculating the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a
    given amount total.

    Args:
        coins (list): A list of integers representing the values of
        the coins in your possession. total (int): The total
        amount of money you want to make.

    Returns:
        int: The fewest number of coins needed to meet the total,
        or -1 if it cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize a list for storing the minimum coins needed
    # for each value up to the total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    """
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
    """
    coins.sort(reverse=True)

    for coin in coins:
        for i in range(coin, total + 1):
            # Only update dp[i] if we can make a smaller number
            # of coins using the current coin
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    # If dp[total] is still infinity, it means the total cannot
    # be met by any combination of coins
    return dp[total] if dp[total] != float('inf') else -1
