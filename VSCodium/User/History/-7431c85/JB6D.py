def find(s):
    word = ""
    for letter in s:
        if word.startswith(letter) and word * (len(s) // len(word)) == s:
                break
        else:
            word += letter
    return len(word)


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7