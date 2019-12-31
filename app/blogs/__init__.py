#
# Blueprint structure is meant to mirror that of the dreamteam example
#
from flask import Blueprint

blogs = Blueprint('blogs', __name__)

from . import views
