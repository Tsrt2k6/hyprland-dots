def add_student(store, name):
    if name in store:
        pass
    else:
        store[name] = []

def add_course(store, name, course):
    store[name].append(course)


def print_student(store, name):
    if name not in store:
        print(f"{name}: no such person in the database")
        return

    if not store[name]:
        print(f"{name}:\n no completed courses")
        return

    print(f"{name}:")
    print(f" {len(store[name])} completed courses:")
    for course, grade in store[name]:
        print(" ", course, grade)
    
    
students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
print_student(students, "Peter")