import main as db


class User(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)
    registration_date = db.Column(db.DataTime)
    password = db.Column(db.String(255), nullable=True)


