from root import db


class blogdb(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    owner = db.Column(db.String())
    title = db.Column(db.String(length=30),nullable = False,unique=True)
    blogdata = db.Column(db.String(length=1000),nullable=False)