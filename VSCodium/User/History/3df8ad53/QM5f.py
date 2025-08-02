def oldest_person(people):
    oldest = people[0][0]
    for index in range(1, len(people)):
        if people[index][1] < people[index-1][1]:
            oldest = people[index][0]
    return oldest

people_list = [('Donald', 1982), ('Daisy', 1892), ('Angela', 1965), ('Vladimir', 2000), ('Dunja', 1919), ('Elizabeth', 1921)]
result = oldest_person(people_list)