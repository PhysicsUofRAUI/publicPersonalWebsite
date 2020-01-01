from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import PhotoCategory
from .. import db

#
# the style of using the select field was found from the example at this link
# https://stackoverflow.com/questions/35314102/get-choices-from-a-database-query-in-wtforms-and-flask-sqlalchemy
#
def category_choices() :
    return db.session.query(PostCategory).all()

#
# PhotoForm
# Purpose:
#     This form will hold all of the fields needed to specify a photo in the database.
#     It will be used to add and edit a photo
#
# Fields:
#     FileName: StringField (Required)
#     Category: StringField
#     Caption: TextAreaField
#     Submit: SubmitField
#
# Things that will need to be included:
#     StringField, TextAreaField, and SubmitField from wtforms
#     FlaskForm from flask_wtf
#     Required from wtforms.validators
#
class PhotoForm(FlaskForm):
    """
    Form that lets the user add a new post
    """

    file_name = StringField('File Name', validators=[DataRequired()])
    category = QuerySelectField('Category', validators=[DataRequired()], query_factory=category_choices())
    caption = TextAreaField('Caption', validators=[DataRequired()])

    submit = SubmitField('Submit')

#
# PhotoCategoryForm
# Purpose:
#     allows user to add new categories for photos
#
# Fields:
#     Name: String Field (Required)
#     Submit: SubmitField
#
# Other Functions or Classes Needed:
#     StringField, SubmitField from wtforms
#     FlaskForm from flask_wtf
#     Required from wtforms.validators
#
class PhotoCategoryForm(FlaskForm) :
    """
    Form used to submit new subcategories
    """
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Submit')
