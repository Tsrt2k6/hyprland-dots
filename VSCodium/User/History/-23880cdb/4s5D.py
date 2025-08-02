def main():
    score_list = user_input()
    total = score_calc(score_list)
    statistics(total)

def user_input():
    score_list = []
    while True:
        scores = input()
        if scores == "":
            break
        score_list.append(scores)
    return score_list

def score_calc(score_list):
    total = []
    for score in score_list:
        exam, exercise = score.split()
        if int(exam) < 10:   # Exception cutoff point, results in insta fail lol
            total.append(0)
        else:
            sum = int(exam) + int(exercise) // 10
            total.append(sum)
    return total

def statistics(score_list):
    total = 0
    fail_count = 0
    for score in score_list:
        total += score
        if score < 15:
            grade.append(0)
            fail += 1
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
    pass_percentage = (len(score_list) - 1) / len(score_list)

    print("Statistics:")
    print(f"Points average: {average:.1f}")
    print(f"Pass percentage: {pass_percentage}")


main()