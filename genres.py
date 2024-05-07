from main import db


class Genres(db.Model):
    __tablename__ = 'genres'

    genre_id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
