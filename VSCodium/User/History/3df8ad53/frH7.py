def oldest_person(people):
    oldest = people[0]
    for index in range(1, len(people)):
        if people[index][1] < oldest[1]:
            oldest = people[index]
    return [1]

