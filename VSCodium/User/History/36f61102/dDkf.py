def spruce(size):
    i = 1
    while i <= size:
        print((size - i) * " " + i * "*")
        i += 1

if __name__ == "__main__":
    spruce(5)