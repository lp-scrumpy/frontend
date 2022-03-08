from http import HTTPStatus
from flask import Flask, jsonify, request
from uuid import uuid4


users_name = {
    "2e23eb29-b203-4092-859f-8cd26ccec909": {
        "uid": "2e23eb29-b203-4092-859f-8cd26ccec909",
        "username": "Миша",
    },
    "229aeb06-ba19-47db-8652-441f1e8eb950": {
        "uid": "2e23eb29-b203-4092-859f-8cd26ccec909",
        "username": "Маша",
    },
}

app = Flask(__name__)

@app.get('/api/users/')
def get_users():
    users = [user for _, user in users_name.items()]
    return jsonify(users)


@app.get('/api/users/<uid>')
def get_user_id(uid):
    user = users_name.get(uid)
    if not user:
        return {'message':'user not found'}, HTTPStatus.NOT_FOUND

    return user

@app.post('/api/users/')
def add_user():
    user = request.json
    user['uid'] = uuid4().hex
    users_name[user['uid']] = user
    return user, HTTPStatus.CREATED

@app.put('/api/users/<uid>')
def update_user(uid):
    if uid not in users_name:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND

    user = request.json

    users_name[uid] = user
    return user, HTTPStatus.OK

@app.delete('/api/users/<uid>')
def delete_user(uid):
    if uid not in users_name:
        return {"message":"user not found"}, HTTPStatus.NOT_FOUND
    users_name.pop(uid)
    return {}, HTTPStatus.NO_CONTENT

