def final_points():
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            hours, mins = time.split(":")
            start[name] = int(hours), int(mins)
    with open("submissions.csv") as file:
        end = {}
        for line in file:
            name, task, points, time = line.strip().split(";")
            hours, mins = [int(x) for x in time.split(":")]
            hour_diff = hours - start[name][0]
            min_diff = mins - start[name][1]
            if hour_diff > 3 or (hour_diff == 3 and min_diff > 0):
                continue
            if name not in end:
                end[name] = {}
            if task not in end[name]:
                end[name][task] = points
            else:
                end[name][task] = max(end[name][task], points)
        store = {}
        for name in end:
            total = 0
            for task in end[name]:
                total += int(end[name][task])
            store[name] = total
    return store
    
