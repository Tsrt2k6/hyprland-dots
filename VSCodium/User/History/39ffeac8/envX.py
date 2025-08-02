from difflib import get_close_matches

def main():
    text = input()
    words = text.split(" ")
    result = []
    wrong = []
    with open("wordlist.txt") as file:
        word_list = []
        for line in file:
            word_list.append(line.strip())
    for word in words:
        if word.lower() in word_list:
            result.append(word)
        else:
            result.append(f"*{word}*")
            wrong.append(word)
    print(" ".join(result))
    for word in wrong:
        matches = get_close_matches(word, word_list)
        print(f"{word}: {matches[0]}, {matches[1]}, {matches[2]}")
main()