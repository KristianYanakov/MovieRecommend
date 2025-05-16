import pandas as pd

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



