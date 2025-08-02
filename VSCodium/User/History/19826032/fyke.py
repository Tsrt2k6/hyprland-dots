def no_vowels(word):
    vowels = "aiueo"
    for x in vowels:
        word = word.replace(x, "")

    return word