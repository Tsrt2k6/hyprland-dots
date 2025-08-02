def first_word(sentence):
    i = 0
    while True:
        if sentence[i] == " ":
            return sentence[:i]
        i += 1


def second_word(sentence):
    sentence += " "
    i = 0
    count = 0
    while True:
        if sentence[i] == " " and count == 0:
            sentence = sentence[i + 1:]
            count += 1
        else:
            return sentence[:i]
        i += 1


def last_word(sentence):
    i = -1
    while True:
        if sentence[i] == " ":
            return sentence[i + 1:] 
        i -= 1



if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))