def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)

def triangle(size):
    i = 0
    while i < size:
        line(i, "#")

if __name__ == "__main__":
    triangle(5)
