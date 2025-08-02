def cheaters():
    cheats = []
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            hours, mins = time.split(":")
            start[name] = int(hours), int(mins)
    with open("submissions.csv") as file:
        end = {}
        for line in file:
            name, tast, points, time = line.strip().split(";")
            if name in cheats:
                continue
            hours, mins = [int(x) for x in time.split(":")]
            hour_diff = hours - start[name][0]
            min_diff = mins - start[name][1]
            if hour_diff > 3 or (hour_diff == 3 and min_diff > 0):
                cheats.append(name)
                continue
    return cheats

