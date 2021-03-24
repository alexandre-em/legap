from flask import request
from flask_restplus import Resource
from flask_cors import cross_origin

from ..util.dto import SheetDto
from ..service.sheetlist_service import save_sheet, get_sheets, get_sheet, search

api = SheetDto.api
_sheet = SheetDto.sheet


@api.route('/')
class SheetList(Resource):
    @cross_origin(supports_credentials=True)
    @api.doc('list of sheets')
    @api.marshal_list_with(_sheet, envelope='data')
    def get(self):
        '''List all published sheets'''
        return get_sheets()
    
    @cross_origin(supports_credentials=True)
    @api.response(201, 'Sheet successfully published')
    @api.doc('publish a sheet')
    @api.expect(_sheet, validate=True)
    def post(self):
        '''Publish a new sheet'''
        data=request.json
        return save_sheet(data=data)


@api.route('/search/<keyword>')
@api.param('keyword', 'search keyword')
@api.response(404, 'Sheet not found.')
class SearchSheet(Resource):
    @cross_origin(supports_credentials=True)
    @api.doc('search a sheet by keyword')
    @api.marshal_list_with(_sheet, envelope='data')
    def get(self, keyword):
        '''get sheets by keyword'''
        sheets = search(keyword)
        return sheets


@api.route('/id/<id>')
@api.param('id', 'get a sheet by id')
@api.response(404, 'Sheet not found.')
class Sheet(Resource):
    @cross_origin(supports_credentials=True)
    @api.doc('get a sheet')
    @api.marshal_with(_sheet)
    def get(self, id):
        """get a sheet given its identifier"""
        sheet = get_sheet(id)
        if not sheet:
            api.abort(404)
        else:
            return sheet
