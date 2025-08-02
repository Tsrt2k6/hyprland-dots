def add_student(store, name):
    if name in store:
        pass
    else:
        store[name] = []

def add_course(store, name, course):
    if course[1] == 0:
        return
    courses = store[name]
    for index in range(len(courses)):
        if courses[index][0] == course[0]:
            if courses[index][1] < course[1]:   
                courses[index] = course   
            return      
    courses.append(course)


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
        total_grades += grade
    print(" average grade", total_grades / len(store[name]))


def summary(store):
    print("students", len(store))

    most = 0
    most_name = ""
    for name in store:
        if len(store[name]) > most:
            most = len(store[name])
            most_name = name
    print("most courses completed", most, most_name)

    best = ""
    average = 0
    for name in store:
        total = 0
        for course in store[name]:
            total += course[1]
        if total / len(store[name]) > average:
            average = total / len(store[name])
            best = name

    print("best average grade", average, name)

