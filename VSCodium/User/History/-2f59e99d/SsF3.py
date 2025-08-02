def change_case(orig):
    result = ""
    for letter in orig:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result

def split_in_half(orig):
    index = (len(orig) - 1) // 2
    return orig[:index], orig[index:]

print(split_in_half("somethin"))