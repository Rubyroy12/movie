from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# initialization of applciation
app= Flask(__name__,instance_relative_config=True)# allows connection with instance

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


#Initializing flask extension
boostrap = Bootstrap(app)


from app import views
from app import error