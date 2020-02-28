from werkzeug.security import generate_password_hash
from flask import flash, redirect, render_template, url_for
from . import auth
from .forms import LoginForm

# The simple login logout solution was found at the following link:
# https://pythonspot.com/login-authentication-with-flask/
# The bcrypt stuff was found here:
# https://uniwebsidad.com/libros/explore-flask/chapter-12/storing-passwords

# the password hash will be listed here I will run it later
password = "$2y$12$KwjuplvjdZYccEBLpn61iOLa9K0au1earsrimI9OMJV0itDByNGvK"
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
#     redirect, flash, and render_template from flask
#
#     All defined so we good :)
#
@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        if generate_password_hash(request.form['password']) == password and request.form['username'] == 'kody':
            session['logged_in'] = True
            flash('Login Successful!')

            return redirect(url_for('other.home'))


        # when login details are incorrect
        else:
            flash('Invalid username or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

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
#
@auth.route('/logout')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = False
        flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('other.home'))
