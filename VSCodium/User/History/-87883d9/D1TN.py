def add_student(store, name):
    if name in store:
        return False
    store[name] = 0

def print_student(store, name):
    if name not  in store:
        print(f"{name}: no such person in the database")
    

