from flask import Flask
from flask import request
from flask import jsonify
import json
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

startingID = 10000
def generateID():
    return random.randint(10000, 99999)

users = {
    'users_list' :
    [
        { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
        },
        {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
        },
        {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
        }, 
        {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
        },
        {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_username = request.args.get('name')
        if search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd[id] = generateID()
        users['users_list'].append(userToAdd)
        resp = jsonify(success=True)
        resp.status_code = 201
        return resp
    else:
        return 'Invallid HTTP operation'

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def handle_user(id):
    if request.method == 'GET':
        if id :
            for user in users['users_list']:
                if user['id'] == id:
                    return user
            return ({})
        return users
    elif request.method == 'DELETE':
        if id:
            for user in users['users_list']:
                if user['id'] == id:
                    users['users_list'].remove(user)
                    return jsonify(success=True)
        return jsonify(success=False)
