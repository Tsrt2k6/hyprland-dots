def convert(file_name):
    with open(file_name) as file:
        text = file.read()
        recipes = text.split("\n\n")
        copy = []
        for recipe in recipes:
            items = recipe.split("\n")
            ingredients = items[2:]
            items = items[:3]
            items.append(ingredients)
            copy.append(items)
    return copy

def search_by_name(file_name, word):
    recipes = convert(file_name)
    names = []
    for recipe in recipes:
        name = recipe[0]
        if word.lower() in name.lower():
            names.append(name)
    return names