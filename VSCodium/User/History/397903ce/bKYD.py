def csv_copy(file_name):
    store = {}
    with open(file_name) as file:
        for line in file:
            line_list = line.split(";")
            if line_list[0] == "id":
                continue
            store[line_list[0]] = line_list[1:]
    return store

def grade_calc(points):
    minimum = [0, 15, 18, 21, 24, 28]
    for i in range(5, -1, -1):
        if points >= minimum[i]:
            return i

def main():
    if True:
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

    print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")

    for id_no, name in student_info.items():
        grades = exercise_data[id_no]
        exam = exam_points[id_no]

        grades = [int(x) for x in grades]
        exec_nbr = sum(grades)
        exec_pts = sum(grades) // 4
        name = [x.strip() for x in name]
        name = " ".join(name)
        exam = [int(x) for x in exam]
        exm_pts = sum(exam)

        tot_pts = exec_pts + exm_pts
        grade = grade_calc(tot_pts)

        print(f"{name:30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")

main()