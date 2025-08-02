import string

def val_or_var(store, input):
    return int(input) if input.isdigit() else store[input]

def run(program):
    result = []

    location = {}

    store = {}
    for letter in string.ascii_uppercase:
        store[letter] = 0

    index = 0
    while index < len(program):
        line = program[index]
        line = line.split(" ")

        if line[0] == "PRINT":
            result.append(val_or_var(store, line[1]))

        elif line[0] == "MOV":
            store[line[1]] = val_or_var(store, line[2])
        elif line[0] == "ADD":
            store[line[1]] += val_or_var(store, line[2])
        elif line[0] == "SUB":
            store[line[1]] -= val_or_var(store, line[2])
        elif line[0] == "MUL":
            store[line[1]] *= val_or_var(store, line[2])    

        elif line[0] == "END":
            break

        elif line[0] == "IF":
            match line[2]:
                case "==":
                    condition = (val_or_var(store, line[1]) == val_or_var(store, line[3]))
                case "!=":
                    condition = (val_or_var(store, line[1]) != val_or_var(store, line[3]))
                case "<":
                    condition = (val_or_var(store, line[1]) < val_or_var(store, line[3]))
                case "<=":
                    condition = (val_or_var(store, line[1]) <= val_or_var(store, line[3]))
                case ">":
                    condition = (val_or_var(store, line[1]) > val_or_var(store, line[3]))
                case ">=":
                    condition = (val_or_var(store, line[1]) >= val_or_var(store, line[3]))
            if condition:
                index = program.index(line[5] + ":")
                continue

        elif line[0] == "JUMP":
            index = program.index(line[1] + ":")
            continue

        index += 1

    return result