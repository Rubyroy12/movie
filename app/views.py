from flask import render_template
from app import app

@app.route('/')
def index():
    """
    View root page function that returns the template and its data
    
    """
    message = 'Flask is a Python web framework that makes it easy to create a fully-featured web application. Learn the basics of this popular framework so that you can create your own web application with a Python back-end.'
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',message=message,title=title)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
    view movie page ufnctionthat returns the movie page and ista data
    
    """
    # movie_id = 1234
    return render_template('movie.html', id=movie_id)
