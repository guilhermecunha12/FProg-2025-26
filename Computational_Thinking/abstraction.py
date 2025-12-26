def get_watched_movies(user, database):
    pass # specific implementation

def get_favourite_genre(movies):
    pass # specific implementation

def get_favourite_actors(movies):
    pass # specific implementation

def get_movies(genre, actors):
    pass # speficic implementation

def load_database():
    pass # specific implementation

def recommend_movies(user, database):
    watched_movies = get_watched_movies(user, database)
    favourite_genre = get_favourite_genre(watched_movies)
    favourite_actors = get_favourite_actors(watched_movies)
    
    recommended_movies = get_movies(favourite_genre, favourite_actors)
    return recommended_movies

def main(): # only 4 lines!
    user = input()
    database = load_database()
    recommended_movies = recommend_movies(user, database)
    print(recommended_movies)

if __name__ == "__main__":
    main()