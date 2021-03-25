from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto, UserDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/check/<token>')
@api.param('token', 'get an user info by a token')
class getAuth(Resource):
    ''' Auth Resource '''
    @cross_origin(supports_credentials=True)
    def get(self, token):
        return Auth.get_logged_in_user(token)


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @cross_origin(supports_credentials=True)
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/logout/<token>')
@api.param('token', 'get an user info by a token')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @cross_origin(supports_credentials=True)
    @api.doc('logout a user')
    def post(self, token):
        # get auth token
        auth_header = 'Bearer ' + token
        return Auth.logout_user(data=auth_header)
