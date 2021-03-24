from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from ..util.dto import ChangesDto
from ..service.changes_service import save_changes, get_all, get_changes, update_changes

api = ChangesDto.api
_changes = ChangesDto.changes


@api.route('/')
class SheetList(Resource):
    @cross_origin(supports_credentials=True)
    @api.doc('list of song')
    @api.marshal_with(_changes)
    def get(self):
        '''List all published changes'''
        return get_all()

    @cross_origin(supports_credentials=True)
    @api.response(201, 'Changes successfully published')
    @api.doc('publish a Change')
    @api.expect(_changes, validate=True)
    def post(self):
        '''Publish a new Change'''
        data = request.json
        return save_changes(data=data)


@api.route('/<id>')
@api.param('id', 'get a sheet by id')
@api.response(404, 'Change id not found.')
class Sheet(Resource):
    @cross_origin(supports_credentials=True)
    @api.doc('get a change')
    @api.marshal_with(_changes)
    def get(self, id):
        """get a change given its identifier"""
        change = get_changes(id)
        if not change:
            api.abort(404)
        else:
            return change

    @cross_origin(supports_credentials=True)
    @api.response(201, 'Changes successfully updated.')
    @api.doc('Update changes info')
    @api.expect(_changes)
    def put(self, id):
        '''Update Changes informations'''
        put_data = request.json
        return update_changes(id, put_data)
