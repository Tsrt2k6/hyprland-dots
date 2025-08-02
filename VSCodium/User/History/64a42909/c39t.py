def transpose(matrix):
    new = []
    for column in range(len(matrix)):
        for row in range(len(matrix)):
            new.append(matrix[row][column])
    matrix = new