#  Copyright (c) 2020, Egor N. Kostyuk, All rights reserved.

def primes():
    number = 1
    while True:
        number += 1
        _, *divisors, self_divisor = [d for d in range(1, number + 1)]
        if not any([number % d == 0 for d in divisors]):
            yield number


def primes2():
    number = 1
    while True:
        number += 1
        is_divisible_by = [number % d == 0 for d in range(2, number)]
        if not any(is_divisible_by) or not is_divisible_by:
            yield number
