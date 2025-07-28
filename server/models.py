from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from datetime import datetime

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    created_at = db.Column(DateTime, default=datetime.utcnow)
    updated_at = db.Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

{
  "id": 1,
  "body": "Hello",
  "username": "Duane",
  "created_at": "2025-07-28T10:00:00",
  "updated_at": "2025-07-28T10:00:00"
}


