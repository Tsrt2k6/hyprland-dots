store = []
count = 0
while True:
    word = input()
    if word in store:
        break
    count += 1

print(f"You typed in {count} different words")