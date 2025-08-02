def longest_series_of_neighbours(store):
    neighbour_count = 1
    max_count = 1
    for x in range(1, len(store)):
        if (store[x-1] - store[x]) == 1 or (store[x-1] - store[x]) == -1:
            neighbour_count += 1
        if neighbour_count > max_count:
            max_count = neighbour_count
        neighbour_count = 1

    return max_count
