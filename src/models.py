import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class person(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, primary_key=True)
    password = Column(String(250), nullable=False, primary_key=True)
    following = Column(Integer, nullable=True)
    followers = Column(Integer, nullable=True)


class post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    profile_name = Column(String(250), ForeignKey('user.id'))
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=True)
    comments = Column(Integer, nullable=True)
    person = db.relationship('person', backref='Post', lazy=True)

    
class comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    person = db.relationship('person', backref='Comments', lazy=True)


class likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comments_id = Column(Integer, ForeignKey('comments.id'))   
    person = db.relationship('person', backref='Likes', lazy=True)

   
class followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    person = db.relationship('person', backref='Follow', lazy=True)

    
class following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    person = db.relationship('person', backref='Following', lazy=True)   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e

# need to add href to all tables like in the example that Laura sent me through slack 