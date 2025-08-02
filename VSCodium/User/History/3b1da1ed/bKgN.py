def find_movies(data, search_term):
    new = []
    for movie in data:
        if search_term.lower() in movie["name"].lower():
            new.append(movie)
    return new