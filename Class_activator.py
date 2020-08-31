import os

from classes import *

from flask import Flask

app = Flask(__name__)
# the connection to the database follows the following
#1 postgres is the name of postgresql deafault connection
#2 postgres(second) owner of the database we are trying to connect to!
#Prayer1020 is password
# localhost served locally of coutse
#Flack_App is the name of the database that i am trying to connect to!
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://postgres:Prayer1020@localhost:5432/Flack_App'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def Create():
    db.create_all()
    print("Table Created Succesfully!")

if __name__ == "__main__":
    with app.app_context():
        Create()
