def cheaters():
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            start[name] = time
    with open("submissions.csv") as file:
        ends = {}
        for line in file:
            name, task, points, time = line.strip().split(";")
            ends[name] = time

    for name in start:
        start_time = start[name].split(":")
