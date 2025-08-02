# Write your solution here

def add_course(store, name, course):
    if course[1] == 0:
        return
    courses = store[name]
    for index in range(len(courses)):
        if courses[index][0] == course[0]:
            if courses[index][1] < course[1]:   
                courses[index] = course   
            return      
    courses.append(course)