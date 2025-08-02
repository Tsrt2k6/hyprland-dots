def matrix_sum():
    with open("matrix.txt") as new:
        sum = 0
        num_list = new.read().replace("\n", ",").split(",")
        num_list.pop()
        for num in num_list:
            sum += int(num)
    return sum

def matrix_max():
    pass

matrix_sum()
print(matrix_sum())