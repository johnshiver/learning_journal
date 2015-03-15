import datetime
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.login import UserMixin

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from werkzeug.security import generate_password_hash, check_password_hash

import markdown

from utils import slugify

db_user = os.environ.get('BLOG_DB_USER', None)
db_password = os.environ.get('BLOG_DB_PASSWORD', None)
host = os.environ.get('BLOG_DB_HOST', None)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@{}/john_blog".format(db_user, db_password, host)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def colorize_text(user_input):
    return highlight(user_input, PythonLexer(), HtmlFormatter())


def markdown_text(user_input):
    return markdown.markdown(user_input, extensions=['codehilite'])


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)
    slug = db.Column(db.String(127))

    def __init__(self, title, body, slug=None, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.datetime.utcnow()
        if slug is None:
            slug = slugify(self.title)
        self.slug = slug
        self.pub_date = pub_date

    def __repr__(self):
        return slugify(self.title)


def update_entry(title, text, id):
    print title, text, id
    print 'update entry here'
    post = Post.query.filter_by(id=id).first()
    post.title = title
    post.body = text
    db.session.commit()


def write_entry(title, body):
    if not title or not body:
        raise ValueError("Title and text required for writing an entry")
    new_entry = Post(title, body)
    db.session.add(new_entry)
    db.session.commit()


def get_five_entries():
    """return a list of all entries as dicts"""
    all_posts = Post.query.order_by(Post.id.desc()).limit(5).all()
    for post in all_posts:
        post.body = markdown_text(post.body)
    return all_posts


def get_all_entries():
    """return a list of all entries as dicts"""
    all_posts = Post.query.order_by(Post.id.desc()).all()
    for post in all_posts:
        post.body = markdown_text(post.body)
    return all_posts


def get_one_entry(tite):
    post = Post.query.filter_by(id=id).first()
    return post


def delete_post(id):
    p = get_one_entry(id)
    db.session.delete(p)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
