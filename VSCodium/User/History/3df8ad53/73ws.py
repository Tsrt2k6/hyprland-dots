def oldest_person(people):
    oldest = people[0][0]
    for index in range(1, len(people)):
        if people[index][1] < people[index-1][1]:
            oldest = people[index][0]
    return oldest
