def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(5)
