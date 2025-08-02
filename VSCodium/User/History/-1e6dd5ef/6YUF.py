import urllib.request, json

def retrieve_all():
    website = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    conv = json.load(website)
    store = []
    for week in conv:
        if week['enabled'] == True:
            name = week('fullname')
            name = week('name')

retrieve_all()