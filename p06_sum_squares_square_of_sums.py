
def sum_of_squares(limit):
    return (2 * limit + 1)*(limit + 1)*limit // 6

def square_of_sum(limit):
    return (limit * (limit + 1) // 2) ** 2


limit = 100
print(f"{square_of_sum(limit)} - {sum_of_squares(limit)} = {square_of_sum(limit) - sum_of_squares(limit)}")

