from flask import Flask
from config import config_options # create application factory functions
from flask_bootstrap import Bootstrap


Bootstrap = Bootstrap()


def create_app(config_name):
    app= Flask(__name__)

    #creating the app configuration
    app.config.from_object(config_options[config_name])

    #initializing the flask extensions
    bootstrap.init_app(app)

    #we will ad the viws and the form

    return app
    


# # initialization of applciation
# instance_relative_config=True)# allows connection with instance

# #setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')


# #Initializing flask extension
# b = Bootstrap(app)


# from app import views
# from app import error