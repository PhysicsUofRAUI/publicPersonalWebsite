from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#
# Purpose:
#     To hold instances of photos.
#
# Relationships:
#     Each photo has a PhotoCategory. The relationship goes one PhotoCategory to many
#     photos.
#
# Views and Forms Used in:
#     PhotoForm: This is the form that contains all the needed information to specify
#         an entry.
#
#     Add Photo: The view that displays the PhotoForm for the user to fill out and
#         add a new photo
#
#     Edit Photo: Displays the PhotoForm filled out with the current entry so that the
#         user can edit the entry.
#
#     Gallery: View that displays selected photos for the user
#
#     Delete Photo: Removes an entry from the database when the user requests it to be removed.
#
# Inspiration:
#     The following links database was used to model this:
#         https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#
class Photo(db.Model) :
    """
    Create Photos Table
    """

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(64), nullable=False)
    caption = db.Column(db.String(600))

    category_id = db.Column(db.Integer, db.ForeignKey('photo_categories.id'), nullable=False)

    category = db.relationship('PhotoCategory', backref=db.backref('photos', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.filename


#
# Purpose:
#     To hold instances of photos.
#
# Relationships:
#     Each PhotoCategory can be related to multiple photos. The relationship goes
#     one PhotoCategory to many photos.
#
# Views and Forms Used in:
#     PhotoForm: This is the form that contains all the needed information to specify
#         an entry. One of those fields is the photo category
#
#     PhotoCategoryForm: Will be used to add new photo categories to the database.
#
#     Add Photo: The view that displays the PhotoForm for the user to fill out and
#         add a new photo. The photo category is a field that will be filled out in
#         the add view.
#
#     Edit Photo: Displays the PhotoForm filled out with the current entry so that the
#         user can edit the entry. The photo category could be edited in this view.
#
#     Gallery: View that displays selected photos for the user. User can select specific
#         categories to look at those photos.
#
#     Add PhotoCategory: Lets the user add a new PhotoCategory
#
# Inspiration:
#     The following links database was used to model this:
#         https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#
class PhotoCategory(db.Model) :
    """
    Create Category Table For Photos
    """

    __tablename__ = 'photo_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<PhotoCategory %r>' % self.name


#
# Purpose:
#     To hold instances of blog posts.
#
# Relationships:
#     Each post has a Category and SubCategory. The relationship goes one SubCategory
#     one Category to many blog posts.
#
# Views and Forms Used in:
#     PostForm: This is the form that contains all the needed information to specify
#         an entry.
#
#     Add Post: The view that displays the PostForm for the user to fill out and
#         add a new post
#
#     Edit Post: Displays the PostForm filled out with the current entry so that the
#         user can edit the entry.
#
#     Travel: View that displays blog posts in the Travel category
#
#     Projects: View that displays blog posts in the Project category
#
#     Delete Post: Removes an entry from the database when the user requests it to be removed.
#
# Inspiration:
#     The following links database was used to model this:
#         https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#
class Post() :
    """
    Create Posts Table
    """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    content = db.Column(db.String(12000))

    # relation to category
    category_id = db.Column(db.Integer, db.ForeignKey('post_categories.id'), nullable=False)

    category = db.relationship('PostCategory', backref=db.backref('posts', lazy=True))


    # relation to subcategory
    subcategory_id = db.Column(db.Integer, db.ForeignKey('post_sub_categories.id'), nullable=False)

    subcategory = db.relationship('PostSubCategory', backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Post %r>' % self.name



#
# Purpose:
#     To hold the instances of blog post categories (Travel and Projects)
#
# Relationships:
#     Each post has a Category. The relationship goes one Category to many blog posts.
#
# Views and Forms Used in:
#     PostForm: This is the form that contains all the needed information to specify
#         an entry. Category is a field in this form
#
#     Add Post: The view that displays the PostForm for the user to fill out and
#         add a new post. A category will have to be specified
#
#     Edit Post: Displays the PostForm filled out with the current entry so that the
#         user can edit the entry. The category could be changed
#
#     Travel: View that displays blog posts in the Travel category. If the blog
#         post has Travel as a category it will be displayed
#
#     Projects: View that displays blog posts in the Project category. If the blog
#         post has Project as a category it will be displayed
#
# Inspiration:
#     The following links database was used to model this:
#         https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#
class PostCategory() :
    """
    Create Categories table For Posts
    """

    __tablename__ = 'post_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name



#
# Purpose:
#     To hold instances of subcategories of blog posts.
#
# Relationships:
#     Each post has a SubCategory. The relationship goes one SubCategory to many
#     blog posts.
#
# Views and Forms Used in:
#     PostForm: This is the form that contains all the needed information to specify
#         an entry for a blog post. The subcategory will be a field in this form
#
#     SubCategoryForm: Will be used to add new subcategory entries to the database.
#
#     Add Post: The view that displays the PostForm for the user to fill out and
#         add a new post. The SubCategory will have to be specified.
#
#     Edit Post: Displays the PostForm filled out with the current entry so that the
#         user can edit the entry. The subcategory could be edited
#
#     Travel: View that displays blog posts in the Travel category. A subcategory
#         can be selected to display more specific posts.
#
#     Projects: View that displays blog posts in the Project category. A subcategory
#         can be selected to display more specific posts.
#
# Inspiration:
#     The following links database was used to model this:
#         https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
#
class PostSubCategory() :
    """
    Create SubCategories table For Posts
    """

    __tablename__ = 'post_sub_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<CSubCategory %r>' % self.name
