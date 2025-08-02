def main():
    score_list = user_input()
    total_list, total = score_calc(score_list)
    statistics(total_list, total)

def user_input():
    score_list = []
    while True:
        scores = input()
        if scores == "":
            break
        score_list.append(scores)
    return score_list

def score_calc(score_list):
    total_list = []
    total = 0
    for score in score_list:
        exam, exercise = score.split()
        sum = int(exam) + int(exercise) // 10
        total += sum
        if int(exam) < 10:   # Exception cutoff point, results in insta fail lol
            total_list.append(0)
        else:
            total_list.append(sum)
    return total_list, total

def statistics(score_list, total):
    grade = []
    for score in score_list:
        if score < 15:
            grade.append(0)
        elif 15 <= score <= 17:
            grade.append(1)
        elif 18 <= score <= 20:
            grade.append(2)
        elif 21 <= score <= 23:
            grade.append(3)     
        elif 24 <= score <= 27:
            grade.append(4) 
        elif 28 <= score <= 30:
            grade.append(5)

    average = total / len(score_list)
    pass_percentage = ((len(score_list) - grade.count(0)) / len(score_list)) * 100

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage}")
    print("Grade distribution:")
    print(f"5: {grade.count(5) * "*"}")
    print(f"4: {grade.count(4) * "*"}")
    print(f"3: {grade.count(3) * "*"}")
    print(f"2: {grade.count(2) * "*"}")
    print(f"1: {grade.count(1) * "*"}")
    print(f"0: {grade.count(0) * "*"}")


main()