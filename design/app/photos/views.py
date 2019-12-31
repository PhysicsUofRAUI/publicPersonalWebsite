
#
# Gallery
# Purpose:
#     It will display all the selected photos
#
# Method:
#     if a category is selected:
#         search the database for photos in the selected category
#
#         search for the photo categories
#
#         render the Gallery page with those photos and the gallery categories
#
#     else
#         search the database for all Photos
#         search the database for photo categories
#
#         render the Gallery page with all the photos and the categories
# Other Functions or classes needed:
#     render_template from flask
#     also need database manipulation stuff, and the Post and Get shit
#
# Need to look at:
#     database and Post and Get stuff
#
# Useful Advice:
#     The subcategory could be specified in the url as well. It could then be checked whether that
#     passed value is null or not and that can be how subcategories are specified.
#
#     See the dream team example and https://exploreflask.com/en/latest/views.html
#


#
# Add PhotoCategory
# Purpose:
#     Let the user add a new category for photos.
# Method:
#     check if the user is logged in
#
#     create a PhotoCategoryForm
#
#     if a PhotoCategoryForm has been validated
#         create a new photocategory instance and make it's values equal to the submited values
#
#         try:
#             adding the new photocategory
#             flash a success message
#         except:
#             flash that an error has occured
#
#         redirect to the Gallery page
#
#     render the add photocategory template
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     PhotoCategoryForm from forms.py
#     several database, POST and GET stuff that will be figured later
#


#
# Add Photo
# Purpose:
#     Allows the user to enter a new photo in the database
#
# Method:
#     check if user is logged in
#     create an empty PhotoForm
#
#     if a PhotoForm has been validated
#         create a new Photo instance and make it's values equal to the submited values
#
#         try:
#             adding the new photo
#             flash a success message
#         except:
#             flash that an error has occured
#
#         redirect to the Gallery page with that particular photo as an input
#
#     render the add photo template
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     PhotoForm from forms.py
#     several database, POST and GET stuff that will be figured later
#

#
# Edit Photo
# Purpose:
#     To allow the user to edit an existing photo entry in the database
#
# Method:
#     check if user is logged in
#     Find the specified Photo
#
#     Create a PhotoForm filled with the info from the specified Post
#
#     if the form has been validated
#         update the photo with the new information
#
#         commit it to the database
#
#         flash a success message
#
#         redirect to the Gallery page
#
#     specify that the form should be filled with the data from the Photo that was collected
#
#     render the edit page
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     PhotoForm from forms.py
#     several database, POST and GET stuff that will be figured later
#
# Useful advice:
#   the id of the post can be specified in the route. See this link: https://exploreflask.com/en/latest/views.html
#   also the dream team example does the same thing.
#

#
# Delete Photo
# Purpose:
#     allow a user to delete a photo from the database
#
# Method:
#     (the link) /gallery/delete/<int: id number> // need GET and POST as methods
#
#     check if user is an administrator (logged in)
#
#     find the particular photo
#
#     delete the photo
#
#     commit the changes
#
#     flash a success message
#
#     redirect to the Gallery
#
# Other Functions and such needed
#     the database (aka db) defined in the init.py
#     Photo from models
#     render_template, flash from flask
#
