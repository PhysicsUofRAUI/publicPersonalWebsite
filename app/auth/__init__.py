from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

# the blueprint style comes from the dream team example
