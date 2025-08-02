def layer_letter(row, column, centre):
    diff_row = abs(row - centre[0])
    diff_column = abs(column - centre[1])
    diff = max(diff_row, diff_column)
    return chr(65 + diff)

def layers_main():
    layers = int(input())
    centre_index = layers - 1
    for row_no in range(layers * 2 - 1):
        for column_no in range(layers * 2 - 1):
            print(layer_letter(row_no, column_no, centre_index), end="")
        print("")

layers_main()