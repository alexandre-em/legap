from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.sheet_controller import api as sheet_ns
from .main.controller.changes_controller import api as changes_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Leg(n) API',
          version='0.01',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(sheet_ns, path='/sheet')
api.add_namespace(changes_ns, path='/changes')
