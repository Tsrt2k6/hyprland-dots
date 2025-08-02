def add_student(store, name):
    if name in store:
        pass
    else:
        store[name] = []

def add_course(store, name, course):
    store[name] = course

def print_student(store, name):
    if name not in store:
        print(f"{name}: no such person in the database")
        return
    if not store[name]:
        print(f"{name}:\n no completed courses")


students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")