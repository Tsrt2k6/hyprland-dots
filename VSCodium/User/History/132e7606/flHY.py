def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)

def square_of_hashes(size):
    line(4, "#")

if __name__ == "__main__":
    square_of_hashes(5)
