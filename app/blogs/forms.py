from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import PostCategory, PostSubCategory
from .. import db
from flask_sqlalchemy import SQLAlchemy
#
# the style of using the select field was found from the example at this link
# https://stackoverflow.com/questions/35314102/get-choices-from-a-database-query-in-wtforms-and-flask-sqlalchemy
#


def category_choices() :
    return PostCategory.query

def sub_category_choices() :
    return PostSubCategory.query

#
# PostForm
# Purpose:
#     Gives the user a way to input information into the post table.
#
# Fields:
#     Title: String Field (Required)
#     Category: String Field (Required)
#     Subcategory: String Field (Required)
#     Content: Text Field (Required)
#     Submit: Submit Field
#
# Other Functions or Classes Needed:
#     TextAreaField, StringField, SubmitField from wtforms
#     FlaskForm from flask_wtf
#     Required from wtforms.validators
#
class PostForm(FlaskForm):
    """
    Form that lets the user add a new post
    """

    title = StringField('Title', validators=[DataRequired()])
    category = QuerySelectField('Category', validators=[DataRequired()], query_factory=category_choices)
    sub_category = QuerySelectField('SubCategory', validators=[DataRequired()], query_factory=sub_category_choices)
    content = TextAreaField('Content', validators=[DataRequired()])

    submit = SubmitField('Submit')

#
# SubCategoryForm
# Purpose:
#     allows user to add new subcategories
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
class SubCategoryForm(FlaskForm) :
    """
    Form used to submit new subcategories
    """
    name = StringField('Name', validators=[DataRequired()])

    submit = SubmitField('Submit')
