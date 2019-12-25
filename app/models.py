#
# This will largely be deleted/redone in the final version.
# I just wanted to use this to roughly detail what I wanted the
# database to look like
#

class Photo() :
    """
    Create Photos Table
    """

    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(64), index=True, unique=True)
    caption = db.Column(db.String(1200))

class PhotoCategory() :
    """
    Create Category Table For Photos
    """

    __tablename__ = 'photo_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    photos = db.relationship('Photo', backref='PhotoCategory', lazy='dynamic')


class Post() :
    """
    Create Posts Table
    """

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    content = db.Column(db.String(12000))

class PostCategory() :
    """
    Create Categories table For Posts
    """

    __tablename__ = 'post_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    posts = db.relationship('Post', backref='PostCategory', lazy='dynamic')
    sub_categories = db.relationship('SubCategory', backref='PostCategory', lazy='dynamic')

class PostSubCategory() :
    """
    Create SubCategories table For Posts
    """

    __tablename__ = 'post_sub_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    photos = db.relationship('Post', backref='PostSubCategory', lazy='dynamic')
