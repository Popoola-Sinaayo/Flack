import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "Website_Users"
    id = db.Column(db.Integer, primary_key=True)
    Email = db.Column(db.String)
    Display_Name = db.Column(db.String)
    def __init__ (self, id, Email, Display_Name):
        self.id = id
        self.Email = Email
        self.Display_Name = Display_Name
