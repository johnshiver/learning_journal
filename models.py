import datetime
import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

import markdown

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://{}:{}@localhost/john_blog".format(db_user, db_password)
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/john_blog"

db = SQLAlchemy(app)


def colorize_text(user_input):
    return highlight(user_input, PythonLexer(), HtmlFormatter())


def markdown_text(user_input):
    return markdown.markdown(user_input, extensions=['codehilite'])


class Post(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(127))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, body, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.datetime.utcnow()
        self.pub_date = pub_date

    def __repr__(self):
        return "<Post %r>" % self.title

    def update_entry(self, title, text, id):
        pass

    def write_entry(title, body):
        if not title or not body:
            raise ValueError("Title and text required for writing an entry")
        new_entry = Post(title, body)
        db.session.add(new_entry)
        db.session.commit()

    def get_all_entries(self):
        """return a list of all entries as dicts"""
        all_posts = Post.query.all()
        keys = ('id', 'title', 'text', 'created')
        theList = [dict(zip(keys, row)) for row in all_posts]
        for aDict in theList:
            aDict['text'] = markdown_text(aDict['text'])
        return theList

    def get_one_entry(self, id):
        pass















