def count(s):
    count0 = 0
    count1 = 1
    for digit in s:
        match digit:
            case "0":
                count0 += 1
            case "1":
                count1 += 1
    return min(count0, count1)

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("101111101")) # 4