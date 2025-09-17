from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Helper method to serialize the model to a dictionary."""
        return {
            'id': self.id,
            'magnitude': self.magnitude,
            'location': self.location,
            'year': self.year
        }

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
