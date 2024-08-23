# services/AuthService.py

from models.user import User, db
import jwt
import datetime

class AuthService:

    @staticmethod
    def register(data):
        if not data or not data.get('email') or not data.get('password'):
            return {'status_code': 400}
        
        if User.query.filter_by(email=data['email']).first():
            return {'status_code': 410}
        
        new_user = User(name=data['name'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully', 'status_code': 201}

    @staticmethod
    def login(data):
        user = User.query.filter_by(email=data['email']).first()

        if user and user.check_password(data['password']):
            token = jwt.encode({
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
            }, 'your_secret_key', algorithm='HS256')
            return {'message': 'Login successful', 'token': token, 'status_code': 200}
        else:
            return {'message': 'Invalid username or password', 'status_code': 401}

    @staticmethod
    def get_user_info(email):
        user = User.query.filter_by(email=email).first()

        if not user:
            return {'message': 'User not found', 'status_code': 404}
        
        return {'user': user.to_dict(), 'status_code': 200}
