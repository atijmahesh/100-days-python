from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    

# CREATE TABLE
with app.app_context():
    db.create_all()


# TMDb API Key
TMDB_API_KEY = '8e17407bdff6becdc90ac9853a1b3319'

# Home route
@app.route("/")
def home():
    movies = Movie.query.order_by(desc(Movie.ranking)).all()
    return render_template("index.html", movies=movies)

# Add movie route
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form['title']
        # Perform a search request to TMDb API to find the movie by title
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={title}")
        data = response.json()
        movies = data.get('results', [])
        return render_template("select.html", movies=movies)
    return render_template("add.html")

# Select movie route
@app.route("/select")
def select():
    return render_template("select.html")

# Add movie to database route
@app.route("/add_to_db/<int:movie_id>", methods=["GET"])
def add_to_db(movie_id):
    # Use the movie ID to get full details from TMDb
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}")
    movie_data = response.json()

    # Extract movie details
    new_movie = Movie(
        title=movie_data['title'],
        year=movie_data['release_date'].split("-")[0],
        description=movie_data['overview'],
        rating=movie_data['vote_average'],
        ranking=0,  # You can adjust this as needed
        review="No review yet.",
        img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
    )

    # Add the movie to the database
    db.session.add(new_movie)
    db.session.commit()
    
    return redirect(url_for('home'))

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    if request.method == "POST":
        new_rating = request.form["rating"]
        new_review = request.form["review"]
        
        # Update rating and review in the database
        movie.rating = new_rating
        movie.review = new_review
        db.session.commit()  # Commit the changes to the database
        
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie)

@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()  # Commit the changes to the database
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
