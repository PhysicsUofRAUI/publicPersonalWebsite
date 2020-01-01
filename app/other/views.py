from flask import render_template
from . import home

#
# Home
# Purpose:
#     will display the home page of the website both '/' and '/home' are used
#     so that this is the first page shown and the page that is shown when home is
#     requested
#
# Method:
#     render the home page template
#     (next version may include a search for Photos to make it more dynamic)
#
# Other Functions and Classes needed:
#     render_template from flask
#
@other.route('/')
@other.route('/home')
def homepage():
    render_template("home.html", title='Home')

#
# Resume
# Purpose:
#     displays my resume in HTML with the download links at the bottom
#
# Method:
#     render the resume page template
#
# Other Functions and Classes needed
#     render_template from flask
#
@other.route('/resume')
def resume() :
    render_template('resume.html', title='Resume')
