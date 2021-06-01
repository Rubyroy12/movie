from flask import render_template
from app import app

@app.route('/')
def index():
    """
    View root page function that returns the template and its data
    
    """
    message = 'Flask is a Python web framework that makes it easy to create a fully-featured web application. Learn the basics of this popular framework so that you can create your own web application with a Python back-end.'
    return render_template('index.html',message=message)