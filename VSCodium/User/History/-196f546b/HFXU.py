from datetime import datetime, timedelta

def final_points():
    with open("start_times.csv") as file:
        start = {}
        for line in file:
            name, time = line.strip().split(";")
            hours, mins = time.split(":")
            time = datetime.strptime(time, "%H:%M")
            start[name] = time
    with open("submissions.csv") as file:
        end = {}
        for line in file:
            name, task, points, time = line.strip().split(";")
            time = datetime.strptime(time, "%H:%M")
            if time - start[name] > timedelta(hours=3):
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
    
