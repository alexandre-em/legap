from .. import db

class Changes(db.Model):
    '''
    Changes model for storing ChordChanges related details
    '''
    __tablename__ = "changes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    songname = db.Column(db.String(100))
    composer = db.Column(db.String(100))
    year = db.Column(db.Integer)
    chords = db.Column(db.String(950))