import itertools, math, time

def sieve_of_Sundaram(n):
    """The sieve of Sundaram is a simple deterministic algorithm for finding all the prime numbers up to a specified integer."""
    k = (n - 2) // 2
    integers_list = [True] * (k + 1)
    for i in range(1, k + 1):
        j = i
        while i + j + 2 * i * j <= k:
            integers_list[i + j + 2 * i * j] = False
            j += 1
    
    if n > 2:
        primes = [2]

    for i in range(1, k + 1):
        if integers_list[i]:
            primes += [2 * i + 1]

    return primes

def is_prime(n):
    assert n > 0

    if n == 1:
        return False

    if n < 4: 
        return True

    if n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    for d in range(5, int(math.sqrt(n)) + 1, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False

    return True

def prime_candidates(start=1, stop=-1, step=1):
    a = start
    while True:
        if stop > 0 and 6 * a - 1 > stop:
            break

        yield 6 * a - 1

        if stop > 0 and 6 * a + 1 > stop:
            break

        yield 6 * a + 1
        a += step



#print([a for a in itertools.islice(prime_candidates(), 100)])

limit = 2000000
#s = time.time()
#if limit == 1:
#    print(2)
#elif limit == 2:
#    print(3)
#else:
#    print(next(itertools.islice(filter(is_prime, itertools.count(5)), limit-3, None)))

#print(time.time() - s)

#s = time.time()
#if limit == 1:
#    print(2)
#elif limit == 2:
#    print(3)
#else:
#    print(5 + sum(itertools.islice(filter(is_prime, prime_candidates(1, 10)), None, None)))

#print(time.time() - s)

#s = time.time()
#print(sieve_of_Sundaram(10000000)[100000])
#print(time.time() - s)

s = time.time()
print(sum([2,3] + [i for i in itertools.islice(filter(is_prime, prime_candidates(1, limit)), None, None)]))
print(time.time() - s)

