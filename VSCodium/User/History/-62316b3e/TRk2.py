store = []
count = 0
while True:
    word = input()
    store.append(word)
    if word in store:
        break
    count += 1

print(f"You typed in {count} different words")