def check(word):
    with open("wordlist.txt") as file:
        wordlist = [x.strip() for x in file]
    return word in wordlist

def main():
    