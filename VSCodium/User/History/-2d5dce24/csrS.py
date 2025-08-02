def cheaters():
    with open("start_times.csv") as file:
        store = {}
        for line in file:
            name, time = line.strip().split(";")
            store[name] = time
    with open("submissions.csv") as file:
        stor