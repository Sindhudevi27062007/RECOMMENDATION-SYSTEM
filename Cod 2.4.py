# Expanded movie dataset with more genres
movies = [
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
    {"title": "The Conjuring", "genre": "Horror"},
    {"title": "Titanic", "genre": "Romance"},
    {"title": "Get Out", "genre": "Horror"},
    {"title": "The Matrix", "genre": "Sci-Fi"},
    {"title": "The Fault in Our Stars", "genre": "Romance"},
    {"title": "Mad Max: Fury Road", "genre": "Action"},
    {"title": "John Wick", "genre": "Action"},
    {"title": "Mission: Impossible", "genre": "Action"},
    {"title": "The Dark Knight", "genre": "Thriller"},
    {"title": "Joker", "genre": "Thriller"},
    {"title": "The Hangover", "genre": "Comedy"},
    {"title": "Superbad", "genre": "Comedy"},
    {"title": "The Pursuit of Happyness", "genre": "Drama"},
    {"title": "Forrest Gump", "genre": "Drama"}
]

def recommend_movies(user_genre):
    recommended = []
    for movie in movies:
        if movie["genre"].lower() == user_genre.lower():
            recommended.append(movie["title"])
    return recommended

# User interaction
print("🎬 Welcome to the Movie Recommender!")
print("Available genres: Sci-Fi, Romance, Horror, Action, Thriller, Comedy, Drama")

user_input = input("Enter your favorite genre: ")

recommendations = recommend_movies(user_input)

if recommendations:
    print("\n✅ Recommended Movies:")
    for movie in recommendations:
        print("•", movie)
else:
    print("\n❌ Sorry, no movies found for that genre.")
