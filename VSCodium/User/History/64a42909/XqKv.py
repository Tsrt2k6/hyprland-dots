def transpose(matrix):
    new = []
    for column in range(len(matrix)):
        for row in range(len(matrix)):
            new.append(matrix[row][column])
    matrix = new

store = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]