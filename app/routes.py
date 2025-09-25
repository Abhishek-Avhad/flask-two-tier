from flask import Blueprint, jsonify, request
from . import db
from .models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return jsonify({'message': 'Hello from Flask two-tier app'})

@main_bp.route('/users', methods=['GET'])
def list_users():
    users = User.query.all()
    return jsonify([u.as_dict() for u in users])

@main_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json() or {}
    name = data.get('name')
    if not name:
        return jsonify({'error': 'name is required'}), 400
    u = User(name=name)
    db.session.add(u)
    db.session.commit()
    return jsonify(u.as_dict()), 201
