def csv_copy(file_name):
    store = {}
    with open(file_name) as file:
        for line in file:
            line_list = line.split(";")
            if line_list[0] == "id":
                continue
            store[line_list[0]] = []
            for word in line_list[1:]:
                if type(word) == type(0):
                    store[line_list[0]].append(int(word))
    return store

print(csv_copy("students1.csv"))