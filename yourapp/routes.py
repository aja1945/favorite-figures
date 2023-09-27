from flask import render_template
from yourapp import app

@app.route('/')
@app.route('/home')
def home():
    # Create a list of your favorite artists or sports figures
    favorite_figures = ["Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5"]
    return render_template('home.html', favorite_figures=favorite_figures)

@app.route('/favorite')
def favorite():
    return render_template('favorite.html')