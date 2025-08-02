def convert(file_name):
    with open(file_name) as file:
        text = file.read()
        recipies = text.split("\n\n")
        copy = []
        for recipie in recipies:
            items = recipie.split("\n")
            ingredients = items[2:]
            items[2:] = ingredients
            copy.append(items)
    return copy

print(convert("recipes1.txt"))