
def biggest_palindromic_of(digits):
    start = 10 ** digits - 1
    stop = 10 ** (digits - 1)
    step = -1

    val = max(x * y 
        for x in range(start, stop, step) 
        for y in range(start, stop, step) 
        if str(x*y) == str(x*y)[ : : -1])

    return str(val)

if __name__ == "__main__":
    print(biggest_palindromic_of(3))
        