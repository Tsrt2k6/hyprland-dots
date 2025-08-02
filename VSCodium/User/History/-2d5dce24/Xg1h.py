def cheaters():
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            hours, mins = [int(x) for x in time.split(":")]
            start[name] = hours, mins
    with open("submissions.csv") as file:
        ends = {}
        for line in file:
            name, task, points, time = line.strip().split(";")
            hours, mins = [int(x) for x in time.split(":")]
            if name in ends:
                if ends[name][0] - hours > 0:
                    pass
                elif ends[name][0] - hours == 0 and ends[name][1] - mins > 0:
                    pass
                else:
                    continue
            ends[name] = (hours, mins)
    for name in start:
        cheat = []
        hour_diff = ends[name][0] - start[name][0]
        min_diff = ends[name][1] - start[name][1]
        if hour_diff >= 3:
            print(min_diff)
            if min_diff > 0 or hour_diff > 3:
                cheat.append(name)

    return cheat

print(cheaters())