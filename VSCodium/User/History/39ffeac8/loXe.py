def main():
    text = input()
    text += " "
    word = ""
    with open("wordlist.txt") as file:
        
    for letter in text:
        if letter != " ":
            word += letter
        else:
