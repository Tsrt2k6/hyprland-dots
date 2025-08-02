def matrix_sum():
    with open("matrix.txt") as new:
        sum = 0
        num_list = new.read().replace("\n", ",").split(",")
        num_list.pop()
        for num in num_list:
            sum += int(num)
    return sum

def matrix_max():
    with open("matrix.txt") as new:
        num_list = new.read().replace("\n", ",").split(",")
        num_list.pop()
        largest = 0
        for num in num_list:
            largest = max(largest, int(num))
    return largest

def row_sums():
    with open("matrix.txt") as file:
        sum_list = []
        for line in file:
            num_list = line.split(",")
            total = 0
            for num in num_list:
                total += int(num)
            sum_list.append(total)
    return sum_list

