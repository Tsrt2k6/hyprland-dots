import json

def print_persons(file_name):
    with open(file_name) as file:
        person = json.load(file)
    