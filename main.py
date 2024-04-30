from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2


main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ulwgoripw8ejfilgoi5u:yIus83C46Zx1VgDBZ5UjzY04BQrST3@brgeicfqg8kyazonirom-postgresql.services.clever-cloud.com:50013/brgeicfqg8kyazonirom'
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(main)
from authors import Author

@main.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return authors


if __name__ == '__main__':
    main.run()
