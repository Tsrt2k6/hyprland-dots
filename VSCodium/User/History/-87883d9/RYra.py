def add_student(store, name):
    if name in store:
        pass
    else:
        store[name] = []

def add_course(store, name, course):
    if course[1] == 0:
        return
    for courses in store[name]:
        if course[0] == courses[0] and course[1] > courses[1]:
            

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
    total_grades = 0
    for course, grade in store[name]:
        print(" ", course, grade)
        total_grades += int(grade)
    print(" average grade", total_grades / len(store[name]))
    
