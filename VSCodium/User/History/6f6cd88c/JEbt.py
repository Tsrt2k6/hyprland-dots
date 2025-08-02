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

        match line[0]:

            case "PRINT":
                result.append(val_or_var(store, line[1]))

            case "MOV":
                store[line[1]] = val_or_var(store, line[2])
            case "ADD":
                store[line[1]] += val_or_var(store, line[2])
            case "SUB":
                store[line[1]] -= val_or_var(store, line[2])
            case "MUL":
                store[line[1]] *= val_or_var(store, line[2])    

            case "END":
                break

            case "IF":
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

            case "JUMP":
                index = program.index(line[1] + ":")
                continue

        index += 1

    return result