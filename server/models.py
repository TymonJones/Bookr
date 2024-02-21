from flask import current_app
from google.cloud import firestore

db = firestore.Client(current_app)

class User:
    def __init__(self, uid, email, display_name):
        self.uid = uid
        self.email = email
        self.display_name = display_name

    def to_dict(self):
        return {
            'uid': self.uid,
            'email': self.email,
            'display_name': self.display_name
        }

    @staticmethod
    def from_dict(source):
        return User(
            uid=source['uid'],
            email=source['email'],
            display_name=source['display_name']
        )

    @staticmethod
    def create(uid, email, display_name):
        user_ref = db.collection('Users').document(uid)  # Updated collection name
        user_ref.set({
            'email': email,
            'display_name': display_name
        })

    @staticmethod
    def get(uid):
        user_ref = db.collection('Users').document(uid)  # Updated collection name
        user_doc = user_ref.get()
        if user_doc.exists:
            return User.from_dict(user_doc.to_dict())
        else:
            return None
