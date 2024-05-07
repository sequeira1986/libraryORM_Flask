from datetime import datetime

from flask import request, jsonify

from main import db, app


class Members(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    registration_date = db.Column(db.DateTime)
    password = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "registration_date": self.registration_date,
            "password": self.password
        }


