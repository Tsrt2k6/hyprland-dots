def no_shouting(store):
    new = []
    for x in store:
        if x.isupper():
            new.append(x)
    return new