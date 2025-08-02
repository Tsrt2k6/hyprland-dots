def palindromes():
    while True:
        word = input()
        reverse = ""
        for x in range(-1, -len(word) - 1, -1):
            reverse += word[x]
        print(reverse)

palindromes()