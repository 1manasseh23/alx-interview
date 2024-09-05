#!/usr/bin/python3
# Prime Game solution

def sieve_of_eratosthenes(max_n):
    """Returns a list that tells if numbers are prime up to max_n"""
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return sieve

def count_primes_up_to_n(n, sieve):
    """Counts how many prime numbers exist up to n using a sieve"""
    return sum(sieve[:n + 1])

def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.
    :param x: Number of rounds
    :param nums: List of n values for each round
    :return: Name of the player with the most wins (Maria or Ben)
    """
    if not nums or x < 1:
        return None

    # Find the largest number in nums
    max_n = max(nums)
    
    # Create a sieve of prime numbers up to max_n
    sieve = sieve_of_eratosthenes(max_n)
    
    # Variables to keep track of wins
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Count how many primes are up to n
        primes_count = count_primes_up_to_n(n, sieve)
        
        # Maria wins if the count of primes is odd, Ben wins if even
        if primes_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

