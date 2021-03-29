from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'firstname': fields.String(description='user firstname'),
        'avatar': fields.String(description='avatar url'),
        'public_id': fields.String(description='public id')
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
        'id': fields.Integer(required=False, description='sheet id'),
        'author': fields.String(required=True, description='user id ref'),
        'title': fields.String(required=True, description='title s song'),
        'url': fields.String(required=True, description='sheet s file url'),
        'composer': fields.String(required=True, description='song s composer name'),
        'year': fields.String(required=True, description='year the song was composed'),
        'published_on': fields.DateTime(required=False, description='publication date')
    })


class ChangesDto:
    api = Namespace('changes', description='chord changes related operations')
    changes = api.model('changes', {
        'songname': fields.String(required=True, description='song name'),
        'composer': fields.String(required=True, description='song composer'),
        'year': fields.String(required=True, description='song year'),
        'chords': fields.String(required=True, description='chord changes separator /./ between root and tone and /|/ between each chord')
    })
