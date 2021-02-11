"""API Generic Resources"""


# ---------------------------------------------------------------------------------------------
# Generic Functionally for API
# ---------------------------------------------------------------------------------------------


class GenericSource:
    error_not_found = 404
    error_not_allowed = 405
    error_bad_request = 400
    error_internal_server = 500
    error_access_denied = 403
    success_status = 200

    @staticmethod
    def response_generator(status, content_name="content", content="", message=False):
        response = [
            ["status", status],
            ["mimetype", "application/json"],
            [content_name, content],
            ["message", message],
        ]
        return dict(response)

    @staticmethod
    def locked_methods(cod):
        response = [
                ["status", cod],
                ["mimetype", "application/json"],
                ["error", False],
                ["message", "Bad Request: Method Not Allowed !"],
        ]
        return dict(response)
