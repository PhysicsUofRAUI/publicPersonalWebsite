#
# Creates the blueprint for other pages (right now resume and the homepage)
#
from flask import Blueprint

other = Blueprint('other', __name__)

from . import views
