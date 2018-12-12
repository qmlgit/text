from .import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(120),unique=True)

    def __init__(self,username,password):
        self.username = username
        self.password = password

class Words(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer,primary_key=True)
    word = db.Column(db.String(255))
    interpret = db.Column(db.String(512))

    def to_dict(self):
        dic = {
            'id':self.id,
            'interpret':self.interpret
        }
        return dic