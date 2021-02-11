from sources import *
from generic_sources import *


"""API Routes"""


# List all
@app.route("/users", methods=["GET"])
@cross_origin()
def select_user():
    users = TbUser.query.all()
    users_list = [user.to_json() for user in users]
    print(users_list)
    print(len(users_list))

    if len(users_list) == 0:
        return GenericSource.response_generator(
            '404',
            'users',
            users_list,
            'Users Not Found !'
        )

    return GenericSource.response_generator(
        '200',
        'users',
        users_list,
        'User listed successfully'
    )


@app.route("/users", methods=["POST"])
@cross_origin()
def method_blocked_users():
    return GenericSource.response_generator(
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

    return GenericSource.response_generator(
        '200',
        'user',
        user_list,
        'User listed successfully'
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

        return GenericSource.response_generator(
                '200',
                'user',
                param["name"],
                'User Updated successfully !'
            )

    except Exception as er:
        return GenericSource.response_generator(
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
        return GenericSource.response_generator(
            '404',
            'error',
            delete_user,
            'User Not Found !'
        )

    try:
        db.session.delete(delete_user)
        db.session.commit()

        return GenericSource.response_generator(
                '200',
                'user',
                delete_user.name,
                'User Deleted successfully !'
            )

    except Exception as er:
        return GenericSource.response_generator(
            '500',
            'exception',
            er,
            'Internal Server Error !'
        )


# ---------------------------------------------------------------------------------------------
# CREATE
# ---------------------------------------------------------------------------------------------

@app.route("/create/full", methods=["POST"])
@cross_origin()
def create_table():

    try:

        create_tb = TbUser.create_full()

        return GenericSource.response_generator(
            GenericSource.success_status,
            "result",
            create_tb,
            "Table created successfully !"
        )

    except NameError as ner:

        return GenericSource.response_generator(
            GenericSource.error_internal_server,
            "error",
            ner,
            "Internal Server Error !"
        )


@app.route("/create/full", methods=["PUT", "GET", "DELETE", "PATCH"])
@cross_origin()
def create_table_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


@app.route("/useradd", methods=["POST"])
@cross_origin()
def user_create():
    param = request.get_json()

    try:
        create_user = TbUser().create_user(param["name"], param["email"])

        return GenericSource.response_generator(
                GenericSource.success_status,
                'user',
                param["name"],
                'User Created successfully !'
            )

    except Exception as er:
        return GenericSource.response_generator(
            GenericSource.error_internal_server,
            'exception',
            er,
            'Internal Server Error !'
        )


@app.route("/useradd", methods=["GET", "PUT", "DELETE", "PATCH"])
@cross_origin()
def user_create_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


# ---------------------------------------------------------------------------------------------
# DELETE
# ---------------------------------------------------------------------------------------------

@app.route("/delete/full", methods=["DELETE"])
@cross_origin()
def delete_table():

    try:

        delete_tb = TbUser.delete_full()

        return GenericSource.response_generator(
            GenericSource.success_status,
            "result",
            delete_tb,
            "Table deleted successfully !"
        )

    except NameError as ner:

        return GenericSource.response_generator(
            GenericSource.error_internal_server,
            "error",
            ner,
            "Internal Server Error !"
        )


@app.route("/delete/full", methods=["GET", "PUT", "POST", "PATCH"])
@cross_origin()
def delete_table_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


# ---------------------------------------------------------------------------------------------
# EXTRA: Not Permission
# ---------------------------------------------------------------------------------------------

@app.route("/", methods=["GET", "PUT", "POST", "PATCH", "DELETE"])
@cross_origin()
def access_denied():
    return GenericSource.response_generator(
        GenericSource.error_access_denied,
        "error",
        False,
        "Access Denied !"
    )
