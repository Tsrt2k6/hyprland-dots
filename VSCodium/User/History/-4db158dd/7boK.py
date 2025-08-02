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
    long1 = stations[station1][0]
    lat1 = stations[station1][1]

    long2 = stations[station2][0]
    lat2 = stations[station2][1]

    x_km = (long1 - long2) * 55.26
    y_km = (lat1 - lat2) * 111.2
    distance_km = (x_km**2 + y_km**2) ** 0.5


stations = get_station_data('stations1.csv')
d = distance(stations, "Designmuseo", "Hietalahdentori")
print(d)
d = distance(stations, "Viiskulma", "Kaivopuisto")
print(d)