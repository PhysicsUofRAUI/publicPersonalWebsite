from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, redirect, render_template, url_for, request, session
from . import auth
from .forms import LoginForm
from config import Config

# The simple login logout solution was found at the following link:
# https://pythonspot.com/login-authentication-with-flask/
# The bcrypt stuff was found here:
# https://uniwebsidad.com/libros/explore-flask/chapter-12/storing-passwords

#
# My password that was previously hashed
# To add a new password it world have to be hashed and then that hash would be
# added.
#
passwrd = Config.user_password_hash

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
@auth.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        if check_password_hash(passwrd, form.password.data) and form.username.data == 'your-username-here':
            session['logged_in'] = True
            flash('Login Successful!')

            return redirect(url_for('other.home'))


        # when login details are incorrect
        else:
            flash('Invalid username or password.')

    # load login template
    return render_template('login.html', form=form, title='Login')

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
@auth.route('/logout')
def logout():
    if session.get('logged_in'):
        session['logged_in'] = False
        flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('other.home'))
