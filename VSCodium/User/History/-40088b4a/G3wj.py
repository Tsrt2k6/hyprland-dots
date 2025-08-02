def count(t):
    i = 0
    for x in range(len(t)):
        for y in range(x + 1, len(t)):
            if t[x] > t[y]:
                i += 1
    return i


if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12