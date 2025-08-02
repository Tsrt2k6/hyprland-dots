def matrix_sum():
    with open("matrix.txt") as new:
        num_list = new.read().replace("\n", ",").split(",")
        total = sum(int(num_list))
    return total

def matrix_max():
    pass

matrix_sum()