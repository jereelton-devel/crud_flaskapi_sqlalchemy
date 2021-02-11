from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors.decorator import cross_origin
import mysql.connector
import json
from generic_sources import *


"""API Resources"""


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devel:123mudar@localhost/localtests'

db = SQLAlchemy(app)


# ---------------------------------------------------------------------------------------------
# Model and CRUD: Create tb_user with create_all(), ex: db.create_all()
# ---------------------------------------------------------------------------------------------
class TbUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    # Create

    @staticmethod
    def create_full():

        try:

            db.create_all()

            return GenericSource.response_generator(
                GenericSource.success_status,
                "result",
                True,
                "Table created successfully !"
            )

        except NameError as ner:

            return GenericSource.response_generator(
                GenericSource.error_internal_server,
                "error",
                ner,
                "Internal Server Error !"
            )

    @staticmethod
    def create_user(param_name, param_mail):

        try:

            create_user = TbUser(name=param_name, email=param_mail)
            db.session.add(create_user)
            db.session.commit()

            return GenericSource.response_generator(
                    GenericSource.success_status,
                    'user',
                    param_name,
                    'User Created successfully !'
                )

        except Exception as er:
            return GenericSource.response_generator(
                GenericSource.error_internal_server,
                'exception',
                er,
                'Internal Server Error !'
            )

    # Read
    @staticmethod
    def read_users(_param):

        if _param != "all" and _param != "full":
            users = TbUser.query.filter(TbUser.name.like(_param+'%'), TbUser.email.like(_param+'%'))
        else:
            users = TbUser.query.all()

        users_list = [user.to_json() for user in users]

        if len(users_list) == 0:
            return GenericSource.response_generator(
                GenericSource.error_not_found,
                'users',
                users_list,
                'Users Not Found !'
            )

        return GenericSource.response_generator(
            GenericSource.success_status,
            'users',
            users_list,
            'Users listed successfully'
        )

    @staticmethod
    def read_user(param):
        user = TbUser.query.filter_by(id=param).first()

        if user is None:
            user = TbUser.query.filter(TbUser.name.like(param+'%')).first()

        if user is None:
            user = TbUser.query.filter(TbUser.email.like(param+'%')).first()

        if user is None:
            user_list = []
        else:
            user_list = user.to_json()

        if len(user_list) == 0:
            return GenericSource.response_generator(
                GenericSource.error_not_found,
                'user',
                user_list,
                'User Not Found !'
            )

        return GenericSource.response_generator(
            GenericSource.success_status,
            'user',
            user_list,
            'User listed successfully'
        )

    # Update

    @staticmethod
    def update_user(param_id, param):

        try:

            up_user = TbUser.query.filter_by(id=param_id).first()

            if up_user is None:
                return GenericSource.response_generator(
                    GenericSource.error_not_found,
                    'user',
                    param_id,
                    'User Not Found !'
                )

            if "name" in param:
                up_user.name = param["name"]

            if "email" in param:
                up_user.email = param["email"]

                db.session.add(up_user)
                db.session.commit()

            return GenericSource.response_generator(
                GenericSource.success_status,
                'user',
                param["name"],
                'User Updated successfully !'
            )

        except Exception as er:
            return GenericSource.response_generator(
                GenericSource.error_internal_server,
                'exception',
                er,
                'Internal Server Error !'
            )

    # Delete

    @staticmethod
    def delete_full():

        try:

            db.drop_all()

            return GenericSource.response_generator(
                GenericSource.success_status,
                "result",
                True,
                "Table deleted successfully !"
            )

        except Exception as er:

            return GenericSource.response_generator(
                GenericSource.error_internal_server,
                "error",
                er,
                "Internal Server Error !"
            )

    @staticmethod
    def delete_user(param_id):
        user_delete = TbUser.query.filter_by(id=param_id).first()

        if user_delete is None:
            return GenericSource.response_generator(
                GenericSource.error_not_found,
                'user_id',
                param_id,
                'User Not Found !'
            )

        try:
            db.session.delete(user_delete)
            db.session.commit()

            return GenericSource.response_generator(
                GenericSource.success_status,
                'user',
                user_delete.name,
                'User Deleted successfully !'
            )

        except Exception as er:
            return GenericSource.response_generator(
                GenericSource.error_internal_server,
                'exception',
                er,
                'Internal Server Error !'
            )

    # Generic

    def to_json(self):
        return {"id": self.id, "name": self.name, "email": self.email}
