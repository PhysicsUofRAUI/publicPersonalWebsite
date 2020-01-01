#
# Will import the and create the photos blueprint
#
from flask import Blueprint

photos = Blueprint('photos', __name__)

from . import views
