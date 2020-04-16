from flask import render_template, session, redirect, url_for, flash
from .. import db
from . import photos
from .forms import PhotoForm, PhotoCategoryForm
from ..models import Photo, PhotoCategory
from app.database import db_session

# Notes:
#   Much difficulty was faced when deploying the website with regards to getting a
#   mysql has gone away error. It was fixed after the following three lines were added
#   after each database access
#   db_session.close()
#   db_session.remove()
#   db_session.rollback()

#
# Gallery
# Description:
#   This view is the only one that displays photos. There are three optional parameters
#   each of which give a different option that for the function. The parameters are
#   described in the parameter section.
#
# Parameters:
#   photo: This allows for one specific photo to be loaded.
#
#   category: this allows a specific category of photos to be loaded (ex the 'Belgium'
#       photos)
#
#   page: The page is a designation for what page we are on in the pagination.
#
@photos.route('/gallery/<photo>/<page>', defaults={'category': None}, methods=['GET', 'POST'])
@photos.route('/gallery/<photo>/<category>/<page>', defaults={'photo': None}, methods=['GET', 'POST'])
@photos.route('/gallery/<page>', defaults={'category': None, 'photo': None}, methods=['GET', 'POST'])
@photos.route('/gallery', defaults={'category': None, 'photo': None, 'page' : 0}, methods=['GET', 'POST'])
def gallery(photo, category, page) :
    page = int(page)
    categories = PhotoCategory.query.all()

    if not photo == None :
        # if a specific photo has been selected this if statement will be ran
        photos = Photo.query.filter_by(id=photo).order_by(Photo.id.desc()).offset(page * 5).limit(5)
        more = Photo.query.filter_by(category_id=category).offset((page + 1) * 5).first()

        db_session.close()
        db_session.remove()
        db_session.rollback()

        if page != 0 :
            prev_url = url_for('photos.gallery', category=category, page=page - 1)
        else :
            prev_url = None

        if not more == None :
            next_url = url_for('photos.gallery', category=category, page=page + 1)
        else :
            next_url = None

        return render_template('gallery.html', Photos=photos, categories=categories, next_url=None, prev_url=None)

    elif not category == None :
        # if a specific category has been selected this if statement will be ran
        photos = Photo.query.filter_by(category_id=category).order_by(Photo.id.desc()).offset(page * 5).limit(5)

        more = Photo.query.filter_by(category_id=category).offset((page + 1) * 5).first()

        db_session.close()
        db_session.remove()
        db_session.rollback()

        if page != 0 :
            prev_url = url_for('photos.gallery', category=category, page=page - 1)
        else :
            prev_url = None

        if not more == None :
            next_url = url_for('photos.gallery', category=category, page=page + 1)
        else :
            next_url = None

        return render_template('gallery.html', Photos=photos, categories=categories, next_url=next_url, prev_url=prev_url)

    else :
        # if a no specific photo or category has been selected this if statement will be ran
        photos = Photo.query.order_by(Photo.id.desc()).offset(page * 5).limit(5)

        more = Photo.query.offset((page + 1) * 5).first()

        db_session.close()
        db_session.remove()
        db_session.rollback()

        if page != 0 :
            prev_url = url_for('photos.gallery', category=category, page=page - 1)
        else :
            prev_url = None

        if not more == None :
            next_url = url_for('photos.gallery', category=category, page=page + 1)
        else :
            next_url = None

        return render_template('gallery.html', Photos=photos, categories=categories, next_url=next_url, prev_url=prev_url)

#
# Add PhotoCategory
# Description:
#   This view adds a photo category to the database. It will call the add_photocategory
#   template and then the user will specify the name of the new photosubcategory.
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
            db_session.add(new_photocategory)
            db_session.commit()
            db_session.close()
            db_session.remove()
            db_session.rollback()
            flash('You have successfully added a new photo category')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_photocategory.html', form=form)


#
# Add Photo
# Description:
#   This view adds a photo to the database. It will call the add_photo template and
#   then the user will fill in the fieds required on the form that is presented.
#   It will then be added to the database to be called by the previously described
#   gallery view.
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
            db_session.add(new_photo)
            db_session.commit()
            db_session.close()
            db_session.remove()
            db_session.rollback()
            flash('You have successfully added a new photo!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_photo.html', form=form)

#
# Edit Photo
# Description:
#   The following is the view that will allow the user to edit a photo. The
#   user will first be directed to the edit_photo template (form.validate_on_submit()=False)
#   after the user fills the form the database will be updated (form.validate_on_submit()=True).
#   The edits will now be uploaded instead of the old version in the previously
#   explained view that displays the photos (gallery view).
#
@photos.route('/edit_photo/<int:id>', methods=['GET', 'POST'])
def edit_photo(id):
    """
    Edit a photo
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    photo = Photo.query.get(id)
    form = PhotoForm(obj=photo)
    if form.validate_on_submit():
        photo.filename = form.file_name.data
        photo.caption = form.caption.data
        photo.category_id = form.category.data.id
        photo.category = form.category.data

        db_session.commit()
        db_session.close()
        db_session.remove()
        db_session.rollback()
        flash('You have successfully edited the blog post.')

        # redirect to the home page
        return redirect(url_for('other.home'))

    form.caption.data = photo.caption
    form.file_name.data = photo.filename
    form.category.data = photo.category
    return render_template('edit_photo.html', form=form, photo=photo, title="Edit Photo")

#
# Delete Photo
# Description:
#   This is a view that will delete a photo. The id that is passed in is that of the
#   photo that will be deleted.
#
@photos.route('/delete_photo/<int:id>', methods=['GET', 'POST'])
def delete_photo(id):
    """
    Delete a photo from the database
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    photo = Photo.query.get(id)
    db_session.delete(photo)
    db_session.commit()
    db_session.close()
    db_session.remove()
    db_session.rollback()
    flash('You have successfully deleted the photo.')

    # redirect to the home page
    return redirect(url_for('other.home'))
