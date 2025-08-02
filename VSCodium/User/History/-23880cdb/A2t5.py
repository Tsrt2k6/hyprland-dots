def main():
    score_calc(user_input())

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
        if int(exam) < 10:
            total.append(0)
        else:
            sum = int(exam) + int(exercise) // 10
            total.append(sum)
        


main()