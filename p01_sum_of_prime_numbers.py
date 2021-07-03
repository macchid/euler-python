#!/bin/python3

import math
import itertools

def sumMultiplesOf(numbers, n):
    sum = 0
    for r in range(1, len(numbers) + 1):
        for g in itertools.combinations(numbers, r):
            m = math.prod(g)
            limit = (n-1) // m
            sign = int(math.pow(-1, len(g)-1))

            #print(f"{sign}*{m}*{limit}*{1+limit}/2")
            sum += sign * m * (limit)*(1+limit) // 2

    return sum

def sumMultStatic(limit):
    return sum(n for n in range(limit) if n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0)


if __name__ == "__main__":
    print(sumMultiplesOf([3,5,7,11], 100000000))
    print(sumMultStatic(100000000))