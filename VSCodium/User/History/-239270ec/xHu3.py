def csv_copy(file_name):
    store = {}
    with open(file_name) as file:
        for line in file:
            line_list = line.split(";")
            if line_list[0] == "id":
                continue
            store[line_list[0]] = line_list[1:]
    return store

def main():
    if True:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
    student_info = csv_copy(student_info)
    exercise_data = csv_copy(exercise_data)
    for id_no, name in student_info:
        grades = exercise_data[id_no]
        grades = [int(x) for x in grades]
        total = sum(grades)
        print