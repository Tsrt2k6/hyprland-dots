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
    return count2

print(longest_series_of_neighbours(1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25))