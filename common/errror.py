# # create array code and array messsage in error.py

ERROR = [
    {
        "code": 403,
        "message": "Forbidden"
    },
    {
        "code": 404,
        "message": "Not Found"
    },
    {
        "code": 405,
        "message": "Method Not Allowed"
    },
    {
        "code": 409,
        "message": "Missing required fields"
    },
    {
        "code": 500,
        "message": "Internal Server Error"
    }
    
]

def get_error_message(code):
    for error in ERROR:
        if error["code"] == code:
            return error["message"]
    return "Unknown Error"
