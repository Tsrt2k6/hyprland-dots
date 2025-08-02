def layer_letter(row, centre):
    diff = abs(row - centre)
    return chr(65 + diff)

def layers_main():
    layers = int(input())
    centre_index = layers - 1
    for row_no in range(layers * 2 - 1):
        