def longest_series_of_neighbours(store):
    count1 = 1
    count2 = 1
    for x in range(1, len(store)):
        if (store[x-1] - store[x]) == 1 or (store[x-1] - store[x]) == -1:
            count1 += 1
        else:
            if count1 > count2:
                count2 = count1
            count1 = 1
    if count1 > count2:
        return count1
    return count2
