# common/error.py

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
        "message": "Email đã cũ"
    },
    {
        "code": 500,
        "message": "Internal Server Error"
    }
]

def generate_error_response(code):
    message = next((error['message'] for error in ERROR if error['code'] == code), "Unknown Error")
    return {'message': message, 'status_code': code}
