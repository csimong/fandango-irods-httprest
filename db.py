from flask_sqlalchemy import SQLAlchemy

# Instanciate SQLAlchemy
db = SQLAlchemy() 

# DB Models
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    details = db.Column(db.String(1200), nullable=False)
    rawdata = db.Column(db.String(1200), nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'details': self.details,
            'rawdata': self.rawdata,
        }