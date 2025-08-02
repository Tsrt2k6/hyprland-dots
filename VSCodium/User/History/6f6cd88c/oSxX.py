import string

def val_or_var(store, input):
    return int(input) if input.isdigit() else store[input]

def run(program):
    result = []

    store = {}
    for letter in string.ascii_uppercase:
        store[letter] = 0

    index = 0
    while index < len(program):
        line = program[index]
        print(line)
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


program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
print(result)