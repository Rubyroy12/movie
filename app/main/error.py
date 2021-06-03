from flask import render_template
from . import main #main is the blueprint instance here

@main.app.errorhandler(404)
def four_ow_four(error):
    """
    Function to handle the 404 error page.
    """
    return render_template('fourOwfour.html'), 404