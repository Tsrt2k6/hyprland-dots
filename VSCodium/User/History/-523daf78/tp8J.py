def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)



if __name__ == "__main__":
    line(5, "x")