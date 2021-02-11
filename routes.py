from sources import *


"""API Routes"""


# ---------------------------------------------------------------------------------------------
# CREATE
# ---------------------------------------------------------------------------------------------

@app.route("/create/full", methods=["POST"])
@cross_origin()
def create_table():
    create_tb = TbUser.create_full()
    return create_tb


@app.route("/create/full", methods=["PUT", "GET", "DELETE", "PATCH"])
@cross_origin()
def create_table_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


@app.route("/create/user", methods=["POST"])
@cross_origin()
def user_create():
    param = request.get_json()
    create_user = TbUser.create_user(param["name"], param["email"])
    return create_user


@app.route("/create/user", methods=["GET", "PUT", "DELETE", "PATCH"])
@cross_origin()
def user_create_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


# ---------------------------------------------------------------------------------------------
# READ
# ---------------------------------------------------------------------------------------------

@app.route("/read/users/<_param>", methods=["GET"])
@cross_origin()
def read_users(_param):
    users = TbUser.read_users(_param)
    return users


@app.route("/read/users/<_param>", methods=["DELETE", "POST", "PUT", "PATCH"])
@cross_origin()
def read_users_locked_method(_param):
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


@app.route("/read/user/<_param>", methods=["GET"])
@cross_origin()
def read_user(_param):
    user = TbUser.read_user(_param)
    return user


@app.route("/read/user/<_param>", methods=["DELETE", "POST", "PUT", "PATCH"])
@cross_origin()
def read_user_locked_method(_param):
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


# ---------------------------------------------------------------------------------------------
# UPDATE
# ---------------------------------------------------------------------------------------------

@app.route("/update/user/<_id>", methods=["PUT"])
@cross_origin()
def update_user(_id):
    user_update = TbUser.update_user(_id, request.get_json())
    return user_update


@app.route("/update/user/<_id>", methods=["GET", "POST", "PATCH", "DELETE"])
@cross_origin()
def update_user_locked_method(_id):
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


# ---------------------------------------------------------------------------------------------
# DELETE
# ---------------------------------------------------------------------------------------------

@app.route("/delete/full", methods=["DELETE"])
@cross_origin()
def delete_table():
    table_delete = TbUser.delete_full()
    return table_delete


@app.route("/delete/full", methods=["GET", "PUT", "POST", "PATCH"])
@cross_origin()
def delete_table_locked_method():
    return GenericSource.locked_methods(GenericSource.error_not_allowed)


@app.route("/delete/user/<_id>", methods=["DELETE"])
@cross_origin()
def delete_user(_id):
    user_delete = TbUser.delete_user(_id)
    return user_delete


@app.route("/delete/user/<_id>", methods=["GET", "PUT", "POST", "PATCH"])
@cross_origin()
def delete_user_locked_method(_id):
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


@app.route("/<path:path>", methods=["GET", "PUT", "POST", "PATCH", "DELETE"])
@cross_origin()
def default_function(path):

    if path != "":
        return GenericSource.response_generator(
            GenericSource.error_access_denied,
            "error",
            False,
            "Not Permitted !"
        )
