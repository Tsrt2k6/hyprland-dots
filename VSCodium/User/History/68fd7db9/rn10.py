def same_chars(word, a, b):
    if a >= len(word) or b >= len(word):
        return False
    if word[a] != word[b]:
        return False
    return True


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))