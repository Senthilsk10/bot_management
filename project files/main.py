import os
import sys
from app import app as flask_app


sys.path.insert(0, os.path.dirname(__file__))


def wsgi(environ, start_response):
    # Check if the request is for the Flask app, if so, call it
    return flask_app(environ, start_response)