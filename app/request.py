from app import app
import urllib.request,json #help to create a connection to our api url and send request 
from .models import movie

Movie = movie.Movie


#getting api-key
api_key = app.config['MOVIE_API_KEY']

#getting the base url
base_url = app.config['MOVIE_API_BASE_URL']


def get_movies(category):
    """
    function that get the json response to our url request
    """
    get_movies_url = base_url.format(category,api_key)#to replace the curly braces in the url

    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data= url.read()
        get_movies_response=json.loads(get_movies_data)

        movie_results= None

        if get_movies_response['results']:
            movie_results_list= get_movies_response['results']
            movie_results= process_results(movie_results_list)
            
        
    return movie_results


def process_results(movie_list):
    """
    Function that process the movie results and transform them into  a list of objects
    args: 
    movie_list: alist of dictionaries that contain movie details

    returns: list of movie objects
    
    """

    movie_results=[]
    for movie_item in movie_list:
        id= movie_item.get('id')
        title = movie_item.get('title')
        overview= movie_item.get('overview')
        poster= movie_item.get('poster')
        vote_average= movie_item.get('vote_average')
        vote_count= movie_item.get('vote_count')

        if poster:
            movie_object= Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)
    return movie_results



    