
def prime_factors(n):

    factors = []
    c = 0
    while (n % 2 == 0):
        c += 1
        n >>= 1

    if c > 0:
        factors.append((2, c))

    f = 3
    c = 0
    while (f*f < n):
        while n % f == 0:
            c += 1
            n //= f
        
        if c > 0:
            factors.append((f, c))
        c = 0
        f += 2

    if c > 0:
        factors.append((f, c))

    if n != 1:
        factors.append((n, 1))

    return factors

if __name__ == "__main__":
    print(prime_factors(991199))
    print(prime_factors(990099))
    print(prime_factors(989989))
    print(prime_factors(988889))
    print(prime_factors(987789))
    print(prime_factors(986689))
    print(prime_factors(985589))
    print(prime_factors(984489))
    print(prime_factors(983389))
    print(prime_factors(982289))
    print(prime_factors(981189))
    print(prime_factors(980089))
    print(prime_factors(979979))
    print(prime_factors(978879))
    print(prime_factors(977779))
    print(prime_factors(976679))
    print(prime_factors(975579))
    print(prime_factors(974479))
    print(prime_factors(973379))
    print(prime_factors(972279))
    print(prime_factors(971179))
    print(prime_factors(970079))
