from flask import render_template, session, redirect, url_for, flash
from .. import db
from . import blogs
from .forms import PostForm, SubCategoryForm
from ..models import Post, PostCategory, PostSubCategory
from app.database import db_session
from app import models

# Notes:
#   Much difficulty was faced when deploying the website with regards to getting a
#   mysql has gone away error. It was fixed after the following three lines were added
#   after each database access
#   db_session.close()
#   db_session.remove()
#   db_session.rollback()


#
# Travel
# Description:
#   This view will pull up travel blogs for the user to look at. The posts
#   marked as a travel post has the 'category_id=1'. If there is more
#   5 blogs marked as travel then the posts will be paginated through utilizing
#   the offset and limit functions provided by sqlalchemy.
#
@blogs.route('/travel/<page>', methods=['GET', 'POST'])
@blogs.route('/travel/', defaults={'page' : 0}, methods=['GET', 'POST'])
def travel(page) :
    categories = PostSubCategory.query.all()

    page = int(page)

    blogs = db_session.query(Post).filter(Post.category_id==1).order_by(Post.id.desc()).offset(page * 5).limit(5)

    if page != 0 :
        prev_url = url_for('blogs.travel', page=page - 1)
    else :
        prev_url = None

    if blogs.count() == 6 :
        next_url = url_for('blogs.travel', page=page + 1)
    else :
        next_url = None

    db_session.close()
    db_session.remove()
    db_session.rollback()

    return render_template('travel.html', blogs=blogs, categories=categories, next_url=next_url, prev_url=prev_url)


#
# Projects
# Description:
#   This will pull up blog posts that are marked as a project blog post. The posts
#   marked as a project post has the 'category_id=2'.  If there is more
#   5 blogs marked as projects then the posts will be paginated through utilizing
#   the offset and limit functions provided by sqlalchemy.
#
#
@blogs.route('/projects/<page>', methods=['GET', 'POST'])
@blogs.route('/projects',  defaults={'page' : 0}, methods=['GET', 'POST'])
def projects(page) :
    categories = PostSubCategory.query.all()
    page = int(page)
    blogs = db_session.query(Post).filter(Post.category_id==2).order_by(Post.id.desc()).offset(page * 5).limit(5)

    more = db_session.query(Post).filter(Post.category_id==2).order_by(Post.id.desc()).offset((page + 1) * 5).first()

    db_session.close()
    db_session.remove()
    db_session.rollback()

    if page != 0 :
        prev_url = url_for('blogs.projects', page=page - 1)
    else :
        prev_url = None

    if not more == None :
        next_url = url_for('blogs.projects', page=page + 1)
    else :
        next_url = None

    return render_template('projects.html', blogs=blogs, categories=categories, next_url=next_url, prev_url=prev_url)



#
# Subcategory Blogs
# Description:
#   This view will pull up a specific subcategory of blog posts. Blog posts from a
#   subcategory could belong to either the project category or the travel category.
#   As with the travel and project category view the subcategory view is also paginated
#   in the same way.
#
@blogs.route('/subcategory_blogs/<subcategory>/<page>', methods=['GET', 'POST'])
@blogs.route('/subcategory_blogs/<subcategory>', defaults={'page' : 0}, methods=['GET', 'POST'])
def subcategory_blogs(subcategory, page) :
    categories = PostSubCategory.query.all()
    page = int(page)

    blogs = db_session.query(Post).filter(Post.subcategory_id==subcategory).order_by(Post.id.desc()).offset(page * 5).limit(5)

    more = db_session.query(Post).filter(Post.subcategory_id==subcategory).order_by(Post.id.desc()).offset((page + 1) * 5).first()

    db_session.close()
    db_session.remove()
    db_session.rollback()

    if page != 0 :
        prev_url = url_for('blogs.subcategory_blogs', subcategory=subcategory, page=page - 1)
    else :
        prev_url = None

    if not more == None :
        next_url = url_for('blogs.subcategory_blogs', subcategory=subcategory, page=page + 1)
    else :
        next_url = None

    return render_template('subcategory_blogs.html', blogs=blogs, categories=categories, next_url=next_url, prev_url=prev_url)

#
# Arbitrary Post
# Description:
#   This view loads a particular blog post. The 'id' being passed is the specific
#   id to that blog post in the database. It does not have a paginate part because it
#   only loads one post.
#
@blogs.route('/arbitrary_post/<int:id>', methods=['GET', 'POST'])
def arbitrary_post(id) :
    categories = PostSubCategory.query.all()

    blog = Post.query.get(id)

    db_session.close()
    db_session.remove()
    db_session.rollback()

    return render_template('arbitrary_post.html', blog=blog, categories=categories)

#
# Add Post
# Description:
#   This view adds a post to the database. It will call the add_post template and
#   then the user will fill in the fieds required on the form that is presented.
#   It will then be added to the database to be called by the previously described
#   views that display blog posts.
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
            db_session.add(new_post)
            db_session.commit()

            db_session.close()
            db_session.remove()
            db_session.rollback()
            flash('You have successfully added a new blog post!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_post.html', form=form)

#
# Edit Post
# Description:
#   The following is the view that will allow the user to edit a blog post. The
#   user will first be directed to the edit_post template (form.validate_on_submit()=False)
#   after the user fills the form the database will be updated (form.validate_on_submit()=True).
#   The edits will now be uploaded instead of the old version in the previously
#   explained views that load blog posts.
#
@blogs.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    """
    Edit a blog post
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    post = Post.query.get(id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.name = form.title.data
        post.content = form.content.data
        post.category_id = form.category.data.id
        post.category = form.category.data
        post.subcategory_id = form.sub_category.data.id
        post.subcategory = form.sub_category.data

        db_session.commit()

        db_session.close()
        db_session.remove()
        db_session.rollback()
        flash('You have successfully edited the blog post.')

        # redirect to the home page
        return redirect(url_for('other.home'))

    form.content.data = post.content
    form.title.data = post.name
    form.category.data = post.category
    form.sub_category.data = post.subcategory
    return render_template('edit_post.html', form=form, post=post, title="Edit Post")


#
# Delete Post
# Description:
#   This is a view that will delete a post. The id that is passed in is that of the
#   post that will be deleted.
#
@blogs.route('/delete_post/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    """
    Delete a post from the database
    """
    # check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('other.home'))

    post = Post.query.get(id)
    db_session.delete(post)
    db_session.commit()

    db_session.close()
    db_session.remove()
    db_session.rollback()
    flash('You have successfully deleted the post.')

    # redirect to the home page
    return redirect(url_for('other.home'))

#
# Add PostSubCategory
# Description:
#   This view adds a subcategory to the database. It will call the add_subcategory
#   template and then the user will specify the name of the new subcategory.
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
            db_session.add(new_subcategory)
            db_session.commit()

            db_session.close()
            db_session.remove()
            db_session.rollback()
            flash('You have successfully added a new subcategory!')
        except:
            flash('An error occured :(')

        return redirect(url_for('other.home'))

    return render_template('add_subcategory.html', form=form)
