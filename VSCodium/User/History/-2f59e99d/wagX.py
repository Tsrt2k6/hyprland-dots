def change_case(orig):
    result = ""
    for letter in orig:
        if letter.islower():
            result += upper(letter)
        else:
            result += lower(letter)
    return result

change_case("HeLlO wOrLd")