from string import 

def change_case(orig):
    result = ""
    for letter in orig:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result

def split_in_half(orig):
    index = len(orig) // 2
    return orig[:index], orig[index:]

def remove_special_characters(orig):
