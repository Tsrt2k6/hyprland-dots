def main():
    text = input()
    words = text.split(" ")
    result = []
    with open("wordlist.txt") as file:
        word_list = []
        for line in file:
            word_list.append(line.strip())
    for word in words:
        if word in word_list:
            result.append(word)
        else:
            result.append(f"")