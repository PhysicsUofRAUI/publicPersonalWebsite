

#
# Login
# Purpose:
#     To allow the user login
#
# Method:
#     if form submitted
#         if Values are correct
#             login the user
#
#             redirect to home
#
#         else
#             render login and flash that it was incorrect
#
#     else
#         render the login page
#
# Other Functions Needed:
#     login_user from flask_login
#     redirect, flash, and render_template from flask
#
#     All defined so we good :)
#
# GET and POST stuff:
#   the flask software largely takes care of it I guess. Check the dream team example.
# 

#
# Logout
# Purpose:
#     This function will respond when the user clicks the logout link by logging
#     the user out.
#
# Method:
#     logout user
#
#     set a flash to say logout was successful
#
#     redirect to the homepage
#
# Other Functions Needed:
#     redirect, flash, url_for from flask
#     logout_user from flask_login
#
