from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors.decorator import cross_origin
import mysql.connector
import json


"""API Resources"""


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devel:123mudar@localhost/localtests'

db = SQLAlchemy(app)


# ---------------------------------------------------------------------------------------------
# Model: Create tb_user with create_all(), ex: db.create_all()
# ---------------------------------------------------------------------------------------------
class TbUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    @staticmethod
    def create_full():
        db.create_all()
        return True

    @staticmethod
    def delete_full():
        db.drop_all()
        return True

    # Create

    @staticmethod
    def create_user(param_name, param_mail):
        create_user = TbUser(name=param_name, email=param_mail)
        db.session.add(create_user)
        commit = db.session.commit()
        return commit


# ---------------------------------------------------------------------------------------------
# Data Handle and Connection
# ---------------------------------------------------------------------------------------------
class CrudHandler:
    def __init__(self, _app):
        self.db_instance(_app)

    def db_instance(self, app):
        self.db = SQLAlchemy(app)
        return self.db

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    def set_id(self, _id):
        self.id = _id

    def set_name(self, _name):
        self.name = _name

    def set_name(self, _email):
        self.email = _email

    def set_all(self, _id, _name, _email):
        self.id = _id
        self.name = _name
        self.email = _email

    def get_all(self):
        return self.to_json()

    # Read
    def read_all(self):
        self.items = self.db.query.all()
        return self.items

    def read_one(self):
        self.items = self.db.query.all()
        return self.items

    # Update
    def update_user(self):
        self.items = self.db.query.all()
        return self.items

    # Delete
    def delete_user(self):
        self.items = self.db.query.all()
        return self.items


# ---------------------------------------------------------------------------------------------
# Create dynamic table by model
# ---------------------------------------------------------------------------------------------
class CreateTable:
    def __init__(self, tb):
        self.tb = tb

    @staticmethod
    def create_full():
        db.create_all()
        return True


# ---------------------------------------------------------------------------------------------
# Drop table
# ---------------------------------------------------------------------------------------------
class DeleteTable:
    def __init__(self, tb):
        self.tb = tb

    @staticmethod
    def delete_full():
        db.drop_all()
        return True
