def matrix_sum():
    with open("matrix.txt") as new:
        num_list = new.read().replace("\n", ",").split(",")
        total = sum(num_list)

def matrix_max():
    pass