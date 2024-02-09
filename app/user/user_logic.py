from flask_restful import Resource
from app.user.user_tables import User
from flask import request
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

class GetUsers(Resource):
    def get(self):
        user = User.query.all()
        if user:
            return {"username": user.username, "email": user.email}, 200
        else:
            return {"message": "User not found"}, 404
    
    def post(self):
        try:
            data = request.get_json()
            new_user = User( 
                username = data.get('username'),
                password = data.get('password'),
                email = data.get('email'),
                mobile = data.get('mobile'),
                city = data.get('city'),
                designation = data.get('designation')
            )
            db.session.add(new_user)
            db.session.commit()

            access_token = create_access_token(identity=new_user.id)

            return {'message': 'User registered successfully', 'token': access_token}, 200
        
        except Exception as e:
            return {'message': 'User registration failed'}, 500
        
#Logic fro user login
class UserLogin(Resource):
    def post(self):
        try:
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')

            #check if user exist in DB
            user = User.query.filter_by(username=username).first()

            #logic to authenticate
            if user:
                if user.password == password:
                    #create jwt token for user
                    user_token = create_access_token(identity=user.id)
                    return {'Access Token': user_token}, 200
                return {'message': 'invalid password'}, 401
            
            else:
                return {'message': 'User not found'}, 400
            
        except Exception as e:
            return {'message': 'User login failed'}, 400

#Api to get information
#restricting to access user information without the bearer token
class UserInfo(Resource):
    @jwt_required()
    def get(self):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        user_data = {
            'id': user.id,
            'username': user.username
            
        }

        return {"success": "User Data"}