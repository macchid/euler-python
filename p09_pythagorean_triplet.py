

limit = 1000


def special_pythagorean():
    for i in range(1, limit - 2):
        for j in range(i + 1, limit -1):
            for k in range(j + 1, limit):
                if i*i + j*j == k*k:
                    if i + j + k == limit:
                        print(i, j, k)
                        return i * j * k



print(special_pythagorean())