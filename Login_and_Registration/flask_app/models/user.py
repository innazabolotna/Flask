from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT into users (first_name,last_name,email,password,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL('users_schema').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_schema').query_db(query,data)
        if len(results) < 1:
            return False
        return User(results[0])
    
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM users ORDER BY users.id DESC LIMIT 1;"
        results = connectToMySQL('users_schema').query_db(query)
        return User(results[0])
    
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users WHERE users.id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            is_valid = False
            flash("First name must be at least 2 characters.","register")
        if len(user['last_name']) < 2:
            is_valid = False
            flash("Last name must be at least 2 characters.","register")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid Email Address.","register")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.","register")
        if user['password'] != user['confirm_password']:
            is_valid = False
            flash("Passwords do not match!","register")
        
        return is_valid
    
