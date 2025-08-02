def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)

def square(size, character):
    i = 0
    while i < size:
        line(size, character)
        i += 1

if __name__ == "__main__":
    square(5, "x")