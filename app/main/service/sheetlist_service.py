import datetime

from app.main import db
from app.main.model.sheetlist import SheetList


def save_sheet(data):
    new_sheet = SheetList(
        author=data['author'],
        title=data['title'],
        published_on=datetime.datetime.utcnow(),
        url=data['url'],
        composer=data['composer'],
        year=data['year']
    )
    db.session.add(new_sheet)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Sheet added'
    }
    return response_object, 200


def search(keyword, page, per_page):
    result = SheetList.query.filter(SheetList.title.ilike('%'+keyword+'%'))
    return result.paginate(page=page, per_page=per_page)


def get_sheets(page, per_page):
    return SheetList.query.paginate(page=page, per_page=per_page)


def get_sheet(id):
    return SheetList.query.filter_by(id=id).first()


def dict_sheet_pagination (response):
    return {
        'data': [{
            'id': item.id,
            'author': item.author,
            'title': item.title,
            'url': item.url,
            'published_on': item.published_on,
            'composer': item.composer,
            'year': item.year
        } for item in response.items],
        'pages': response.pages,
        'total': response.total
    }
