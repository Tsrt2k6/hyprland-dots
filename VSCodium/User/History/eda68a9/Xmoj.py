def anagrams(word1, word2):
    for char in sorted(word1):
        if char not in word2:
            return False
    for char in sorted(word2):
        if char not in word1:
            return False
    return True
    