
def response_generator(status, content_name="content", content="", message=False):

    response = {
        "status": status,
        "mimetype": "application/json",
        content_name: content,
        "message": message
    }

    return response
