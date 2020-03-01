from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash, redirect, render_template, url_for, request, session
from . import auth
from .forms import LoginForm

# The simple login logout solution was found at the following link:
# https://pythonspot.com/login-authentication-with-flask/
# The bcrypt stuff was found here:
# https://uniwebsidad.com/libros/explore-flask/chapter-12/storing-passwords

passwrd = 'pbkdf2:sha256:150000$y6icYOFI$a8055a0ba1820ab85b52de7e6a57d3dfec22891e08e961f3dc27d7007aac37a8'
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
@auth.route('/login', methods=['Get', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        if check_password_hash(passwrd, form.password.data) and form.username.data == 'kody':
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
