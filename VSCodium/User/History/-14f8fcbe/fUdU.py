def everything_reversed(store):
    new = []
    for i in range(len(store) - 1, -1, -1):
        print(i)
        new.append(store[i][::-1])
    return new

everything_reversed(['fed', 'cba'])