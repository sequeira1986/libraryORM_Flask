from datetime import datetime

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from member.member_descriptor import Member

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://ulwgoripw8ejfilgoi5u:yIus83C46Zx1VgDBZ5UjzY04BQrST3@brgeicfqg8kyazonirom-postgresql.services.clever-cloud.com:50013/brgeicfqg8kyazonirom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from Author import Author
from Members import Members
from flask import jsonify


@app.route("/authors/", methods=['GET'])
def getAuthors():
    authors = Author.query.all()
    author_list = [
        {"author_id": author.author_id, "name": author.name, "bio": author.bio}
        for author in authors
    ]
    return jsonify(author_list)


@app.route("/members/", methods=['GET'])
def getMembers():
    members = Members.query.all()
    member_list = [mem.to_dict() for mem in members]
    return jsonify(member_list)


@app.route("/members/<int:member_id>", methods=['GET'])
def getMemberById(member_id):
    if request.method == 'GET':
        member = Members.query.get(member_id)
        if member:
            return jsonify(member.to_dict())
        else:
            return jsonify({"error": "Member not found"}), 404


@app.route("/members", methods=['POST'])
def addMember():
    if request.method == 'POST':
        data = request.json
        new_member = Members(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            registration_date=datetime.now(),  # Assuming you're using datetime module
            password=data.get('password')
        )
        db.session.add(new_member)
        db.session.commit()
        return jsonify({"message": "Member added successfully",
                        "member_id": new_member.member_id,
                        "member_details": new_member.to_dict()}), 201


if __name__ == "__main__":
    app.run(debug=True)
