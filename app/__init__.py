from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# create application factory functions

# from flask_bootstrap import Bootstrap


bootstrap = Bootstrap()

def create_app(config_name):
    app= Flask(__name__)

    #creating the app configuration
    app.config.from_object(config_options[config_name])

    #initializing the flask extensions
    bootstrap.init_app(app)

    #we will ad the viws and the form


    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .request import configure_request
    configure_request(app)



    return app
    