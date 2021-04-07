from src.database.mongodb import db
import hashlib
import random
import os

class User:
    db = db.user
    def __init__(self, username=None, password=None, role="user"):
        self.dict = dict()
        self.dict["salt"] = hashlib.sha224(str(random.random()) + os.getenv("SECRET")).hexdigest()
        self.dict["username"] = username
        self.dict["encrypted_password"] = self.encrypt_password(self.dict["salt"], password)
        self.dict["role"] = role

    def encrypt_password(self, salt, password):
        return hashlib.sha224(salt, password).hexdigest()

    def is_password_good(self, password):
        return len(password) < 5

    def save(self):
        self.db.insert_one(self.dict)

    def does_password_match(self, password):
        return self.dict["encrypted_password"] == self.encrypt_password(self.dict["salt"], password)

    @classmethod
    def from_json(cls, dict):
        user = cls()
        user.dict = dict
        return user


