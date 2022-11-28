from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text(400), nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return self.title