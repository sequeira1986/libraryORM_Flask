from main import db


class Books(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.integer, primary_key=True)
    title = db.Column(db.String(255))
    author_id = db.Column(db.integer, unique=True)
    genres_id = db.Column(db.integer, unique=True)
    isbn = db.Column(db.String(13))
    publication_year = db.Column(db.integer)
    copies = db.Column(db.integer, default=1)

    author = db.relationship("Author", book_populates="books")
    genres = db.relationship("Genres", book_populates="books")
