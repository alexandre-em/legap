from app.main import db
from app.main.model.changes import Changes


def get_all():
    return Changes.query.all()


def save_changes(data):
    new_changes = Changes(
        songname=data['songname'],
        composer=data['composer'],
        year=data['year'],
        chords=data['chords']
    )
    db.session.add(new_changes)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Changes added'
    }
    return response_object, 200


def get_changes(id):
    return Changes.query.filter_by(id=id).first()


def update_changes(id, data):
    if data:
        Changes.query.filter(Changes.id == id).\
            update(data)
        db.session.commit()
        return {
            'status': 'success',
            'message': 'Changes successfully updated.'
        }, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Changes id does not exists.',
        }
        return response_object, 404
