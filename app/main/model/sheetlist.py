from .. import db

class SheetList(db.Model):
    """ 
    SheetList Model for storing sheets related details
    """
    __tablename__ = "sheetlist"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100))
    published_on = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(512))
