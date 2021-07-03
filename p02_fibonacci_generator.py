
def fib(limit):
    x, y = 0, 1
    while x < limit:
        yield x
        x, y = y, x + y


if __name__ == "__main__":
   print([x for x in fib(4000000) if x % 2 == 0])
   print(sum(x for x in fib(4000000) if x % 2 == 0))


