def first_word(sentence):
    word = ""
    i = 0
    while True:
        word += sentence[i]
        i += 1
        if sentence[i] == " ":
            break


def second_word(sentence):
    word = ""
    



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))