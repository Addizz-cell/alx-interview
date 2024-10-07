#!/usr/bin/python3
"""
Prime Game
"""


def prime_numbers(n):
    """
    Return list of prime numbers between 1 and n inclusive.
    
    Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime_numbers = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if filtered[prime]:
            prime_numbers.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return prime_numbers


def is_winner(x, nums):
    """
    Determines winner of Prime Game.
    
    Args:
        x (int): number of rounds of the game
        nums (list of int): upper limit of range for each round
    
    Returns:
        str: Name of the winner (Maria or Ben), or None if there is no winner
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None

    maria = ben = 0
    for i in range(x):
        prime_numbers_list = prime_numbers(nums[i])
        if len(prime_numbers_list) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    
    return None