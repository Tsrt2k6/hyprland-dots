def spruce(size):
    i = 1
    space = size -1
    while i < size * 2:
        print(space * " " + i "*")


if __name__ == "__main__":
    spruce(5)