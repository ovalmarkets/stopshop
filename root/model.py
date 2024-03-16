from root import db,login_manager
from root import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key = True)
    username = db.Column(db.String(length=30),nullable = False,unique=True)
    password = db.Column(db.String(length=1000),nullable=False)

class blogdb(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key = True)
    owner = db.Column(db.String())
    title = db.Column(db.String(length=30),nullable = False,unique=True)
    blogdata = db.Column(db.String(length=1000),nullable=False)