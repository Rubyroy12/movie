from flask import Flask
from .config import DevConfig

# initialization of applciation
app= Flask(__name__,instance_relative_config=True)# allows connection with instance

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views