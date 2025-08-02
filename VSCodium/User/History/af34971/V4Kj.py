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
    if False:
        student_info = input("Student information: ")
        exercise_data = input("Exercises completed: ")
        exam_points = input("Exam points: ")
    else:
        student_info = "students1.csv"
        exercise_data = "exercises1.csv"
        exam_points = "exam_points1.csv"

    student_info = csv_copy(student_info)
    exercise_data = csv_copy(exercise_data)
    exam_points = csv_copy(exam_points)

    for id_no, name in student_info.items():
        grades = exercise_data[id_no]
        exam = exam_points[id_no]
        grades = [int(x) for x in grades]
        name = [x.strip() for x in name]
        exam = [int(x) for x in exam]
        total = sum(exam) + sum(grades) // 10
        print(name[0], name[1], total)

main()