def longest_series_of_neighbours(store):
    count1 = 1
    count2 = 1
    for x in range(1, len(store)):
        if (store[x-1] - store[x]) == 1 or (store[x-1] - store[x]) == -1:
            count1 += 1
            if count1 > count2:  # Makes sure that count2 is updated constantly instead of when the sequence of neighbours ends, because putting this in the else statement would make sequences that end due to reaching the end of the list not update the count2 fuc-
                count2 = count1
        else:
            count1 = 1
    return count2
