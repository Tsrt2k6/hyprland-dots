import string

def val_or_var(store, input):
    if input.isdigit():
        return int(input())
    else:
        return store[input]

def run(program):
    result = []

    store = {}
    for letter in string.ascii_uppercase:
        store[letter] = 0

    index = 0
    while True:
        line = program[index]
        print(line)
        line = line.split(" ")

        if line[0] == "PRINT":
            result.append(line[1])

        elif line[0] == "MOV":
            store[line[1]] = val_or_var(line[2])

        elif line[0] == "ADD":
            store[line[1]] += val_or_var(line[2])

        elif line[0] == "SUB":
            store[line[1]] -= val_or_var(line[2])

        elif line[0] == "MUL":
            store[line[1]] *= val_or_var(line[2])
        
        elif line[0] == "END":
            break

        index += 1

    return result
            
program1 = []
program1.append("MOV A 1")
program1.append("MOV B 2")
program1.append("PRINT A")
program1.append("PRINT B")
program1.append("ADD A B")
program1.append("PRINT A")
program1.append("END")
result = run(program1)
print(result)