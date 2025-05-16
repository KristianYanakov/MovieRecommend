import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

movies = pd.read_csv('data/ml-latest-small/movies.csv')
ratings = pd.read_csv('data/ml-latest-small/ratings.csv')

data = pd.merge(ratings, movies, on='movieId')

data = data.dropna()

data = data.reset_index(drop=True)

# tests

# movie = data['title'][4]
# rating = data['rating'][12345]
#
# print(movie)
# print(rating)

# Build pivot table
pivot = data.pivot_table(index="userId", columns='title', values='rating').fillna(0)

# Compute similarity
similarity = cosine_similarity(pivot)

# Get recommendations for a user
# def get_recommendations(user_index, top_n=5):
#     scores = list(enumerate(similarity[user_index]))
#     scores = sorted(scores, key = lambda x: x[1], reverse=True)
#
#     return [pivot.index[i] for i, _ in scores[:top_n]]

def get_recommendations(user_index, top_n=5):
    # Similar users
    scores = list(enumerate(similarity[user_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]  # skip self

    # Get top N similar users
    similar_user_indices = [i for i, _ in scores[:10]]
    similar_users = pivot.iloc[similar_user_indices]

    # Movies the target user hasn't rated yet
    user_rated_movies = pivot.iloc[user_index]
    unrated_movies = user_rated_movies[user_rated_movies == 0].index

    # Predict scores for unrated movies by averaging similar users' ratings
    mean_ratings = similar_users[unrated_movies].mean().sort_values(ascending=False)

    # Return top_n movies as (title, predicted_rating)
    return list(mean_ratings.head(top_n).items())

print(get_recommendations(1))

recs = get_recommendations(1)
for title, score in recs:
    print(f"{title}: {score:.2f}")