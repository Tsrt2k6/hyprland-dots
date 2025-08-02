def cheaters():
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            hours, mins = time.split(":")
            start[name] = hours, mins
        print(start)

cheaters()