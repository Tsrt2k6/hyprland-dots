def check(word):
    with open("wordlist.txt") as file:
        wordlist = [x.strip() for x in file]
    return word in wordlist

def main():
    text_list = input().split(" ")
    result = ""
    for word in text_list:
        if check(word):
            result += word
        else:
            result += f"*{word}*"
        result += " "
    print(result)