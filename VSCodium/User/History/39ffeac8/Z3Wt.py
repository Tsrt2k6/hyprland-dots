def main():
    text = input()
    words = text.split(" ")
    with open("wordlist.txt") as file:
        word_list = []
        for line in file:
            word_list.append(line.strip())
    