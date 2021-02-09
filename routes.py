from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors.decorator import cross_origin
import mysql.connector
import json
from sources import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devel:123mudar@localhost/localtests'

db = SQLAlchemy(app)


class TbUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}


# List all
@app.route("/users", methods=["GET"])
@cross_origin()
def select_user():
    users = TbUser.query.all()
    users_list = [user.to_json() for user in users]
    print(users_list)

    return response_generator(
        '200',
        'users',
        users_list,
        'User listed successfully'
    )


@app.route("/users", methods=["POST"])
@cross_origin()
def method_blocked_users():
    return response_generator(
        '400',
        'error',
        False,
        'Method not available'
    )


# List one
@app.route("/user/<_id>", methods=["GET"])
@cross_origin()
def select_one_user(_id):
    user = TbUser.query.filter_by(id=_id).first()
    user_list = user.to_json()

    return response_generator(
        '200',
        'user',
        user_list,
        'User listed successfully'
    )


# Create item
@app.route("/useradd", methods=["POST"])
@cross_origin()
def user_create():
    param = request.get_json()

    try:
        create_user = TbUser(name=param["name"], email=param["email"])
        db.session.add(create_user)
        db.session.commit()

        return response_generator(
                '200',
                'user',
                param["name"],
                'User Created successfully !'
            )

    except Exception as er:
        return response_generator(
            '500',
            'exception',
            er,
            'Internal Server Error !'
        )


# Update data
@app.route("/userup/<_id>", methods=["PUT"])
@cross_origin()
def update_user(_id):
    param = request.get_json()
    up_user = TbUser.query.filter_by(id=_id).first()

    try:
        if "name" in param:
            up_user.name = param["name"]

        if "email" in param:
            up_user.email = param["email"]

            db.session.add(up_user)
            db.session.commit()

        return response_generator(
                '200',
                'user',
                param["name"],
                'User Updated successfully !'
            )

    except Exception as er:
        return response_generator(
            '500',
            'exception',
            er,
            'Internal Server Error !'
        )


# Delete item
@app.route("/userdel/<_id>", methods=["DELETE"])
@cross_origin()
def user_delete(_id):
    delete_user = TbUser.query.filter_by(id=_id).first()

    if delete_user is None:
        return response_generator(
            '404',
            'error',
            delete_user,
            'User Not Found !'
        )

    try:
        db.session.delete(delete_user)
        db.session.commit()

        return response_generator(
                '200',
                'user',
                delete_user.name,
                'User Deleted successfully !'
            )

    except Exception as er:
        return response_generator(
            '500',
            'exception',
            er,
            'Internal Server Error !'
        )


# Not Permission
@app.route("/")
@cross_origin()
def access_denied():
    return response_generator(
        403,
        "error",
        False,
        "Access Denied !"
    )


# db.create_all()
