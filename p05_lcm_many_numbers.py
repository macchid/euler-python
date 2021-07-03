import math 

def lcm(numbers):
    assert len(numbers) > 0

    lcm = numbers[0]
    for n in numbers:
        lcm *= n // math.gcd(lcm, n)

    return lcm
    

if __name__ == "__main__":
    print(lcm(range(1, 20)))