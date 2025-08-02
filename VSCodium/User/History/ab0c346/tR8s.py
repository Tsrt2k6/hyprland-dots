def convert(file_name):
    with open(file_name) as file:
        text = file.read()
        recipes = text.split("\n\n")
        copy = []
        for recipe in recipes:
            items = recipe.split("\n")
            ingredients = items[2:]
            print(ingredients)
            items = items[:3]
            items.append(ingredients)
            items[1] = int(items[1])
            copy.append(items)
    print(copy)
    return copy

def search_by_name(file_name, word):
    recipes = convert(file_name)
    names = []
    for recipe in recipes:
        name = recipe[0]
        if word.lower() in name.lower():
            names.append(name)
    return names

def search_by_time(file_name, prep_time):
    recipes = convert(file_name)
    names = []
    for recipe in recipes:
        name = recipe[0]
        time = recipe[1]
        if time <= prep_time:
            names.append(f"{name}, preparation time {time} min")
    return names

def search_by_ingredient(file_name, ingredient):
    recipes = convert(file_name)
    names = []
    for recipe in recipes:
        name = recipe[0]
        time = recipe[1]
        ingredients = recipe[2]
        if ingredient in ingredients:
            names.append(f"{name}, preparation time {time} min")
    return names

found_recipes = search_by_ingredient("recipes1.txt", "eggs")

for recipe in found_recipes:
    print(recipe)