#
# Forms
#     PhotoForm: Will hold all the fields needed to edit and add new photo entries
#

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
