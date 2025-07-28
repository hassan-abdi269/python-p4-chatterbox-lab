from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Message
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

db.init_app(app)
migrate = Migrate(app, db)


# GET /messages
@app.route('/messages', methods=['GET'])
def get_messages():
    messages = Message.query.order_by(Message.created_at).all()
    return jsonify([msg.to_dict() for msg in messages]), 200

# POST /messages
@app.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    new_msg = Message(
        body=data.get("body"),
        username=data.get("username")
    )
    db.session.add(new_msg)
    db.session.commit()
    return jsonify(new_msg.to_dict()), 201

# PATCH /messages/<id>
@app.route('/messages/<int:id>', methods=['PATCH'])
def update_message(id):
    msg = Message.query.get_or_404(id)
    data = request.get_json()
    if "body" in data:
        msg.body = data["body"]
    db.session.commit()
    return jsonify(msg.to_dict()), 200

# DELETE /messages/<id>
@app.route('/messages/<int:id>', methods=['DELETE'])
def delete_message(id):
    msg = Message.query.get_or_404(id)
    db.session.delete(msg)
    db.session.commit()
    return {}, 204
