def older_people(people, year):
    store = []
    for person in people:
        if person[1] < year:
            store.append(person[0])
    return store