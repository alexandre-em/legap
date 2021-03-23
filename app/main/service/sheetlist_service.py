import datetime

from app.main import db
from app.main.model.sheetlist import SheetList


def save_sheet(data):
    new_sheet = SheetList(
        author=data['author'],
        title=data['title'],
        published_on=datetime.datetime.utcnow(),
        url=data['url']
    )
    db.session.add(new_sheet)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Sheet added'
    }
    return response_object, 200


def search(keyword):
    result = SheetList.query.filter(SheetList.title.like('%'+keyword+'%'))
    return result.all()


def get_sheets():
    return SheetList.query.all()

def get_sheet(id):
    return SheetList.query.filter_by(id=id).first()
