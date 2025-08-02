def line(length, character):
    if not character:
        character = "*"
    print(character[0] * length)
    
def shape(t_length, t_char, r_length, r_char):
    i = 1
    while i <= t_length:
        print(i * t_char)
        i += 1

if __name__ == "__main__":
    shape(5, "x", 2, "o")