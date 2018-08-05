# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from datetime import datetime

from app import db


class Messages(db.Model):
    __tablename__ = 'messages'
    id = db.Column('id', db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime)
    json = db.Column(db.String)
    parse = db.Column(db.Boolean)

    def __init__(self, json):
        self.json = json
        self.parse = False
        self.pub_date = datetime.utcnow()

