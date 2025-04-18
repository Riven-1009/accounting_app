from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # income or expense
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    note = db.Column(db.String(200))
    date = db.Column(db.String(10), nullable=False)  # 'YYYY-MM-DD'