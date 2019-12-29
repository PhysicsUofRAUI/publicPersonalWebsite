
#
# Travel
# Purpose:
#     This view will pull up travel blogs for the user to look at. It will also
#     respond to the clicks of specific categories
#
# Method:
#     if a subcategory is selected:
#         search the database for post in the category 'Travel' and the selected
#             subcategory
#
#         search for the travel subcategories
#
#         render the Travel page with those posts and the subcategories
#
#     else
#         search the database for all Travel Posts
#         search the database for travel subcategories
#
#         render the Travel page with all the posts and the subcategories
#
# Other Functions or classes needed:
#     render_template from flask
#     also need database manipulation stuff, and the Post and Get shit
#
# Need to look at:
#     database and Post and Get stuff
#

#
# Projects
# Purpose:
#     Pulls up the blog posts about projects for the user to see
#
# Method:
#     if specific Post is selected
#         search the database for that particular post
#
#         search for the project subcategories
#
#         render the Project page with that particular post and the subcategories
#     else if subcategory is selected:
#        search the database for post in the category 'Travel' and the selected
#             subcategory
#
#         search for the Project subcategories
#
#         render the Project page with those posts and the subcategories
#     else
#         search the database for all Project Posts
#         search the database for Project subcategories
#
#         render the Project page with all the posts and the subcategories
# Other Functions or classes needed:
#     render_template from flask
#     also need database manipulation stuff, and the Post and Get shit
#
# Need to look at:
#     database and Post and Get stuff
#     good stuff can be found by looking how departments are dealt with in the example
#

#
# Add Post
# Purpose:
#     allows the administrator to add a new blog post to the database
#
# Method:
#     check if user is logged in
#     create an empty PostForm
#
#     if a PostForm has been validated
#         create a new Post instance and make it's values equal to the submited values
#
#         try:
#             adding the new post
#             flash a success message
#         except:
#             flash that an error has occured
#
#         redirect to the Post page with that particular post as an input
#
#     render the add post template
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     PostForm from forms.py
#     several database, POST and GET stuff that will be figured later
#

#
# Edit Post
# Purpose:
#     to allow the user the abiltiy to edit an existing post
#
# Method:
#     check if user is logged in
#     Find the specified Post
#
#     Create a PostForm filled with the info from the specified Post
#
#     if the form has been validated
#         update the post with the new information
#
#         commit it to the database
#
#         flash a success message
#
#         redirect to the posts page
#
#     specify that the form should be filled with the data from the Post that was collected
#
#     render the edit page
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     PostForm from forms.py
#     several database, POST and GET stuff that will be figured later
#

#
# Delete Post
# Purpose:
#     allow a user to delete a post from the database
#
# Method:
#     (the link) /post/delete/<int: id number> // need GET and POST as methods
#
#     check if user is an administrator (logged in)
#
#     find the particular post
#
#     delete the post
#
#     commit the changes
#
#     flash a success message
#
#     redirect to the Home page (for now)
#
# Other Functions and such needed
#     the database (aka db) defined in the init.py
#     Post from models
#     render_template, flash from flask
#

#
# Add PostSubCategory
# Purpose:
#     Let the user add a new subcategory for posts.
#
