def matrix_sum():
    with open("matrix.txt") as new:
        sum = 0
        num_list = new.read().replace("\n", ",").split(",")
        print(num_list)
    return sum

def matrix_max():
    pass

matrix_sum()