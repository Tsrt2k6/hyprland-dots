import string

def value(store, input):
    return int(input) if input.isdigit() else store[input]

def run(program):
    result = []

    store = {}
    for letter in string.ascii_uppercase:
        store[letter] = 0

    index = 0
    while index < len(program):
        line = program[index]
        line = line.split(" ")

        match line[0]:

            case "PRINT":
                result.append(value(store, line[1]))

            case "MOV":
                store[line[1]] = value(store, line[2])
            case "ADD":
                store[line[1]] += value(store, line[2])
            case "SUB":
                store[line[1]] -= value(store, line[2])
            case "MUL":
                store[line[1]] *= value(store, line[2])    

            case "END":
                break

            case "IF":
                match line[2]:
                    case "==":
                        condition = (value(store, line[1]) == value(store, line[3]))
                    case "!=":
                        condition = (value(store, line[1]) != value(store, line[3]))
                    case "<":
                        condition = (value(store, line[1]) < value(store, line[3]))
                    case "<=":
                        condition = (value(store, line[1]) <= value(store, line[3]))
                    case ">":
                        condition = (value(store, line[1]) > value(store, line[3]))
                    case ">=":
                        condition = (value(store, line[1]) >= value(store, line[3]))
                if condition:
                    index = program.index(line[5] + ":")
                    continue

            case "JUMP":
                index = program.index(line[1] + ":")
                continue

        index += 1

    return result