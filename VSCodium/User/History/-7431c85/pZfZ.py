def find(s):
    word = ""
    while True:
        for letter in s:
            if word.startswith(letter):
                break
            else:
                word += letter
        


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7