def get_station_data(file_name):
    with open(file_name) as file:
        store = {}
        for line in file:
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            store[line[3]] = (float(line[0]), float(line[1]))
    return store

def distace(stations, station1, station2):
    longitude


stations = get_station_data('stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)