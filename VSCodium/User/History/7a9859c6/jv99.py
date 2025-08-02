def longest_series_of_neighbours(store):
    count1 = 1
    count2 = 1
    for x in range(1, len(store)):
        if store[x-1] 