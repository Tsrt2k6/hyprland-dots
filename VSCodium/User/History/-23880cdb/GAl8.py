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

def score_calc(word):
    

main()