# services/AuthService.py

from models.user import User, db
import jwt
import datetime
from services.email_service import send_verification_email
from common.error import generate_error_response  

class AuthService:

    @staticmethod
    def register(data):
        if not data or not data.get('email') or not data.get('password'):
            return generate_error_response(400)  
        
        if User.query.filter_by(email=data['email']).first():
            return generate_error_response(409)  
        
        new_user = User(name=data['name'], email=data['email'])
        new_user.set_password(data['password'])
        new_user.status = 0  
        db.session.add(new_user)
        db.session.commit()

        token = jwt.encode({
            'user_id': new_user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, 'your_secret_key', algorithm='HS256')

        send_verification_email(new_user.email, token)

        return {
            'message': 'User registered successfully. Please check your email to verify your account.',
            'status_code': 201
        }

    @staticmethod
    def verify_email(token):
        try:
            payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            user_id = payload['user_id']
            user = User.query.get(user_id)
            if user:
                user.status = 1 
                db.session.commit()
                return {'message': 'Email verified successfully', 'status_code': 200}
            else:
                return generate_error_response(404)
        except jwt.ExpiredSignatureError:
            return generate_error_response(400)
        except jwt.InvalidTokenError:
            return generate_error_response(400)

    @staticmethod
    def login(data):
        user = User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            if user.status == 0:
                return generate_error_response(403)

            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, 'your_secret_key', algorithm='HS256')
            return {'message': 'Login successful', 'token': token, 'status_code': 200}
        else:
            return generate_error_response(401)

    @staticmethod
    def get_user_info(email):
        user = User.query.filter_by(email=email).first()

        if not user:
            return generate_error_response(404)
        
        return {'user': user.to_dict(), 'status_code': 200}
