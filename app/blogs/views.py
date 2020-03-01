from flask import render_template, session, redirect, url_for, flash
from .. import db
from . import blogs
from .forms import PostForm, SubCategoryForm
from ..models import Post, PostCategory, PostSubCategory

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
#
# Useful Advice:
#     The subcategory could be specified in the url as well. It could then be checked whether that
#     passed value is null or not and that can be how subcategories are specified.
#
#     See the dream team example and https://exploreflask.com/en/latest/views.html
#
# The category_id = 1 is used to select only the Travel blog posts
#
@blogs.route('/travel/<blog>', defaults={'subcategory': None}, methods=['GET', 'POST'])
@blogs.route('/travel/<subcategory>', defaults={'blog': None}, methods=['GET', 'POST'])
@blogs.route('/travel', defaults={'subcategory': None, 'blog': None}, methods=['GET', 'POST'])
def travel(subcategory, blog) :
    categories = PostSubCategory.query.all()
    if not blog == None :
        blogs = Post.query.filter_by(id=blog)

        return render_template('travel.html', blogs=blogs)

    elif not subcategory == None :
        blogs = Post.query.filter_by(subcategory_id=subcategory, category_id=1)

        return render_template('travel.html', blogs=blogs)

    else :
        blogs = Post.query.filter_by(category_id=1)

        return render_template('travel.html', blogs=blogs, categories=categories)


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
#
# Useful Advice:
#     The subcategory could be specified in the url as well. It could then be checked whether that
#     passed value is null or not and that can be how subcategories are specified.
#
#     See the dream team example and https://exploreflask.com/en/latest/views.html
#
# Need to add query for the categories. Could also change around the GET and POST stuff.
#
@blogs.route('/projects/<blog>', defaults={'subcategory': None}, methods=['GET', 'POST'])
@blogs.route('/projects/<subcategory>', defaults={'blog': None}, methods=['GET', 'POST'])
@blogs.route('/projects', defaults={'subcategory': None, 'blog': None}, methods=['GET', 'POST'])
def projects(subcategory, blog) :
    categories = PostSubCategory.query.all()
    if not blog == None :
        blogs = Post.query.filter_by(id=blog)

        return render_template('projects.html', blogs=blogs)

    elif not subcategory == None :
        blogs = Post.query.filter_by(subcategory_id=subcategory, category_id=2)

        return render_template('projects.html', blogs=blogs)

    else :
        blogs = Post.query.filter_by(category_id=2)

        return render_template('projects.html', blogs=blogs)

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
@blogs.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """
    Add a blog post
    """
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(name=form.title.data, content=form.content.data, category_id=form.category.data.id, category=form.category.data,
            subcategory_id=form.sub_category.data.id, subcategory=form.sub_category.data)

        try:
            db.session.add(new_post)
            db.session.commit()
            flash('You have successfully added a new blog post!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_post.html', form=form)

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
#
# Useful advice:
#   the id of the post can be specified in the route. See this link: https://exploreflask.com/en/latest/views.html
#   also the dream team example does the same thing.
#   unsure of correctness of lines marked with US
#
@blogs.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    """
    Edit a blog post
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.name = form.title.data
        post.content = form.content.data
        post.category_id = form.category.data.id # US
        post.category = form.category.data # US
        post.subcategory_id = form.sub_category.data.id # US
        post.subcategory = form.sub_category.data # US

        db.session.commit()
        flash('You have successfully edited the blog post.')

        # redirect to the home page
        return redirect(url_for('other.home'))

    form.content.data = post.content
    form.title.data = post.name
    form.category.data = post.category # US
    form.sub_category.data = post.subcategory # US
    return render_template('edit_post.html', form=form, post=post, title="Edit Post")


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
@blogs.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    """
    Delete a post from the database
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('You have successfully deleted the post.')

    # redirect to the home page
    return redirect(url_for('other.home'))

#
# Add PostSubCategory
# Purpose:
#     Let the user add a new subcategory for posts.
# Method:
#     check if the user is logged in
#
#     create a SubCategoryForm
#
#     if a SubCategoryForm has been validated
#         create a new subcategory instance and make it's values equal to the submited values
#
#         try:
#             adding the new subcategory
#             flash a success message
#         except:
#             flash that an error has occured
#
#         redirect to the home page
#
#     render the add subcategory template
#
# Other functions and classes needed:
#     render_template, flash, and url_for from flask
#     SubCategoryForm from forms.py
#
@blogs.route('/add_subcategory', methods=['GET', 'POST'])
def add_subcategory():
    """
    Add a subcategory for blog posts
    """
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    form = SubCategoryForm()

    if form.validate_on_submit():
        new_subcategory = PostSubCategory(name=form.name.data)

        try:
            db.session.add(new_subcategory)
            db.session.commit()
            flash('You have successfully added a new subcategory!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_subcategory.html', form=form)
