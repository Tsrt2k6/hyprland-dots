import urllib.request, json

def retrieve_all():
    website = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    conv = json.load(website)
    store = []
    for week in conv:
        if week['enabled'] == True:
            fullName = week['fullName']
            name = week['name']
            year = week['year']
            exercises = sum(week['exercises'])
            store.append((fullName, name, year, exercises))
    return store

def retrieve_course(course_name):
    website = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    conv = json.load(website)
    store = {}
    week = 0
    students = 0
    hours = 0
    exercise = 0
    for line in conv:
        week += 1
        content = conv[line]
        students = max(students, content['students'])
        hours += content['hour_total']
        exercise += content['exercise_total']
    hours_avg = hours // students
    exercise_avg = exercise // students

    print( {'weeks': week,
            'students': students,
            'hours': hours,
            'hours_average': hours_avg,
            'exercises': exercise,
            'exercises_average': exercise_avg}    )

retrieve_course("docker2019")