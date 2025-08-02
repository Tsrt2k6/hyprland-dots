import string

def val_or_var(store, input):
    return int(input) if input.isdigit() else store[input]

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

        elif 

        elif program[index].endswith(":"):
            location = index
        elif line[0] == "JUMP":
            index = location
            continue

        index += 1

    return result
            
program2 = []
program2.append("MOV A 1")
program2.append("MOV B 10")
program2.append("begin:")
program2.append("IF A >= B JUMP quit")
program2.append("PRINT A")
program2.append("PRINT B")
program2.append("ADD A 1")
program2.append("SUB B 1")
program2.append("JUMP begin")
program2.append("quit:")
program2.append("END")
result = run(program2)
print(result)