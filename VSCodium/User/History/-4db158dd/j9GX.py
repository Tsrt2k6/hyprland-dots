def get_station_data(file_name):
    with open(file_name) as file:
        store = {}
        for line in file:
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            store[line[3]] = (line[0], line[1])
    return store