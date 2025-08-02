def convert(file_name):
    with open(file_name) as file:
        text = file.read()
        recipes = text.split("\n\n")
        copy = []
        for recipe in recipes:
            items = recipe.split("\n")
            ingredients = items[2:]
            print(ingredients)
            items[2:] = ingredients
            copy.append(items)
    return copy

(convert("recipes1.txt"))