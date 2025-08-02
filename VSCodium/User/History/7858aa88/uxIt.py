def palindromes(word):
    reverse = ""
    for x in range(-1, -1 - len(word), -1):
        reverse += word[x]
    if reverse == word:
        print(word, "is a palindrome!")
    else:
        print("that wasn't a palindrome")