def find_movies(data, search_term):
    new = []
    for movie in data:
        if search_term in movie["name"].lower():
            new.append(movie)
    return new