"""
.. module:: models
   :synopsis: Contains model of a Content Record

.. moduleauthor:: Sebastian Schwindt <github.com/sschwindt>


"""

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from newAPI.database import metadata, db_session


# class Teacher defining each column in our company table
class Content(object):
    """This class is the model of a new Content record.
    """
    query = db_session.query_property()

    def __init__(self, id=None, name=None, location=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return '<Content %r %r %r>' % (self.id, self.name, self.location)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }


# Metadata of the content table
content = Table('content', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String(120), unique=True, nullable=False),
                Column('location', String(120)))

# Map the teacher metadata to the class Content
mapper(Content, teacher)