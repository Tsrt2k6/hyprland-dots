import json

def print_persons(file_name):
    with open(file_name) as file:
        person = json.loads(file)
    return person

print(print_persons("file1.json"))