def change_case(orig):
    result = ""
    for letter in orig:
        if letter.islower():
            result += upper(letter)
        else:
            result += letter.lower
    return result

change_case("HeLlO wOrLd")