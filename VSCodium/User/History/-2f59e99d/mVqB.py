def change_case(orig):
    result = ""
    for letter in orig:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result

print(change_case("HeLlO wOrLd"))