import json

def print_persons(file_name):
    with open(file_name) as file:
        people = json.load(file)
    for person in people:
        print(f"{person["name"]} {person["age"]} years {person["hobbies"]}")