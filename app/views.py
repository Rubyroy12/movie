from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie

@app.route('/') 
def index():
    """
    View root page function that returns the template and its data
    
    """
    #getting popular movies
    popular_movies= get_movies('popular')
    upcoming_movie= get_movies('upcoming')
    now_showing_movie= get_movies('now_playing')
    print(popular_movies)
    message = 'Flask is a Python web framework that makes it easy to create a fully-featured web application. Learn the basics of this popular framework so that you can create your own web application with a Python back-end.'
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')

    if search_movie:
       return redirect(url_for('search',movie_name=search_movie))
    else:
        """Return"""
        
        return render_template('index.html',message=message,title=title,popular=popular_movies,upcoming=upcoming_movie,now_showing=now_showing_movie)

@app.route('/movie/<int:id>')
def movie(id):
    """
    view movie page ufnctionthat returns the movie page and ista data
    
    """
    movie = get_movie(id)
    title = f'{movie.title}'

    return render_template('movie.html', movie=movie, title=title)

@app.route('/search/<movie_name>')
def search(movie_name):
    """
    view function to display tye search results
    
    """
    movie_name_list = movie_name.split('')
    movie_name_format= "+".join(movie_name_list)
    searched_movies= search_movie(movie_name_format)
    title= f'search results for {movie_name}'
    return render_template('search.html', movies=searched_movies)

    


