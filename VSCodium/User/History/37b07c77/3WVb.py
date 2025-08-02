def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)