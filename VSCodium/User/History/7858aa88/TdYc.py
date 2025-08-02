def palindromes(word):
    reverse = ""
    for x in range(-1, -len(word) - 1, -1):
        reverse += word[x]
    return reverse == word

while True:
    word = input()
    if palindromes(word):
        print(word, "is a palindrome!")
    else:
        print("that wasn't a palindrome")