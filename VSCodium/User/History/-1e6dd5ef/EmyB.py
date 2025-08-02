import urllib.request, json

def retrieve_all():
    website = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    conv = json.load(website)
    store = []
    for week in conv:
        if week['enabled'] == True:
            fullname = week('fullname')
            name = week('name')
            year = week('year')
            exercises = sum(week[exercises])
            store.append(fullname, name, year, exercises)

retrieve_all()