# 🎬 Movie Recommender AI Web App

An AI-powered web application that recommends movies to users based on their preferences. Built with Flask, this app includes user interaction features like commenting on movies, viewing posters from the OMDb API, and receiving personalized recommendations.

---

## 🚀 Features

- ✅ Movie recommendation system using collaborative filtering
-
- ✅ View movie details including ratings and poster images
- ✅ Leave comments under individual movies
- ✅ Browse all movies in the dataset
- ✅ RESTful API endpoints for movies and recommendations
- ✅ Custom 404 error page
- ⏳ (Planned) Download recommendations as a PDF file
- ⏳ Search for movies by title
---

## 📂 Project Structure

movie-recommender-app/
│
├── app.py # Flask app entry point
├── routes.py # Main route definitions
├── model.py # Recommendation engine logic
├── comment.py # Comment model (SQLAlchemy)
├── templates/ # HTML templates (Jinja2)
│ ├── index.html
│ ├── movie.html
│ ├── movies_list.html
│ ├── recommendations.html
│ └── 404.html
├── static/ # Static assets (CSS, JS, images)
├── .env # Contains your OMDb API key
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

## ⚙️ Setup Instructions

## 1. Clone the Repository

git clone https://github.com/KristianYanakov/MovieRecommend
cd MovieRecommend

## 2. Create a virtual environment
python -m venv venv

Activate it:
source venv/bin/activate #On windows: venv\Scripts\activate

## 3. Install Dependencies
pip install requirements.txt

## 4. Add environment variables
Create a .env file and insert your own OMDB API key

OMDB_API_KEY=your_omdb_api_key_here

## 5. Run the app
python app.py

OR

flask run

The app will run at:
http://localhost:5000

## 🧠 Recommendation System
The recommendation engine uses collaborative filtering to suggest top 5 movies personalized for each user. The logic is contained in model.py.

## 📡 API Endpoints
GET /api/movies/ — Get all movies

GET /api/movie/<int:movie_id> — Get specific movie

GET /api/recommendations/<int:user_id> — Get recommendations for a user

## 💬 Comment Feature
Users can leave a comment (with their name) under each movie page. Comments are stored using SQLite via SQLAlchemy and sorted by timestamp.

## 📌 Planned Features
 PDF download of user recommendations

 User login and profile support

 Movie rating system

 Genre filters & advanced search

 Like/dislike system on comments

## 🛠 Built With
Flask

SQLAlchemy

Pandas

OMDb API

Bootstrap (for styling)

## 📄 License
This project is licensed under the MIT License. See LICENSE for more details.

## 🙌 Acknowledgements
MovieLens dataset for initial movie data

OMDb API for movie posters and metadata
