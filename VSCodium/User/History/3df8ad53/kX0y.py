def oldest_person(people):
    oldest = people[0][0]
    for index in range(1, len(people)):
        if people[index][1] > people[index-1][1]:
            oldest = people[index][0]
    return oldest

p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))