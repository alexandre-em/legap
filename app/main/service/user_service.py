import uuid
import datetime

from app.main import db, flask_bcrypt
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            firstname=data['firstname'],
            avatar=data['avatar'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def update_user(id, data):
    if data:
        new_data = data
        if 'password' in new_data:
            password = data['password']
            new_data.pop('password')
            new_data['password_hash'] = flask_bcrypt.generate_password_hash(
                password).decode('utf-8')
        User.query.filter(User.public_id==id).\
            update(new_data)
        db.session.commit()
        return {
            'status': 'success',
            'message': 'User successfully updated.'
        }, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User does not exists.',
        }
        return response_object, 404


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401
