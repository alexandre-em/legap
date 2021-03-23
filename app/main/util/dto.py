from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'firstname': fields.String(description='user firstname')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class SheetDto:
    api = Namespace('sheet', description='sheet related operations')
    sheet = api.model('sheet', {
        'author': fields.String(required=True, description='user id ref'),
        'title': fields.String(required=True, description='title s song'),
        'url': fields.String(required=True, description='sheet s file url')
    })
