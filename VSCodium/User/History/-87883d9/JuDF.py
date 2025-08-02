def add_student(store, name):
    if name in store:
        pass
    else:
        store[name] = 0

def print_student(store, name):
    if name not in store:
        print(f"{name}: no such person in the database")
        return
    if store[name] == 0:
        print(f"{name}:\n no completed courses")


students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")