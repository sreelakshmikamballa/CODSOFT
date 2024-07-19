# Sample data: movies with features
movies = [
    {"id": 1, "title": "The Matrix", "genre": "Action", "director": "Wachowski"},
    {"id": 2, "title": "Inception", "genre": "Action", "director": "Nolan"},
    {"id": 3, "title": "Interstellar", "genre": "Sci-Fi", "director": "Nolan"},
    {"id": 4, "title": "The Godfather", "genre": "Crime", "director": "Coppola"},
    {"id": 5, "title": "Pulp Fiction", "genre": "Crime", "director": "Tarantino"},
]

# User preferences
user_preferences = {"genre": "Action", "director": "Nolan"}

# Function to compute similarity score
def compute_similarity(movie, user_preferences):
    score = 0
    if movie["genre"] == user_preferences["genre"]:
        score += 1
    if movie["director"] == user_preferences["director"]:
        score += 1
    return score

# Recommend movies based on user preferences
def recommend_movies(movies, user_preferences):
    recommendations = []
    for movie in movies:
        similarity_score = compute_similarity(movie, user_preferences)
        if similarity_score > 0:  # Only recommend if there's some similarity
            recommendations.append((similarity_score, movie))
    recommendations.sort(reverse=True, key=lambda x: x[0])
    return [movie for score, movie in recommendations]

# Get recommendations
recommended_movies = recommend_movies(movies, user_preferences)

# Print recommended movies
print("Recommended Movies:")
for movie in recommended_movies:
    print(f"{movie['title']} (Genre: {movie['genre']}, Director: {movie['director']})")
