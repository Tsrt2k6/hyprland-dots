def layer_letter(row, centre):
    diff = abs(row - centre)
    return chr(65 + diff)

print(layer_letter(0, 3))