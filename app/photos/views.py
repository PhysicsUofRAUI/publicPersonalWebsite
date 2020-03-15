from flask import render_template, session, redirect, url_for, flash
from .. import db
from . import photos
from .forms import PhotoForm, PhotoCategoryForm
from ..models import Photo, PhotoCategory

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
#
@photos.route('/gallery/<photo>', defaults={'category': None}, methods=['GET', 'POST'])
@photos.route('/gallery/<photo>/<category>', defaults={'photo': None}, methods=['GET', 'POST'])
@photos.route('/gallery', defaults={'category': None, 'photo': None}, methods=['GET', 'POST'])
def gallery(photo, category) :
    categories = PhotoCategory.query.all()
    if not photo == None :
        photos = Photo.query.filter_by(id=photo).order_by(Post.id.desc())

        return render_template('gallery.html', Photos=photos, categories=categories)

    elif not category == None :
        photos = Photo.query.filter_by(category_id=category).order_by(Post.id.desc())

        return render_template('gallery.html', Photos=photos, categories=categories)

    else :
        photos = db.session.query(Photo).all().order_by(Post.id.desc())

        return render_template('gallery.html', Photos=photos, categories=categories)

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
@photos.route('/add_photocategory', methods=['GET', 'POST'])
def add_photocategory():
    """
    Add a photocategory
    """
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    form = PhotoCategoryForm()

    if form.validate_on_submit():
        new_photocategory = PhotoCategory(name=form.name.data)

        try:
            db.session.add(new_photocategory)
            db.session.commit()
            flash('You have successfully added a new photo category')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_photocategory.html', form=form)


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
@photos.route('/add_photo', methods=['GET', 'POST'])
def add_photo():
    """
    Add a photo
    """
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    form = PhotoForm()

    if form.validate_on_submit():
        new_photo = Photo(filename=form.file_name.data, caption=form.caption.data, category_id=form.category.data.id, category=form.category.data)

        try:
            db.session.add(new_photo)
            db.session.commit()
            flash('You have successfully added a new photo!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_photo.html', form=form)

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
@photos.route('/edit_photo/<int:id>', methods=['GET', 'POST'])
def edit_photo(id):
    """
    Edit a photo
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    photo = Photo.query.get_or_404(id)
    form = PhotoForm(obj=photo)
    if form.validate_on_submit():
        photo.filename = form.file_name.data
        photo.caption = form.caption.data
        photo.category_id = form.category.data.id # US
        photo.category = form.category.data # US

        db.session.commit()
        flash('You have successfully edited the blog post.')

        # redirect to the home page
        return redirect(url_for('other.home'))

    form.caption.data = photo.caption
    form.file_name.data = photo.filename
    form.category.data = photo.category # US
    return render_template('edit_photo.html', form=form, photo=photo, title="Edit Photo")

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
@photos.route('/delete_photo/<int:id>', methods=['GET', 'POST'])
def delete_photo(id):
    """
    Delete a photo from the database
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    photo = Photo.query.get_or_404(id)
    db.session.delete(photo)
    db.session.commit()
    flash('You have successfully deleted the photo.')

    # redirect to the home page
    return redirect(url_for('other.home'))
