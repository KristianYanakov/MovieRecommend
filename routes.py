from flask import Flask, Blueprint, render_template, jsonify
from model import data, get_recommendations
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
        # return "Movie not found", 404
        return render_template('404.html'), 404

@routes.route('/movies/')
def get_all_movies():
    titles = data['title']
    ratings = data['rating']

    movies = [{'title': t, 'rating': r} for t, r in zip(titles, ratings)]
    return render_template('movies_list.html', movies=movies)

#API ENDPOINT ROUTES

@routes.route('/api/movies/', methods = ['GET'])
def api_get_all_movies():
    movies = [
        {'id': idx, 'title': row['title'], 'rating': row['rating']}
        for idx, row in data.iterrows()
    ]

    return jsonify(movies)

@routes.route('/api/movie/<int:movie_id>', methods = ['GET'])
def api_get_movie(movie_id):
    if 0 <= movie_id < len(data):
        row = data.iloc[movie_id]
        movie = {
            'id': movie_id,
            'title': row['title'],
            'rating': row['rating']
        }
        return jsonify(movie)
    else:
        # return jsonify({'message': 'Movie not found'}), 404
        return render_template('404.html'), 404

#Recommendations
@routes.route('/recommendations/<int:user_id>')
def get_recommendations_for_user(user_id):
    try:
        recommendations_all = get_recommendations(user_id, 5)
        recommendations_display_format = [{"title": title, "predicted_rating": round(score, 2)} for title, score in recommendations_all]

        return render_template('recommendations.html', user_id=user_id, recommendations=recommendations_display_format)
    except IndexError:
        return render_template('404.html'), 404
        # return f"User {user_id} not found", 404 #could render a 404 html

#API ENDPOINTS FOR RECOMMENDATIONS
@routes.route('/api/recommendations/<int:user_id>', methods = ["GET"])
def get_all_recommedations(user_id):
    try:
        recommendations_all = get_recommendations(user_id, 5)
        recommendations_display_format = [{"title": title, "predicted_rating": round(score, 2)} for title, score in recommendations_all]

        return jsonify(recommendations_display_format)
    except IndexError:
        return render_template('404.html'), 404
        # return f"User {user_id} not found", 404

@routes.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
