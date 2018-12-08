import sqlite3
from flask_restful import Resource, reqparse

class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

# Class methods just mean to use the current class name instead of explicitly defining it (cls = "User")
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from users where username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        # If row is not None, create User object passing values from first 3 columns
        if row:
            # *row is just creating positional arguments rather than writing out row[0], row[1], row[2]
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "select * from users where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        # If row is not None, create User object passing values from first 3 columns
        if row:
            # *row is just creating positional arguments rather than writing out row[0], row[1], row[2]
            user = cls(*row)
        else:
            user = None
        connection.close()
        return _id

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required = True,
                        help = "This field cannot be left blank!"
    )
    parser.add_argument('password',
                        type = str,
                        required = True,
                        help = "This field cannot be left blank!"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL, ?, ?)'
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()
        return {'message': 'User created successfully.'}, 201
