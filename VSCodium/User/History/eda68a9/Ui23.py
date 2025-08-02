def anagrams(word1, word2):
    for char in word1:
        if char not in word2:
            return False
    for char in word2:
        if char not in word1:
            return False
    return True
    
if "__name__" != "__main__":
    print(anagrams('test', 'set'))