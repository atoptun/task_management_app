from app import app, db
from app.models.models import Task, User
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password required'}), 400
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200


@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_id = get_jwt_identity()
    tasks = Task.query.filter_by(owner_id=current_user_id).all()
    return jsonify([task.to_dict() for task in tasks])


@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        owner_id=data['owner_id'],
        status=data.get('status', "невиконана")
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201


@app.route('/tasks/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())


@app.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data['title']
    task.description = data.get('description')
    task.status = data.get('status', task.status)
    task.owner_id = data['owner_id']
    db.session.commit()
    return jsonify(task.to_dict())


@app.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
