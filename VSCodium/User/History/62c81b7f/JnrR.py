def dict_of_numbers():
    store = {}
    for index in range(100):
        store[index] = spelled(index)
    return store

def spelled(num):
        words1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        words2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        words3 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        if 0 <= num <= 9:
            return words1[num]
        elif 10 <= num <= 19:
            return words2[num % 10]
        elif num > 19:
            if num % 10 != 0:
                return words3[num // 10 - 2] + "-" + words1[num % 10]
            else:
                return words3[num // 10 - 2]