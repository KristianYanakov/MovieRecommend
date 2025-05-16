from flask import Flask, Blueprint, render_template
from model import data
import requests
import os
from dotenv import load_dotenv

load_dotenv()

OMDB_API_KEY = os.getenv('OMDB_API_KEY')
#OMDB_API_KEY = '12302140123' #from api get key in .env
routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    # return "Hello Flask ML WEB App!"
    return render_template('index.html')

@routes.route('/hello')
def about():
    return "This is a Movie Recommender AI in which users can also put ratings for movies."

@routes.route('/movie/<int:movie_id>')
def get_movie(movie_id):
    if 0 <= movie_id < len(data):
        title = data.iloc[movie_id]['title']
        rating = data.iloc[movie_id]['rating']

        # Strip off the year (e.g., "Toy Story (1995)" -> "Toy Story")
        clean_title = title.rsplit('(', 1)[0].strip()

        response = requests.get(f'http://www.omdbapi.com/?t={clean_title}&apikey={OMDB_API_KEY}')
        image_url = None

        if response.ok:
            result = response.json()
            image_url = result.get('Poster')

        # return f'Movie {movie_id} : {title} {rating}'
        return render_template('movie.html', title=title, rating=rating, image_url=image_url)
    else:
        return "Movie not found", 404

@routes.route('/movies/')
def get_all_movies():
    titles = data['title']
    ratings = data['rating']

    movies = [{'title': t, 'rating': r} for t, r in zip(titles, ratings)]
    return render_template('movies_list.html', movies=movies)